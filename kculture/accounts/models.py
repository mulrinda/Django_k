from django.db import models
from django.conf import settings

# Create your models here.

class Like(models.Model):
    like_singer = models.IntegerField()
    like_group = models.IntegerField()
    like_actor = models.IntegerField()
    like_showmane = models.IntegerField()
    user_cd = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)