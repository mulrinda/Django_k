from django.db import models
from django.conf import settings
from maps.models import Spot

class Show(models.Model):
    group_name = models.CharField(max_length=500)
    group_img = models.CharField(max_length=500)
    group_cnt = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='user_show', null=True)
   

class Showman(models.Model):
    showman_name = models.CharField(max_length=500)
    showman_img = models.CharField(max_length=500)
    show_cd = models.ForeignKey(Show, on_delete=models.CASCADE, null=True)
    showman_cnt = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='user_showman', null=True)
    spot_cd = models.ManyToManyField(Spot, related_name='spot_show', null=True)