from django.urls import path
from . import views

app_name = 'maptests'

urlpatterns = [
    path('',views.index,name='index'),
]
