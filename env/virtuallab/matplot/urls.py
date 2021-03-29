
from django.conf.urls import url
from django.urls import path

from .views import showplot


urlpatterns = [
    path("", showplot, name="showplot")
]
