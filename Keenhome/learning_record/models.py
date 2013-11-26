from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save


#import model from the control app
from control.models import LivingRoom, DinningRoom, Kitchen, BedRoom1, BedRoom2, BedRoom3

#date and time for the record history:
import datetime
from django.utils import timezone


#----------------------------------Models for History--------------------------------#
# Create your models here.
class RecordLivingRoom(models.Model):
    room = models.ForeignKey(LivingRoom)
    
    datetime = models.DateTimeField('recordtime', auto_now=True)
    
    TURN_ON_OFF = (
        ('ON', 'On'),
        ('OFF', 'Off'),
    )
    
    TEMP = (
        ('HIGH', 'High'),
        ('MEDIUM', 'Medium'),
        ('LOW', 'Low'),
    )
    
    on_off = models.CharField(max_length=2, choices=TURN_ON_OFF)
    temp = models.CharField(max_length=2, choices=TEMP)
    
#signal function: if a user is created, add control livingroom to the user    
def record_livingroom(sender, instance, created, **kwargs):
    #the object which is saved can be accessed with **kwargs
    livingroom = instance
    record = RecordLivingRoom(room=instance, 
                              on_off=livingroom.on_off, 
                              temp=livingroom.temp)
    record.save() 
#    if created:
#        RecordLivingRoom.objects.create(user=instance)
post_save.connect(record_livingroom, sender=LivingRoom)




class RecordDinningRoom(models.Model):
    room = models.ForeignKey(DinningRoom)
    
    datetime = models.DateTimeField('recordtime', auto_now=True)
    
    TURN_ON_OFF = (
        ('ON', 'On'),
        ('OFF', 'Off'),
    )
    
    TEMP = (
        ('HIGH', 'High'),
        ('MEDIUM', 'Medium'),
        ('LOW', 'Low'),
    )
    
    on_off = models.CharField(max_length=2, choices=TURN_ON_OFF)
    temp = models.CharField(max_length=2, choices=TEMP)
    
#signal function: if a user is created, add control livingroom to the user    
def record_dinningroom(sender, instance, created, **kwargs):
    #the object which is saved can be accessed with **kwargs
    dinningroom = instance
    record = RecordDinningRoom(room=instance,
                               on_off=dinningroom.on_off, 
                               temp=dinningroom.temp)
    record.save() 
#    if created:
#        RecordLivingRoom.objects.create(user=instance)
post_save.connect(record_dinningroom, sender=DinningRoom)
    
    


class RecordKitchen(models.Model):
    room = models.ForeignKey(Kitchen)
    
    datetime = models.DateTimeField('recordtime', auto_now=True)
    
    TURN_ON_OFF = (
        ('ON', 'On'),
        ('OFF', 'Off'),
    )
    
    TEMP = (
        ('HIGH', 'High'),
        ('MEDIUM', 'Medium'),
        ('LOW', 'Low'),
    )
    
    on_off = models.CharField(max_length=2, choices=TURN_ON_OFF)
    temp = models.CharField(max_length=2, choices=TEMP)
    
#signal function: if a user is created, add control livingroom to the user    
def record_kitchen(sender, instance, created, **kwargs):
    #the object which is saved can be accessed with **kwargs
    kitchen = instance
    record = RecordKitchen(room=instance,
                           on_off=kitchen.on_off, 
                           temp=kitchen.temp)
    record.save() 
#    if created:
#        RecordLivingRoom.objects.create(user=instance)
post_save.connect(record_kitchen, sender=Kitchen)
    




class RecordBedRoom1(models.Model):
    room = models.ForeignKey(BedRoom1)
    
    datetime = models.DateTimeField('recordtime', auto_now=True)
    
    TURN_ON_OFF = (
        ('ON', 'On'),
        ('OFF', 'Off'),
    )
    
    TEMP = (
        ('HIGH', 'High'),
        ('MEDIUM', 'Medium'),
        ('LOW', 'Low'),
    )
    
    on_off = models.CharField(max_length=2, choices=TURN_ON_OFF)
    temp = models.CharField(max_length=2, choices=TEMP)
    
#signal function: if a user is created, add control livingroom to the user    
def record_bedroom1(sender, instance, created, **kwargs):
    #the object which is saved can be accessed with **kwargs
    bedroom1 = instance
    record = RecordBedRoom1(room=instance,
                            on_off=bedroom1.on_off,
                            temp=bedroom1.temp)
    record.save() 
#    if created:
#        RecordLivingRoom.objects.create(user=instance)
post_save.connect(record_bedroom1, sender=BedRoom1)
    



class RecordBedRoom2(models.Model):
    room = models.ForeignKey(BedRoom2)
    
    datetime = models.DateTimeField('recordtime', auto_now=True)
    
    TURN_ON_OFF = (
        ('ON', 'On'),
        ('OFF', 'Off'),
    )
    
    TEMP = (
        ('HIGH', 'High'),
        ('MEDIUM', 'Medium'),
        ('LOW', 'Low'),
    )
    
    on_off = models.CharField(max_length=2, choices=TURN_ON_OFF)
    temp = models.CharField(max_length=2, choices=TEMP)
    
#signal function: if a user is created, add control livingroom to the user    
def record_bedroom2(sender, instance, created, **kwargs):
    #the object which is saved can be accessed with **kwargs
    bedroom2 = instance
    record = RecordBedRoom2(room=instance,
                            on_off=bedroom2.on_off,
                            temp=bedroom2.temp)
    record.save() 
#    if created:
#        RecordLivingRoom.objects.create(user=instance)
post_save.connect(record_bedroom2, sender=BedRoom2) 
    



class RecordBedRoom3(models.Model):
    room = models.ForeignKey(BedRoom3)
    
    datetime = models.DateTimeField('recordtime', auto_now=True)
    
    TURN_ON_OFF = (
        ('ON', 'On'),
        ('OFF', 'Off'),
    )
    
    TEMP = (
        ('HIGH', 'High'),
        ('MEDIUM', 'Medium'),
        ('LOW', 'Low'),
    )
    
    on_off = models.CharField(max_length=2, choices=TURN_ON_OFF)
    temp = models.CharField(max_length=2, choices=TEMP)
    
#signal function: if a user is created, add control livingroom to the user    
def record_bedroom3(sender, instance, created, **kwargs):
    #the object which is saved can be accessed with **kwargs
    bedroom3 = instance
    record = RecordBedRoom3(room=instance,
                            on_off=bedroom3.on_off,
                            temp=bedroom3.temp)
    record.save() 
#    if created:
#        RecordLivingRoom.objects.create(user=instance)
post_save.connect(record_bedroom3, sender=BedRoom3)








    
