from skailar.apps import AppConfig
from skailar.utils.translation import gettext_lazy as _


class AdminDocsConfig(AppConfig):
    name = "skailar.contrib.admindocs"
    verbose_name = _("Administrative Documentation")
