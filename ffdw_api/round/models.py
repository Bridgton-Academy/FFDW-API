from django.db import models

class Round(models.Model):
    question = models.CharField(max_length=255)
    pts_revealed = models.CharField(max_length=255)
    questions_revealed = models.CharField(max_length=255)


    class Meta:
        ordering = ['question']