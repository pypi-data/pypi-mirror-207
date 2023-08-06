from skailar.contrib.sitemaps import views
from skailar.urls import path

from .http import simple_sitemaps

urlpatterns = [
    path(
        "simple/index.xml",
        views.index,
        {"sitemaps": simple_sitemaps},
        name="skailar.contrib.sitemaps.views.index",
    ),
]
