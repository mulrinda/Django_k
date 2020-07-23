from django.db import models
from django.conf import settings
from maps.models import Spot

class Drama(models.Model):
    drama_name = models.CharField(max_length=500)
    drama_img = models.CharField(max_length=500)
    drama_cnt = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='user_drama', null=True)
   

class Actor(models.Model):
    actor_name = models.CharField(max_length=500)
    actor_img = models.CharField(max_length=500)
    drama_cd = models.ForeignKey(Drama, on_delete=models.CASCADE, null=True)
    showman_cnt = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='user_actor', null=True)
    spot_cd = models.ManyToManyField(Spot, related_name='spot_actor', null=True)