from django.db import models
from django.conf import settings

class Spot(models.Model):
    spot_name = models.CharField(max_length=500)
    spot_address = models.CharField(max_length=500)
    lat = models.FloatField()
    lon = models.FloatField()
    spot_info = models.CharField(max_length=500)
    spot_img = models.CharField(max_length=500)
    
class Theme(models.Model):
    theme_name = models.CharField(max_length=500)
    star_img = models.CharField(max_length=500)
    spot_cd = models.ForeignKey(Spot, on_delete=models.CASCADE, null=True)
    theme_img = models.CharField(max_length=500)