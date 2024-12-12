from django.db import models

class Game(models.Model):
    teamone = models.CharField(max_length=225)
    teamtwo = models.CharField(max_length=225)    
    
    class Meta:
        ordering = ['teamone']