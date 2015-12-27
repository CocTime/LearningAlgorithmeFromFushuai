from django.db import models

# Create your models here.
class Armys(models.Model):
    name = models.CharField(max_length=20)
    level = models.IntegerField(max_length=20,default=1)
    numbers = models.IntegerField(max_length=200,default=0)
    time = models.IntegerField()
    cost_water = models.IntegerField(default=0)
    cost_black_water = models.IntegerField(default=0)

