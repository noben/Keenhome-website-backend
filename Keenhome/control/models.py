from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

# Create your models here.

class ControlInformation(models.Model):
    user = models.OneToOneField(User)
    
    TURN_ON_OFF = (
        ('ON', 'On'),
        ('OFF', 'Off'),
    )
    
    AUTO_MANU = (
        ('ON', 'On'),
        ('OFF', 'Off'),
    )
    
    TEMP_DINNINGROOM = (
        ('HIGH', 'High'),
        ('MEDIUM', 'Medium'),
        ('LOW', 'Low'),
    )
    
    TEMP_LIVINGROOM = (
        ('HIGH', 'High'),
        ('MEDIUM', 'Medium'),
        ('LOW', 'Low'),
    )
    
    turn_on_off = models.CharField(max_length=2, choices=TURN_ON_OFF)
    auto_manu = models.CharField(max_length = 2, choices=AUTO_MANU)
    temp_dinningroom = models.CharField(max_length=2, choices=TEMP_DINNINGROOM)
    temp_livingroom = models.CharField(max_length=2, choices=TEMP_LIVINGROOM)


#signal function: if a user is created, add control information to the user    
def create_control_information(sender, instance, created, **kwargs):
    if created:
        ControlInformation.objects.create(user=instance)

post_save.connect(create_control_information, sender=User)


class LivingRoom(models.Model):
    '''Living Room object'''
    user = models.OneToOneField(User)
        
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
def create_control_livingroom(sender, instance, created, **kwargs):
    if created:
        LivingRoom.objects.create(user=instance)

post_save.connect(create_control_livingroom, sender=User)
        

class DinningRoom(models.Model):
    '''Dinning Room object'''
    user = models.OneToOneField(User)
        
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
    
#signal function: if a user is created, add control information to the user    
def create_control_dinningroom(sender, instance, created, **kwargs):
    if created:
        DinningRoom.objects.create(user=instance)

post_save.connect(create_control_dinningroom, sender=User)


class Kitchen(models.Model):
    '''Kitchen object'''
    user = models.OneToOneField(User)
        
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
    
#signal function: if a user is created, add control information to the user    
def create_control_kitchen(sender, instance, created, **kwargs):
    if created:
        Kitchen.objects.create(user=instance)

post_save.connect(create_control_kitchen, sender=User)

        
class BedRoom1(models.Model):
    '''Kitchen object'''
    user = models.OneToOneField(User)
    
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
    
#signal function: if a user is created, add control information to the user    
def create_control_bedroom1(sender, instance, created, **kwargs):
    if created:
        BedRoom1.objects.create(user=instance)

post_save.connect(create_control_bedroom1, sender=User)
    

class BedRoom2(models.Model):
    '''Kitchen object'''
    user = models.OneToOneField(User)
    
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
    
#signal function: if a user is created, add control information to the user    
def create_control_bedroom2(sender, instance, created, **kwargs):
    if created:
        BedRoom2.objects.create(user=instance)

post_save.connect(create_control_bedroom2, sender=User)
    
        
class BedRoom3(models.Model):
    '''Kitchen object'''
    user = models.OneToOneField(User)
    
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
    
#signal function: if a user is created, add control information to the user    
def create_control_bedroom3(sender, instance, created, **kwargs):
    if created:
        BedRoom3.objects.create(user=instance)

post_save.connect(create_control_bedroom3, sender=User)

        
        
        
        
        
        
        
        
        


