from django.db import models

class Question(models.Model):
    question = models.CharField(max_length=225, blank=True)
    answerone = models.CharField(max_length=225, blank=True)
    answertwo = models.CharField(max_length=225, blank=True)    
    answerthree = models.CharField(max_length=225, blank=True)  
    answerfour = models.CharField(max_length=225, blank=True)
    answerfive = models.CharField(max_length=225, blank=True)
    answersix = models.CharField(max_length=225, blank=True)
    answerseven = models.CharField(max_length=225, blank=True)
    answereight = models.CharField(max_length=225, blank=True)
    class Meta:
        ordering = ['question']


