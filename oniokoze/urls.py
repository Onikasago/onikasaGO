from django.urls import path

from . import views

app_name = 'oniokoze'
urlpatterns = [
    path('', views.IndexView.as_view(), name="index"),
    path('catch-list', views.CatchListView.as_view(), name="catch_list"),
    # path('catch-detail/<int:pk>/', views.CatchDetailView.as_view(), name="catch_detail"),
    path('catch-create', views.CatchCreateView.as_view(), name="catch_create"),
    path('spot-list', views.SpotListView.as_view(), name="spot_list"),
    path('recipe-list', views.RecipeListView.as_view(), name="recipe_list"),
    path('recipe-create', views.RecipeCreateView.as_view(), name="recipe_create"),
    path('recipe-detail/<int:pk>', views.RecipeDetailView.as_view(), name="recipe_detail"),
    path('recipe-delete/<int:pk>/', views.RecipeDeleteView.as_view(), name="recipe_delete"),
    path('recipe-update/<int:pk>/', views.RecipeUpdateView.as_view(), name="recipe_update"),
    path('trivia', views.TriviaView.as_view(), name="trivia"),
    path('mypage', views.MypageView.as_view(), name="mypage"),


]
