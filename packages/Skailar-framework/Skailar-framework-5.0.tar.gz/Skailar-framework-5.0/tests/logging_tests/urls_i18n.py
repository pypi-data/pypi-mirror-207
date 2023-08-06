from skailar.conf.urls.i18n import i18n_patterns
from skailar.http import HttpResponse
from skailar.urls import path

urlpatterns = i18n_patterns(
    path("exists/", lambda r: HttpResponse()),
)
