from django.db import models

# Creating inquiry models .
class Comment(models.Model):
    name = models.CharField(max_length=55)
    phone =models.IntegerField()
    message =models.CharField(max_length=208, default='')
    