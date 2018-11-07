from django.db import models

# Create your models here.

class Prescriber(models.Model):
    name = models.CharField(max_length=100, blank=True, default='')
    street = models.CharField(max_length=100, blank=True, default='') 
    city = models.CharField(max_length=100, blank=True, default='')
    province = models.CharField(max_length=100, blank=True, default='')

    class Meta:
        ordering = ('province',)