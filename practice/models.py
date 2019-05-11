from django.db import models

# Create your models here.


class Task(models.Model):
    theme = models.CharField(max_length=50)
    num = models.BigIntegerField()
    question = models.TextField()
    answer = models.CharField(max_length=20)

    def __str__(self):
        return self.question
