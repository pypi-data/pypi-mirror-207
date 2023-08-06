from skailar.apps import AppConfig
from skailar.core import serializers
from skailar.utils.translation import gettext_lazy as _


class GISConfig(AppConfig):
    default_auto_field = "skailar.db.models.AutoField"
    name = "skailar.contrib.gis"
    verbose_name = _("GIS")

    def ready(self):
        serializers.BUILTIN_SERIALIZERS.setdefault(
            "geojson", "skailar.contrib.gis.serializers.geojson"
        )
