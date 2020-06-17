from django.db import models
from django.contrib.auth.models import User

class Country(models.Model):
    name = models.CharField(verbose_name="Country",max_length=100)
    def __str__(self):
        return self.name

class State(models.Model):
    country = models.ForeignKey(Country,on_delete=models.CASCADE)
    name = models.CharField(verbose_name="State",max_length=100)

    def __str__(self):
        return self.name

class City(models.Model):
    State = models.ForeignKey(State,on_delete=models.CASCADE)
    name = models.CharField(verbose_name="City",max_length=70)

    def __str__(self):
        return self.name

class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    address = models.TextField(verbose_name="Address",max_length=400)
    country = models.ForeignKey(Country,on_delete=models.CASCADE,verbose_name="Country")
    state = models.ForeignKey(State,on_delete=models.CASCADE,verbose_name="State")
    city = models.ForeignKey(City,on_delete=models.CASCADE,verbose_name="City")
    dob = models.DateField(verbose_name="Date Of Birth")
    contact = models.CharField(verbose_name="Contact",max_length=20)
    profile_pic = models.ImageField(verbose_name="Profile Picture",upload_to="myprofile/%d%m%y")

    def __str__(self):
        self.user.username
