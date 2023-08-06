from skailar.apps import AppConfig
from skailar.utils.translation import gettext_lazy as _


class SiteMapsConfig(AppConfig):
    default_auto_field = "skailar.db.models.AutoField"
    name = "skailar.contrib.sitemaps"
    verbose_name = _("Site Maps")
