
from django.conf.urls import url
from django.urls import path

from .views import view_simple_pendulum

urlpatterns = [
    path("",view_simple_pendulum,name="simple_pendulum_view")
]
