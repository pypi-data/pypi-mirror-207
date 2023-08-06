from types import NoneType

from skailar.conf import settings
from skailar.core.checks import Error


def check_site_id(app_configs, **kwargs):
    if hasattr(settings, "SITE_ID") and not isinstance(
        settings.SITE_ID, (NoneType, int)
    ):
        return [
            Error("The SITE_ID setting must be an integer", id="sites.E101"),
        ]
    return []
