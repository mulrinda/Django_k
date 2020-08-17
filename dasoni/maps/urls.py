from django.urls import path
from . import views

app_name = 'maps'

urlpatterns = [
    path('', views.index, name='index'),
    path('stars/', views.stars, name='stars'),
    path('translate/', views.translate, name='translate'),
    path('weather/', views.weather, name='weather'),
    path('rankingtest/', views.rankingtest, name='rankingtest'),
    path('categorysing/', views.categorysing, name='categorysing'),
    path('categorydrama/', views.categorydrama, name='categorydrama'),
    path('categoryenter/', views.categoryenter, name='categoryenter'),
]
