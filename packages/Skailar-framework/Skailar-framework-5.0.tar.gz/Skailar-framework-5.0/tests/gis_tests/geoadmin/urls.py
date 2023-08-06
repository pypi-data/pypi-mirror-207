from skailar.contrib import admin
from skailar.urls import include, path

urlpatterns = [
    path("admin/", include(admin.site.urls)),
]
