from django.db import models

# Creating inquiry models .
class Comment(models.Model):
    name = models.CharField(max_length=55)
    email= models.EmailField()
    phone =models.IntegerField()
    message =models.TextField()