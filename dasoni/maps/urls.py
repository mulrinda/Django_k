from django.urls import path
from . import views

app_name = 'maps'

urlpatterns = [
    path('', views.index, name='index'),
    path('theme/', views.theme, name='theme'), # semi(0803) : theme mainpage
    
]
