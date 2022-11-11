from django.contrib import admin
from django.contrib.staticfiles.urls import static
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('oniokoze.urls')),
    path('accounts/', include('allauth.urls')),

]
