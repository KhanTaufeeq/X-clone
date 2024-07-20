from django.db import models
from cloudinary.models import CloudinaryField

# Create your models here.

class Tweet(models.Model):

    name = models.CharField('Name', max_length=20, blank=False, null=False) 

    body = models.TextField('Body', blank=False, null=False, max_length=500) 

    like_count = models.PositiveIntegerField('Like_Count', blank=True, null=True, default=0) 

    created_at = models.DateTimeField('Created At', blank=False, null=False, auto_now_add=True) 

    updated_at = models.DateTimeField('Updated At', blank=False, null=False, auto_now=True) 

    image = CloudinaryField('Image', blank=True, null=True) 

    def __str__(self):
        return self.name 
