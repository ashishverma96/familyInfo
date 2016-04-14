from __future__ import unicode_literals

from django.db import models

#from forms import BLOOD_GROUP_CHOICES
# Create your models here.

BLOOD_GROUP_CHOICES = (
    ('A+', 'A+'),
    ('A-', 'A-'),
    ('B+', 'B+'),
    ('B-', 'B-'),
    ('AB+','AB+'),
    ('AB-', 'AB-'),
    ('O+', 'O+'),
    ('O-', 'O-'),


)

class UserInfo(models.Model):
    name = models.CharField(max_length=100,blank = False)
    sirname = models.CharField(max_length=100,blank = False)
    phone_no = models.CharField(max_length=10)
    age = models.IntegerField()
    dateofbirth = models.CharField(max_length=100,blank=False)
    Address = models.CharField(max_length=100,blank=True)
    bloodgroup = models.CharField(choices=BLOOD_GROUP_CHOICES,max_length=10)
    image = models.ImageField(blank = True)

