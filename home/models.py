import email
from email import message
from django.db import models

# Create your models here.

class Contact(models.Model):
    fullname=models.CharField(max_length=1000)
    email= models.EmailField()
    phone=models.IntegerField()
    message=models.CharField(max_length=10000)
    
    
    def __str__(self):
        return self.email
    
class Subscribtion (models.Model):
    email= models.EmailField()
    
    def __str__(self):
        return self.email
    
class Post(models.Model):
    post_image = models.ImageField(upload_to='images/',null=True,max_length=250)
    post_title =models.CharField(max_length=10000)
    post_content =models.CharField(max_length=10000)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.post_title
    
    def snippet(self):
        return self.post_content[:200] + ".... "