import email
from threading import get_ident
from turtle import degrees
from unicodedata import name
from django.db import models

# Create your models here.
class Profile(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    phone = models.CharField(max_length=200,blank=True, null=True)
    portfolio_site = models.CharField(max_length=200,blank=True, null=True)
    linkedin = models.CharField(max_length=200,blank=True,null=True)
    github = models.CharField(max_length=200,blank=True,null=True)
    twitter = models.CharField(max_length=200,blank=True,null=True)
    summary = models.TextField(max_length=2000)
    education = models.CharField(max_length=200)
    skills = models.TextField(max_length=2000)
    work_experience = models.TextField(max_length=2000, null=True, blank=True)
    previous_projects = models.TextField(max_length=2000, null=True, blank=True)
    
    
    
    