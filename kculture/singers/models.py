from django.db import models
from django.conf import settings
from maps.models import Spot

class Group(models.Model):
    group_name = models.CharField(max_length=500)
    group_img = models.CharField(max_length=500)
    group_cnt = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='user_group', null=True)
    spot_cd = models.ManyToManyField(Spot, related_name='spot_group')

class Singer(models.Model):
    singer_name = models.CharField(max_length=500)
    singer_img = models.CharField(max_length=500)
    group_cd = models.ForeignKey(Group, on_delete=models.CASCADE, null=True)
    singer_cnt = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='user_singer', null=True)
    spot_cd = models.ManyToManyField(Spot, related_name='spot_singer')