from django.contrib import admin
from django.contrib.staticfiles.urls import static
from django.urls import path, include
from . import settings_dev, settings_common
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('oniokoze.urls')),
    path('accounts/',include('allauth.urls')),
]
urlpatterns += static(settings_dev.MEDIA_URL, document_root=settings_dev.MEDIA_ROOT)
