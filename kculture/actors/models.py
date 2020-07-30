from django.db import models
from django.conf import settings
from maps.models import Spot

class Drama(models.Model):
    drama_name = models.CharField(max_length=500)
    drama_img = models.CharField(max_length=500)   


class Actor(models.Model):
    actor_name = models.CharField(max_length=500)
    actor_img = models.CharField(max_length=500)
    actor_likenum = models.IntegerField(default=0)
    drama_cd = models.ForeignKey(Drama, on_delete=models.CASCADE, null=True)
    spot_cd = models.ManyToManyField(Spot, related_name='spot_actor', null=True)