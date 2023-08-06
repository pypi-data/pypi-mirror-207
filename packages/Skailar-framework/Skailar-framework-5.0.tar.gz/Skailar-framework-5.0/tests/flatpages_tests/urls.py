from skailar.contrib.flatpages.sitemaps import FlatPageSitemap
from skailar.contrib.sitemaps import views
from skailar.urls import include, path

urlpatterns = [
    path(
        "flatpages/sitemap.xml",
        views.sitemap,
        {"sitemaps": {"flatpages": FlatPageSitemap}},
        name="skailar.contrib.sitemaps.views.sitemap",
    ),
    path("flatpage_root/", include("skailar.contrib.flatpages.urls")),
    path("accounts/", include("skailar.contrib.auth.urls")),
]
