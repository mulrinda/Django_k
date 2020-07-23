from django.db import models
from django.conf import settings
from maps.models import Spot

class Show(models.Model):
    show_name = models.CharField(max_length=500)
    show_img = models.CharField(max_length=500)      
    
class Showman(models.Model):
    showman_name = models.CharField(max_length=500)
    showman_img = models.CharField(max_length=500)
    showman_likenum = models.IntegerField()
    show_cd = models.ForeignKey(Show, on_delete=models.CASCADE, null=True)
    spot_cd = models.ManyToManyField(Spot, related_name='spot_show', null=True)