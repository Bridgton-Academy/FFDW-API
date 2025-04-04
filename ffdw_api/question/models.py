from django.db import models

class Question(models.Model):
    question = models.CharField(max_length=225, blank=True)
    answeronepoints = models.IntegerField(default=0)
    answerone = models.CharField(max_length=225, blank=True)
    answertwopoints = models.IntegerField(default=0)
    answertwo = models.CharField(max_length=225, blank=True)    
    answerthreepoints = models.IntegerField(default=0)
    answerthree = models.CharField(max_length=225, blank=True)  
    answerfourpoints = models.IntegerField(default=0)
    answerfour = models.CharField(max_length=225, blank=True)
    answerfivepoints = models.IntegerField(default=0)
    answerfive = models.CharField(max_length=225, blank=True)
    answersixpoints = models.IntegerField(default=0)
    answersix = models.CharField(max_length=225, blank=True)
    answersevenpoints = models.IntegerField(default=0)
    answerseven = models.CharField(max_length=225, blank=True)
    answereightpoints = models.IntegerField(default=0)
    answereight = models.CharField(max_length=225, blank=True)
    class Meta:
        ordering = ['question']


