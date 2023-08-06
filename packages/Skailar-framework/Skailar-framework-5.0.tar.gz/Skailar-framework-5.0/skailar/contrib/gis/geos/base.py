from skailar.contrib.gis.geos.error import GEOSException
from skailar.contrib.gis.ptr import CPointerBase


class GEOSBase(CPointerBase):
    null_ptr_exception_class = GEOSException
