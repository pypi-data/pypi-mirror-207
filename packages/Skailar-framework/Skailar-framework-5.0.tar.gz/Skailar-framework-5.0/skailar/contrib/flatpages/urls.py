from skailar.contrib.flatpages import views
from skailar.urls import path

urlpatterns = [
    path("<path:url>", views.flatpage, name="skailar.contrib.flatpages.views.flatpage"),
]
