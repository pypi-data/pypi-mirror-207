from contextlib import contextmanager

import logging
from functools import wraps, lru_cache
from typing import Dict, List

from ..device import MemoryKind, Memory, Architecture, Device

import numpy

logger = logging.getLogger(__name__)

try:
    import cupy
    import cupy.cuda
except (ImportError, AttributeError):
    import inspect
    # Ignore the exception if the stack includes the doc generator
    if all(
        "sphinx" not in f.filename
        for f in inspect.getouterframes(inspect.currentframe())
    ):
        raise
    cupy = None

__all__ = ["gpu", "cupy"]


class _DeviceCUPy:
    def __init__(self, ctx: "_GPUDevice"):
        self._ctx: "_GPUDevice" = ctx

    def __getattr__(self, item: str):
        v = getattr(cupy, item)
        if callable(v):

            def _wrap_for_device(ctx: "_GPUDevice", f):
                @wraps(f)
                def ff(*args, **kwds):
                    with ctx._device_context():
                        return f(*args, **kwds)

                return ff

            return _wrap_for_device(self._ctx, v)
        return v


class _GPUMemory(Memory):
    @property
    @lru_cache(None)
    def np(self):
        return _DeviceCUPy(self.device)

    def asarray_async(self, src):
        if isinstance(src, cupy.ndarray) and src.device.id == self.device.index:
            return src
        if not (src.flags['C_CONTIGUOUS'] or src.flags['F_CONTIGUOUS']):
            raise NotImplementedError(
                'Only contiguous arrays are currently supported for gpu-gpu transfers.'
            )
        dst = cupy.empty_like(src)
        dst.data.copy_from_device_async(src.data, src.nbytes)
        return dst

    def __call__(self, target):
        # TODO Several threads could share the same device object.
        #      It causes data race and CUDA context is incorrectly set.
        #      For now, this remove assumes that one device is always
        #      assigned to one task.
        # FIXME This code breaks the semantics since a different device
        #       could copy data on the current device to a remote device.
        #with self.device._device_context():
        with cupy.cuda.Device(self.device.index):
            if isinstance(target, numpy.ndarray):
                logger.debug("Moving data: CPU => %r", cupy.cuda.Device())
                return cupy.asarray(target)
            elif isinstance(target, cupy.ndarray) and \
                 cupy.cuda.Device() != getattr(target, "device", None):
                logger.debug(
                    "Moving data: %r => %r", getattr(target, "device", None),
                    cupy.cuda.Device()
                )
                return self.asarray_async(target)
            elif hasattr(target, 'all_to'):  # FIXME for crosspy array
                return target.all_to(self.device.index)
            else:
                logger.debug(
                    "NOT moving data of type %r to %r", target,
                    cupy.cuda.Device()
                )
                return target


# from ..environments import EnvironmentComponent  # for inheritance
# from . import component
class _GPUDevice(Device):
    @property
    @lru_cache(None)
    def resources(self) -> Dict[str, float]:
        dev = cupy.cuda.Device(self.index)
        free, total = dev.mem_info
        attrs = dev.attributes
        return dict(
            threads=attrs["MultiProcessorCount"] *
            attrs["MaxThreadsPerMultiProcessor"],
            memory=total,
            vcus=1
        )

    # @property
    # def default_components(self) -> Collection["component.EnvironmentComponentDescriptor"]:
    #     return [component.GPUComponent()]

    @contextmanager
    def _device_context(self):
        with self.cupy_device:
            yield

    @property
    def cupy_device(self):
        return cupy.cuda.Device(self.index)

    @lru_cache(None)
    def memory(self, kind: MemoryKind = None):
        return _GPUMemory(self, kind)

    def get_array_module(self):
        return cupy

    def __repr__(self):
        return "<CUDA {}>".format(self.index)


class _GPUArchitecture(Architecture):
    _devices: List[_GPUDevice]

    def __init__(self, name, id):
        super().__init__(name, id)
        devices = []
        if not cupy:
            self._devices = []
            return
        for device_id in range(2**16):
            cupy_device = cupy.cuda.Device(device_id)
            try:
                cupy_device.compute_capability
            except cupy.cuda.runtime.CUDARuntimeError:
                break
            assert cupy_device.id == device_id
            devices.append(self(cupy_device.id))
        self._devices = devices

    @property
    def devices(self):
        return self._devices

    def __call__(self, index, *args, **kwds):
        return _GPUDevice(self, index, *args, **kwds)


gpu = _GPUArchitecture("GPU", "gpu")
gpu.__doc__ = """The `~parla.device.Architecture` for CUDA GPUs.

>>> gpu(0)
"""
