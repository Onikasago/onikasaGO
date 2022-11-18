from django.urls import path

from . import views

app_name = 'oniokoze'
urlpatterns = [
    path('', views.IndexView.as_view(), name="index"),
    path('catch-list', views.CatchListView.as_view(), name="catch_list"),
    path('catch-create', views.CatchCreateView.as_view(), name="catch_create"),
    path('fishname-create', views.FishnameCreateView.as_view(), name="fishname_create"),
    path('mypage', views.MypageView.as_view(), name="mypage"),

]
