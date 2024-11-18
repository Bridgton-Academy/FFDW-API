from django.db import models

class GameTeam(models.Model):
    game = models.CharField(max_length=225)
    team = models.CharField(max_length=225)   
    pts = models.IntegerField() 
    
    class Meta:
        ordering = ['game']