from skailar.conf.urls.i18n import i18n_patterns
from skailar.http import HttpResponse, StreamingHttpResponse
from skailar.urls import path
from skailar.utils.translation import gettext_lazy as _

urlpatterns = i18n_patterns(
    path("simple/", lambda r: HttpResponse()),
    path("streaming/", lambda r: StreamingHttpResponse([_("Yes"), "/", _("No")])),
)
