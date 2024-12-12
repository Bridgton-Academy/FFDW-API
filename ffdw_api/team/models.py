from django.db import models

class Team(models.Model):
    name = models.CharField(max_length=225, blank=False)    
    users = models.CharField(max_length=225, blank=False)

    class Meta:
        ordering = ['name']