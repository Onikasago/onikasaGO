from django.urls import path
from . import views
from .views import *

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
    path('spot-create', views.SpotCreateView.as_view(), name="spot_create"),
    path('spot-detail/<int:pk>/', views.SpotDetailView.as_view(), name="spot_detail"),
    path('spot-update/<int:pk>', views.SpotUpdateView.as_view(), name="spot_update"),
    path('spot-delete/<int:pk>/', views.SpotDeleteView.as_view(), name="spot_delete"),
    path('like_for_post/', views.like_for_post, name='like_for_post'),
    path('recipe-list', views.RecipeListView.as_view(), name="recipe_list"),
    path('recipe-create', views.RecipeCreateView.as_view(), name="recipe_create"),
    path('recipe-detail/<int:pk>/', views.RecipeDetailView.as_view(), name="recipe_detail"),
    path('recipe-update/<int:pk>/', views.RecipeUpdateView.as_view(), name="recipe_update"),
    path('recipe-delete/<int:pk>/', views.RecipeDeleteView.as_view(), name="recipe_delete"),
    path('trivia/', views.TriviaView.as_view(), name="trivia"),
    path('mypage/', views.MypageView.as_view(), name="mypage"),
    path('process-form', processForm, name='process-form'),
    path('get-prefecture', getPrefecture, name='get-prefecture'),

]
