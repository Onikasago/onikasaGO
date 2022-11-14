from django.urls import path

from . import views

app_name = 'oniokoze'
urlpatterns = [
    path('', views.IndexView.as_view(), name="index"),
    path('catch-list/', views.CatchListView.as_view(), name="catch_list"),
    path('catch-create/', views.CatchCreateView.as_view(), name="catch_create"),
    # path('spot-list/', views.SpotListView.as_view(), name="spot_list"),



]
