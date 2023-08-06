from skailar.apps import AppConfig
from skailar.utils.translation import gettext_lazy as _


class HumanizeConfig(AppConfig):
    name = "skailar.contrib.humanize"
    verbose_name = _("Humanize")
