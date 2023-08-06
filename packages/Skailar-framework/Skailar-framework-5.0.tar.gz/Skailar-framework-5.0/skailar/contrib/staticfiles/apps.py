from skailar.apps import AppConfig
from skailar.contrib.staticfiles.checks import check_finders
from skailar.core import checks
from skailar.utils.translation import gettext_lazy as _


class StaticFilesConfig(AppConfig):
    name = "skailar.contrib.staticfiles"
    verbose_name = _("Static Files")
    ignore_patterns = ["CVS", ".*", "*~"]

    def ready(self):
        checks.register(check_finders, checks.Tags.staticfiles)
