from django.urls import path
from . import views

app_name = 'tothers'

urlpatterns = [
    path('',views.index,name="index"),
    path('tourtip', views.tourtip, name='tourtip'),
    path('stamp', views.stamp, name='stamp'),
    path('theme/<str:cont>/<str:lang>/', views.theme, name='theme'), # semi(0803) : theme개별페이지 테스트중

]
