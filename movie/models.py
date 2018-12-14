from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField

class Customer(models.Model):
    
    GENDER_CHOICES = (
   ('M', 'Male'),
   ('F', 'Female')
   )
    STATES=(
        
        ('Rajasthan','Rajashan'),
        ('Gujarat','Gujarat'),
        ('Maharashtra','Maharashtra'),
        ('UttarPradesh','UttarPradesh'),
        ('Karnataka','Karnataka'),
        ('Delhi','Delhi'),
        )
    
    CITIES=(
        
        ('Ahmedabad','Ahmedabad'),
        ('Vadodara','Vadodara'),
        ('Jaipur','Jaipur'),
        ('Udaipur','Udaipur'),
        ('Pune','Pune'),
        ('Bombay','Bombay'),
        ('Noida','Noida'),
        ('Banglore','Banglore')
        )
    user=models.OneToOneField(User,related_name='customer_profile',on_delete=models.PROTECT)
    contact=PhoneNumberField()
    gender = models.CharField(choices=GENDER_CHOICES,max_length=1)
    states=models.CharField(choices=STATES,max_length=20)
    city=models.CharField(choices=CITIES,max_length=20)
    def __str__(self):
        return self.user.username 

   
        

    