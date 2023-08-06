from skailar.http import HttpResponse
from skailar.urls import path

urlpatterns = [
    path("", lambda request: HttpResponse("root is here")),
]
