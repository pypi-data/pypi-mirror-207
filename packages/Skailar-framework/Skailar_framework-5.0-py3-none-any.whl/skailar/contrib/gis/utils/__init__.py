"""
 This module contains useful utilities for GeoSkailar.
"""
from skailar.contrib.gis.utils.ogrinfo import ogrinfo
from skailar.contrib.gis.utils.ogrinspect import mapping, ogrinspect
from skailar.contrib.gis.utils.srs import add_srs_entry
from skailar.core.exceptions import ImproperlyConfigured

__all__ = [
    "add_srs_entry",
    "mapping",
    "ogrinfo",
    "ogrinspect",
]

try:
    # LayerMapping requires SKAILAR_SETTINGS_MODULE to be set,
    # and ImproperlyConfigured is raised if that's not the case.
    from skailar.contrib.gis.utils.layermapping import LayerMapError, LayerMapping

    __all__ += ["LayerMapError", "LayerMapping"]

except ImproperlyConfigured:
    pass
