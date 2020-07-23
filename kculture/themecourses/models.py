from django.db import models
from maps.models import Spot

class Theme(models.Model):
    theme_name = models.CharField(max_length=500)
    actor_img = models.CharField(max_length=500)
    spot_cd = models.ForeignKey(Spot, on_delete=models.CASCADE)