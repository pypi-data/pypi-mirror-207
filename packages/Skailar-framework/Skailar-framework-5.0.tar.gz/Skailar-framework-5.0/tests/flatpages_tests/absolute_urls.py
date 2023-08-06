from skailar.contrib.flatpages import views
from skailar.urls import path

urlpatterns = [
    path("flatpage/", views.flatpage, {"url": "/hardcoded/"}),
]
