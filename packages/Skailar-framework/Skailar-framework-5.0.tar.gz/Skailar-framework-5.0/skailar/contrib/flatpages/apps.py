from skailar.apps import AppConfig
from skailar.utils.translation import gettext_lazy as _


class FlatPagesConfig(AppConfig):
    default_auto_field = "skailar.db.models.AutoField"
    name = "skailar.contrib.flatpages"
    verbose_name = _("Flat Pages")
