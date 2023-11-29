from django.db import models
import random

# Create your models here.
class Tweet(models.Model):
    content=models.CharField(max_length=280)
    image=models.FileField(upload_to='images/',blank=True,null=True)
    # likes=models.IntegerField()

    class Meta:
        ordering = ['-id']
        
    def serialize(self):
        return {
            "id":self.id,
            "content":self.content,
            "likes":random.randint(0,12345)
        }