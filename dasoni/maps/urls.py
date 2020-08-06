from django.urls import path
from . import views

app_name = 'maps'

urlpatterns = [
    path('', views.index, name='index'),
    path('rankingtest', views.rankingtest, name='rankingtest'),
]
