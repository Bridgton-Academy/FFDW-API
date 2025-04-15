from django.db import models

class Question(models.Model):
    question = models.CharField(max_length=225, blank=True)
    answeronepoints = models.IntegerField(default=0)
    answeronevisable = models.BooleanField(default=False)
    answerone = models.CharField(max_length=225, blank=True)
    answertwopoints = models.IntegerField(default=0)
    answertwovisable = models.BooleanField(default=False)
    answertwo = models.CharField(max_length=225, blank=True)    
    answerthreepoints = models.IntegerField(default=0)
    answerthreevisable = models.BooleanField(default=False)
    answerthree = models.CharField(max_length=225, blank=True)  
    answerfourpoints = models.IntegerField(default=0)
    answerfourvisable = models.BooleanField(default=False)
    answerfour = models.CharField(max_length=225, blank=True)
    answerfivepoints = models.IntegerField(default=0)
    answerfivevisable = models.BooleanField(default=False)
    answerfive = models.CharField(max_length=225, blank=True)
    answersixpoints = models.IntegerField(default=0)
    answersixvisable = models.BooleanField(default=False)
    answersix = models.CharField(max_length=225, blank=True)
    answersevenpoints = models.IntegerField(default=0)
    answersevenvisable = models.BooleanField(default=False)
    answerseven = models.CharField(max_length=225, blank=True)
    answereightpoints = models.IntegerField(default=0)
    answereightvisable = models.BooleanField(default=False)
    answereight = models.CharField(max_length=225, blank=True)
    class Meta:
        ordering = ['question']


