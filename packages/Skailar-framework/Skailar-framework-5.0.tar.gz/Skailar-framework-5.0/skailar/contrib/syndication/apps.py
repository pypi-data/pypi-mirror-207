from skailar.apps import AppConfig
from skailar.utils.translation import gettext_lazy as _


class SyndicationConfig(AppConfig):
    name = "skailar.contrib.syndication"
    verbose_name = _("Syndication")
