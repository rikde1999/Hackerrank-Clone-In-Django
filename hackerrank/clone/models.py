from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Code(models.Model):
    id = models.AutoField(primary_key=True,unique = True)
    title = models.CharField(max_length=100)
    code = models.TextField(blank=True) 
    questions = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    completed = models.BooleanField(default=False)
    
    
    def __str__(self):
        return self.title

class User_details(models.Model):
    fk = models.ForeignKey(User,on_delete=models.CASCADE)
    id = models.AutoField(primary_key=True,unique = True)
    username = models.CharField(max_length=100)
    featured_image = models.ImageField(default = "default.png")
    email = models.EmailField(max_length=100)
    about_us = models.TextField(blank=True)
    def __str__(self):
        return self.username
    
    
class Solved(models.Model):
    
    fk = models.ForeignKey(User,on_delete=models.CASCADE)
    id = models.AutoField(primary_key=True,unique = True)
    code = models.ForeignKey(Code,on_delete=models.CASCADE)
    def __str__(self):
        return self.code.title