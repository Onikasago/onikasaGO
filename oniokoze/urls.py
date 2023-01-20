from django.urls import path

from . import views

app_name = 'oniokoze'
urlpatterns = [
    path('', views.IndexView.as_view(), name="index"),
    path('catch-list', views.CatchListView.as_view(), name="catch_list"),
    path('catch-create', views.CatchCreateView.as_view(), name="catch_create"),
    path('catch-detail/<int:pk>/', views.CatchDetailView.as_view(), name="catch_detail"),
    path('catch-update/<int:pk>/', views.CatchUpdateView.as_view(), name="catch_update"),
    path('catch-delete/<int:pk>/', views.CatchDeleteView.as_view(), name="catch_delete"),
    path('fishname-create', views.FishnameCreateView.as_view(), name="fishname_create"),
    path('spot-list', views.SpotListView.as_view(), name="spot_list"),
    path('recipe-list', views.RecipeListView.as_view(), name="recipe_list"),
    path('recipe-create', views.RecipeCreateView.as_view(), name="recipe_create"),
    path('trivia', views.TriviaView.as_view(), name="trivia"),
    path('mypage', views.MypageView.as_view(), name="mypage"),


]
