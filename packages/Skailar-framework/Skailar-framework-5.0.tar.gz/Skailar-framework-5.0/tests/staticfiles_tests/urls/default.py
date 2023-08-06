from skailar.contrib.staticfiles import views
from skailar.urls import re_path

urlpatterns = [
    re_path("^static/(?P<path>.*)$", views.serve),
]
