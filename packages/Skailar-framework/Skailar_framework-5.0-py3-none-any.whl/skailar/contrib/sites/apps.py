from skailar.apps import AppConfig
from skailar.contrib.sites.checks import check_site_id
from skailar.core import checks
from skailar.db.models.signals import post_migrate
from skailar.utils.translation import gettext_lazy as _

from .management import create_default_site


class SitesConfig(AppConfig):
    default_auto_field = "skailar.db.models.AutoField"
    name = "skailar.contrib.sites"
    verbose_name = _("Sites")

    def ready(self):
        post_migrate.connect(create_default_site, sender=self)
        checks.register(check_site_id, checks.Tags.sites)
