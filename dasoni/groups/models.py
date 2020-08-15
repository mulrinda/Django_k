from django.db import models
from django.conf import settings
from maps.models import Spot

class Star(models.Model):    
    star_sort = models.IntegerField()
    star_groupname = models.CharField(max_length=500)
    star_name = models.CharField(max_length=500)
    star_img = models.CharField(max_length=500)
    spot_cd = models.ManyToManyField(Spot, related_name='spot_actor', null=True)


class Visit(models.Model):
    visit_theme = models.IntegerField()
    visit_spot = models.IntegerField()
    visit_groupname = models.CharField(max_length=500)
    visit_name = models.CharField(max_length=500)
    visit_user = models.IntegerField()
    visit_date = models.DateTimeField(auto_now_add=True)
    visit_star_king = models.CharField(max_length=500)