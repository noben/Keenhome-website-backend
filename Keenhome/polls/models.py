from django.db import models
import datetime
from django.utils import timezone

class Poll(models.Model):
    question = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    
    def __unicode__(self):
            return self.question
    
    def was_published_recently(self):
            return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
            

class Choice(models.Model):
    poll = models.ForeignKey(Poll)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    
    def __unicode__(self):
            return self.choice_text
            
    def was_published_recently(self):
            return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
            
            
class UserProfile(models.Model):
    user = models.ForeignKey(User, unique=True)
    name = models.CharField(max_length=30, blank=True)
    productNo = models.CharField(max_length=50, blank=True)
    location = models.CharField(max_length=50, blank=True)
    average_temp = models.IntegerField(max_length=5, blank=True)
    
    HOME_TYPE = (
        ('AP', 'Apartment/Condo'),
        ('SH', 'Single House/Residential'),
        ('ST', 'Studio'),
        ('TH', 'Townhouse'),
        ('MH', 'Moblie Home'),
    )
    
    home_type = models.CharField(max_length=1, choices=HOME_TYPE)
    
    
    
    
    
    
    
    
    
