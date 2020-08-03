from django.urls import path
from . import views

app_name = 'tothers'

urlpatterns = [
     path('test/', views.test, name='test'), # semi(0803) : theme개별페이지 테스트중
]
