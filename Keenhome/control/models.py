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
    
    turn_on_off = models.CharField(max_length=1, choices=TURN_ON_OFF)
    auto_manu = models.CharField(max_length = 1, choices=AUTO_MANU)
    temp_dinningroom = models.CharField(max_length=1, choices=TEMP_DINNINGROOM)
    temp_livingroom = models.CharField(max_length=1, choices=TEMP_LIVINGROOM)

#signal function: if a user is created, add control information to the user    
def create_control_information(sender, instance, created, **kwargs):
    if created:
        ControlInformation.objects.create(user=instance)

post_save.connect(create_control_information, sender=User)










