from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Driver(models.Model):
    # user = models.OneToOneField(User,on_delete=models.CASCADE,blank=False,null=False)
    userId = models.IntegerField(null=True,blank=False,unique=True)
    phone = models.CharField(max_length=10,null=True,blank=False)
    regNumber = models.CharField(max_length=50)
    carModel = models.CharField(max_length=100)
    type = models.CharField(max_length=100,choices=(('Mourtuary','Mourtuary'),('Basic','Basic'),('Advance','Advance')))
    evoc = models.FileField()
    liscance = models.FileField()
    aadhar = models.FileField()
    busy = models.BooleanField(default=False)

    def __str__(self):
        return self.regNumber


class FleatOwner(models.Model):
    userId = models.IntegerField(null=True,blank=False,unique=True)
    companyName = models.CharField(max_length=300,null=True,blank=True)
    phone = models.CharField(max_length=10,null=True,blank=False)


'''
class DriverOfFleat():
    user = models.OneToOneField(User,on_delete=models.CASCADE,null=True,blank=False)
    userId = models.IntegerField(null=True,blank=False)
    '''

class Ambulance(models.Model):
    fleatId = models.IntegerField(null=True,blank=False)
    regNumber = models.CharField(max_length=50)
    carModel = models.CharField(max_length=100)
    type = models.CharField(max_length=100,choices=(('Mourtuary','Mourtuary'),('Basic','Basic'),('Advance','Advance')))
    evoc = models.FileField()
    liscance = models.FileField()
    aadhar = models.FileField()
    busy = models.BooleanField(default=False)
