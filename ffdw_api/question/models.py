from django.db import models

class Question(models.Model):
    question = models.CharField(max_length=255)
    answerone = models.CharField(max_length=255)
    answertwo = models.CharField(max_length=255)
    answerthree = models.CharField(max_length=255)
    answerfour = models.CharField(max_length=255)
    answerfive = models.CharField(max_length=255)
    answersix = models.CharField(max_length=255)
    answerseven = models.CharField(max_length=255)
    answereight = models.CharField(max_length=255)


    class Meta:
        ordering = ['question']
