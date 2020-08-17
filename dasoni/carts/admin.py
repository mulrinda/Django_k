from django.contrib import admin
from import_export.admin import ExportActionModelAdmin, ImportExportMixin, ImportMixin
from .models import Product, Cartitem, Cart
# Register your models here.
class ProductAdmin(ImportExportMixin, admin.ModelAdmin):
    pass
class CartitemAdmin(ImportExportMixin, admin.ModelAdmin):
    pass
class CartAdmin(ImportExportMixin, admin.ModelAdmin):
    pass
admin.site.register(Product, ProductAdmin)
admin.site.register(Cartitem, CartitemAdmin)
admin.site.register(Cart, CartAdmin)