from django.db import models

class Spot(models.Model):
    spot_name = models.CharField(max_length=500)
    spot_address = models.CharField(max_length=500)
    lat = models.FloatField()
    lon = models.FloatField()
    spot_info = models.CharField(max_length=500)
 