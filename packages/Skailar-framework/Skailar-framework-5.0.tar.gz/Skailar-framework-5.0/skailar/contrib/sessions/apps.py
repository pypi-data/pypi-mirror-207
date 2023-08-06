from skailar.apps import AppConfig
from skailar.utils.translation import gettext_lazy as _


class SessionsConfig(AppConfig):
    name = "skailar.contrib.sessions"
    verbose_name = _("Sessions")
