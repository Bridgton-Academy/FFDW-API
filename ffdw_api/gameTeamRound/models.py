from django.db import models

class GameTeamRound(models.Model):
    gameTeam = models.CharField(max_length=225)
    round = models.CharField(max_length=225)   
    pts = models.IntegerField() 
    strikes = models.IntegerField()
    
    class Meta:
        ordering = ['gameTeam']