
from django.conf.urls import url
from django.urls import path

from .views import showplot,showanimePlot


urlpatterns = [
    path("", showplot, name="showplot"),
    path("anime/", showanimePlot, name="showanimeplot")
]
