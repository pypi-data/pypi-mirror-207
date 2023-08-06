from skailar.apps import apps as skailar_apps
from skailar.contrib.sitemaps import Sitemap
from skailar.core.exceptions import ImproperlyConfigured


class FlatPageSitemap(Sitemap):
    def items(self):
        if not skailar_apps.is_installed("skailar.contrib.sites"):
            raise ImproperlyConfigured(
                "FlatPageSitemap requires skailar.contrib.sites, which isn't installed."
            )
        Site = skailar_apps.get_model("sites.Site")
        current_site = Site.objects.get_current()
        return current_site.flatpage_set.filter(registration_required=False)
