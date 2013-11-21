from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from collections import namedtuple

#import model from the control app
from control.models import LivingRoom, DinningRoom, Kitchen, BedRoom1, BedRoom2, BedRoom3

#date and time for the record history:
import datetime
from django.utils import timezone


#--------------------------------------Models for History-------------------------------------#
# Create your models here.
class RecordLivingroom(models.Model):
    user = models.OneToOneField(User)
    
    pub_date = models.DateTimeField('date published')

    #define a dictionary here with date and time as key values, and temperature, On/Off as values
    Livingroom = namedtuple("Livingroom", ["date", "time"])
    
    

def create_record_livingroom(sender, instance, created, **kwargs):
    if created:
        RecordLivingroom.objects.create(user=instance)
post_save.connect(create_record_livingroom, sender=User)



class RecordDiningroom(models.Model):
    user = models.OneToOneField(User)

    #define a dictionary here with date and time as key values, and temperature, On/Off as values
    
    
def create_record_diningroom(sender, instance, created, **kwargs):
    if created:
        RecordDiningroom.objects.create(user=instance)
post_save.connect(create_record_diningroom, sender=User)



class RecordKitchen(models.Model):
    user = models.OneToOneField(User)

    #define a dictionary here with date and time as key values, and temperature, On/Off as values
    
    
def create_record_kitchen(sender, instance, created, **kwargs):
    if created:
        RecordKitchen.objects.create(user=instance)
post_save.connect(create_record_kitchen, sender=User)

