from skailar.urls import include, path

urlpatterns = [
    path("flatpage", include("skailar.contrib.flatpages.urls")),
]
