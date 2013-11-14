from django import forms
from django.contrib.auth.models import User
#from django.forms import ModelForm
#from control.models import ControlInformation

class ControlInformationForm(forms.Form):
    
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
    
    on_off = forms.ChoiceField(label="on_off", choices=TURN_ON_OFF)
    auto_manu = forms.ChoiceField(label="auto_manu", choices=AUTO_MANU)
    temp_dinningroom = forms.ChoiceField(label="temp_dinningroom", choices=TEMP_DINNINGROOM)
    temp_livingroom = forms.ChoiceField(label="temp_livingroom", choices=TEMP_LIVINGROOM)
    
        
class LivingRoomControl(forms.Form):
    
    TURN_ON_OFF = (
        ('ON', 'On'),
        ('OFF', 'Off'),
    )
    
    TEMP = (
        ('HIGH', 'High'),
        ('MEDIUM', 'Medium'),
        ('LOW', 'Low'),
    )
    
    on_off = forms.ChoiceField(label="on_off", choices=TURN_ON_OFF)
    temp = forms.ChoiceField(label="temperature", choices=TEMP)
    
class DinningRoomControl(forms.Form):
    
    TURN_ON_OFF = (
        ('ON', 'On'),
        ('OFF', 'Off'),
    )
    
    TEMP = (
        ('HIGH', 'High'),
        ('MEDIUM', 'Medium'),
        ('LOW', 'Low'),
    )
    
    on_off = forms.ChoiceField(label="on_off", choices=TURN_ON_OFF)
    temp = forms.ChoiceField(label="temperature", choices=TEMP)
    
class KitchenControl(forms.Form):
    
    TURN_ON_OFF = (
        ('ON', 'On'),
        ('OFF', 'Off'),
    )
    
    TEMP = (
        ('HIGH', 'High'),
        ('MEDIUM', 'Medium'),
        ('LOW', 'Low'),
    )
    
    on_off = forms.ChoiceField(label="on_off", choices=TURN_ON_OFF)
    temp = forms.ChoiceField(label="on_off", choices=TEMP)
    
class BedRoom1Control(forms.Form):
    
    TURN_ON_OFF = (
        ('ON', 'On'),
        ('OFF', 'Off'),
    )
    
    TEMP = (
        ('HIGH', 'High'),
        ('MEDIUM', 'Medium'),
        ('LOW', 'Low'),
    )
    
    on_off = forms.ChoiceField(label="on_off", choices=TURN_ON_OFF)
    temp = forms.ChoiceField(label="temperature", choices=TEMP)
    
class BedRoom2Control(forms.Form):
    
    TURN_ON_OFF = (
        ('ON', 'On'),
        ('OFF', 'Off'),
    )
    
    TEMP = (
        ('HIGH', 'High'),
        ('MEDIUM', 'Medium'),
        ('LOW', 'Low'),
    )
    
    on_off = forms.ChoiceField(label="on_off", choices=TURN_ON_OFF)
    temp = forms.ChoiceField(label="temperature", choices=TEMP)
    
class BedRoom3Control(forms.Form):
    
    TURN_ON_OFF = (
        ('ON', 'On'),
        ('OFF', 'Off'),
    )
    
    TEMP = (
        ('HIGH', 'High'),
        ('MEDIUM', 'Medium'),
        ('LOW', 'Low'),
    )
    
    on_off = forms.ChoiceField(label="on_off", choices=TURN_ON_OFF)
    temp = forms.ChoiceField(label="temperature", choices=TEMP)
    
    
    
    
    
    
    



        

        