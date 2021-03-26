from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static

from django.conf import settings

from .views import home_page

urlpatterns = [
    path('',home_page, name="home"),
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns = urlpatterns + \
        static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns = urlpatterns + \
        static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)