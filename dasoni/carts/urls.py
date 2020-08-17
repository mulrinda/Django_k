from django.urls import path
from . import views

app_name = 'carts'

urlpatterns = [
<<<<<<< HEAD
=======
    path('goods/', views.goods, name='goods'),
    path('add/<int:product_id>/', views.add_cart, name='add_cart'),
    path('', views.cart_detail, name='cart_detail'),

    
>>>>>>> 17485aaae7c4ca66edc7c3aeebd9b209f3d531f0
  
]
