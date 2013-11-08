from django import forms
from django.contrib.auth.models import User
from django.forms import ModelForm
from control.models import ControlInformation

class ControlInformationForm(ModelForm):
    
    class Meta:
        model = ControlInformation
        fields = ['ON_OFF', 'AUTO_MANU', 'TEMP_DINNINGROOM', 'TEMP_LIVINGROOM']
        exclude = (user,)
        
        
        