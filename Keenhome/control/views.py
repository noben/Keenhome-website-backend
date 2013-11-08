# Create your views here.
from django.http import HttpResponseRedirect, HttpResponse
from django.template import RequestContext, loader
from django.template.context import RequestContext
from django.core.urlresolvers import reverse
from django.shortcuts import render
from django.shortcuts import render_to_response

#models for user signup
from django.contrib.auth.models import User
from django.contrib import messages

#user Login/Logout && Registration
from django.contrib import auth
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect

#import user defined application functions
from control.models import ControlInformation
from control.forms import ControlInformationForm

def control(request):
    if not request.user.is_authenticated():
        return HttpResponseRedirect('/keenhome/accounts/login/')
    
    form = ControlInformationForm(request.POST or None)
    
    if request.method=="POST":
        if form.is_valid():
            form = form.save(commit=False) 
            form.user = request.user# because user is excluded
            form.save()
            return HttpResponseRedirect('/keenhome/control/current_status/')
    
        else:
            form = ControlInformationForm()      
            return render_to_response("control/control.html", {'form':form}, context_instance=RequestContext(request))
    else:
        return render_to_response("control/control.html", {'form':form}, context_instance=RequestContext(requesst))
          
              
def current_status(request):
    if not request.user.is_authenticated():
        return HttpResponseRedirect('/keenhome/accounts/login/')
    Current_Status = request.user.get_profile()  
    
    on_off = Current_Status.turn_on_off
    auto_manu = Current_Status.auto_manu
    temp_dinningroom = Current_Status.temp_dinningroom
    temp_livingroom = Current_Status.temp_livingroom
       
    context = {'on_off': on_off,
               'auto_manu': auto_manu,
               'temp_dinningroom': temp_dinningroom, 
               'temp_livingroom': temp_livingroom,
               }
    return render(request, 'control/current_control_status.html', context)
       
       
       
       
       
        
        
        
        
        