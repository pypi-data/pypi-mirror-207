from skailar.contrib.sitemaps import views
from skailar.urls import path

urlpatterns = [
    path(
        "sitemap-without-entries/sitemap.xml",
        views.sitemap,
        {"sitemaps": {}},
        name="skailar.contrib.sitemaps.views.sitemap",
    ),
]
