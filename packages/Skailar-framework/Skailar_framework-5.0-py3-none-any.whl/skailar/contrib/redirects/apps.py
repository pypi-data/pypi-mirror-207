from skailar.apps import AppConfig
from skailar.utils.translation import gettext_lazy as _


class RedirectsConfig(AppConfig):
    default_auto_field = "skailar.db.models.AutoField"
    name = "skailar.contrib.redirects"
    verbose_name = _("Redirects")
