from django.db import models

# Create your models here.
class Tweet(models.Model):
    content=models.CharField(max_length=280)
    image=models.FileField(upload_to='images/',blank=True,null=True)