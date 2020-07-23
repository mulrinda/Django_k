from django.db import models
from django.conf import settings
from maps.models import Spot

class Group(models.Model):
    group_name = models.CharField(max_length=500)
    group_img = models.CharField(max_length=500)
    spot_cd = models.ManyToManyField(Spot, related_name='spot_group')

class Singer(models.Model):
    singer_name = models.CharField(max_length=500)
    singer_img = models.CharField(max_length=500)
    group_cd = models.ForeignKey(Group, on_delete=models.CASCADE, null=True)
    spot_cd = models.ManyToManyField(Spot, related_name='spot_singer')