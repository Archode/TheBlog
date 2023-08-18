from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from ckeditor.fields import RichTextField

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse("home")

class Post(models.Model):
    title = models.CharField(max_length=200)
    # description = models.TextField()
    description = RichTextField(blank=True,null=True)
    image = models.ImageField(null=True,blank=True,upload_to='images/')
    author = models.ForeignKey(User, on_delete=models.CASCADE,null=True)
    category = models.CharField(max_length=255,default='uncategories',null=True,blank=True)

    def __str__(self):
        return self.title + ' | ' + str(self.author)
    
    def get_absolute_url(self):
        return reverse("home")
    