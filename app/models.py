from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class register(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True,blank=True)
    name = models.CharField(max_length=100,null=True,blank=True)
    username = models.CharField(max_length=100,null=True,blank=True)
    email = models.EmailField(null=True,blank=True)
    password = models.CharField(max_length=100,null=True,blank=True)

    
class Report(models.Model):
    issue_faced = models.CharField(max_length=100)
    device_caused = models.CharField(max_length=100)
    screenshot = models.ImageField(upload_to='screenshots/', blank=True)
    other_details = models.TextField(blank=True)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Report #{self.pk}"
    
class Solution(models.Model):
    image = models.ImageField(upload_to='media/',null=True)
    problem = models.CharField(max_length=255,null=True)
    chances = models.CharField(max_length=255, null=True)
    precautions = models.TextField(null=True)
    solutions = models.TextField(null=True)
    advisor = models.CharField(max_length=255, null=True)

    def __str__(self):
        return self.problem