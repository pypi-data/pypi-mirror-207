from skailar.conf.urls.i18n import i18n_patterns
from skailar.urls import path
from skailar.utils.translation import gettext_lazy as _

urlpatterns = i18n_patterns(
    path(_("translated/"), lambda x: x, name="i18n_prefixed"),
)
