from django.urls import path

from . import views

app_name = 'oniokoze'
urlpatterns = [
    path('', views.IndexView.as_view(), name="index"),
    path('catch-list', views.CatchListView.as_view(), name="catch_list"),
    path('catch-detail/<int:pk>/', views.CatchDetailView.as_view(), name="catch_detail"),
    # path('catch-create', views.CatchCreateView.as_view(), name="catch_create"),



]
