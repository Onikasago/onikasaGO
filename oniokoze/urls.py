from django.urls import path

from . import views

app_name = 'oniokoze'
urlpatterns = [
    path('', views.IndexView.as_view(), name="index"),
    path('catch-list', views.CatchListView.as_view(), name="catch_list"),
    # path('catch-detail/<int:pk>/', views.CatchDetailView.as_view(), name="catch_detail"),
    path('catch-create', views.CatchCreateView.as_view(), name="catch_create"),
    path('fishname-create', views.FishnameCreateView.as_view(), name="fishname_create"),
    path('spot-list', views.SpotListView.as_view(), name="spot_list"),
    path('recipe-list', views.RecipeListView.as_view(), name="recipe_list"),
    path('recipe-create', views.RecipeCreateView.as_view(), name="recipe_create"),
    path('trivia', views.TriviaView.as_view(), name="trivia"),
    path('mypage', views.MypageView.as_view(), name="mypage"),


    path('tool/', views.ToolView.as_view(), name="tool"),
    path('manners/', views.MannersView.as_view(), name="manners"),
    path('fishing_method/', views.Fishing_methodView.as_view(), name="fishing_method"),
    path('bait/', views.BaitView.as_view(), name="bait"),
    path('dangerous_creature/', views.Dangerous_creatureView.as_view(), name="dangerous_creature"),
    path('place/', views.PlaceView.as_view(), name="place"),
]
