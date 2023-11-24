from django.db import models

class Picture(models.Model):
    name = models.CharField(max_length=40)
    production_year = models.IntegerField()
    price = models.CharField(max_length=40)