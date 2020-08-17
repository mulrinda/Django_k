from django.db import models

# Create your models here.

class Product(models.Model):
    product_name = models.CharField(max_length=500)
    product_sort = models.CharField(max_length=500)
    product_price = models.IntegerField()

    class Meta:
        db_table = 'Product'

class Cart(models.Model):
    cart_id = models.CharField(max_length=500, blank=True)
    cart_date = models.DateField(auto_now_add=True)

    class Meta:
        db_table = 'Cart'
        ordering = ['cart_date']

def _str_(self):
    return self.cart_id
    # default 문자열일경우 객체를 알아보기 어렵기 때문에 정의해주는 것이 좋다.


class Cartitem(models.Model):
    quantity = models.IntegerField()
    active = models.BooleanField(default=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    cart =  models.ForeignKey(Cart, on_delete=models.CASCADE)

    class Meta:
        db_table = 'CartItem'
    
    def sub_total(self):            
        return self.product.product_price * self.quantity

    def _str_(self):
        return self.product

