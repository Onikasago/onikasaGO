from django.urls import path

from . import views

app_name = 'oniokoze'
urlpatterns = [
    path('', views.IndexView.as_view(), name="index"),
    path('oniokoze-create', views.OniokozeCreateView.as_view(), name = "oniokoze_create"),

]
