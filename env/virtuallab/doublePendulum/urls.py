
from django.conf.urls import url
from django.urls import path

from .views import view_double_pendulum

urlpatterns = [
    path("",view_double_pendulum,name="double_pendulum_view")
]
