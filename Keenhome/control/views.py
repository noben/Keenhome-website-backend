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

from control.models import LivingRoom, DinningRoom, Kitchen, BedRoom1, BedRoom2, BedRoom3
from control.forms import LivingRoomControl, DinningRoomControl, KitchenControl, BedRoom1Control, BedRoom2Control, BedRoom3Control
    
         
 
def control(request):
    if not request.user.is_authenticated():
        return HttpResponseRedirect('/keenhome/accounts/login/')
    
    Control_Information = ControlInformation.objects.get(user__username=request.user.username)
    if request.method == 'POST':
        form=ControlInformationForm(request.POST)
        if form.is_valid():
            Control_Information.turn_on_off = form.cleaned_data["on_off"]
            Control_Information.auto_manu = form.cleaned_data["auto_manu"]
            Control_Information.temp_dinningroom = form.cleaned_data["temp_dinningroom"]
            Control_Information.temp_livingroom = form.cleaned_data["temp_livingroom"]

            Control_Information.save()
            return HttpResponseRedirect('/keenhome/control/current_status/')
        else:
            form = ControlInformationForm()      
            return render_to_response("control/control.html", {'form':form}, context_instance=RequestContext(request))

    else:
        form = ControlInformationForm()
        return render_to_response("control/control.html", {'form':form}, context_instance=RequestContext(request))
 
              
def current_status(request):
    if not request.user.is_authenticated():
        return HttpResponseRedirect('/keenhome/accounts/login/')
    
    #the only problem happens here: how to get the ControlInformation
    Current_Status = ControlInformation.objects.get(user__username=request.user.username) 
    
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
    

def living_room(request):
    
    if not request.user.is_authenticated():
        return HttpResponseRedirect('/keenhome/accounts/login/')
    
    Living_Room = LivingRoom.objects.get(user__username=request.user.username)
    if request.method == 'POST':
        form=LivingRoomControl(request.POST)
        if form.isvalid():
            Living_Room.on_off = form.cleaned_data["on_off"]
            Living_Room.temp = form.cleaned_data["temp"]
            Living_Room.save()
            return HttpResponseRedirect('/keenhome/control/living_room/')
        else:
            on_off = Living_Room.on_off
            temp = Living_Room.temp
            form = LivingRoomControl()      
            return render_to_response("control/control.html", {'form':form, 'on_off':on_off, 'temp':temp}, context_instance=RequestContext(request))
    else:
        on_off = Living_Room.on_off
        temp = Living_Room.temp
        form = LivingRoomControl()
        return render_to_response("control/control.html", {'form':form, 'on_off':on_off, 'temp':temp}, context_instance=RequestContext(request))    
        

    
def dinning_room(request):
    
    if not request.user.is_authenticated():
        return HttpResponseRedirect('/keenhome/accounts/login/')
        
    Dinning_Room = DinningRoom.objects.get(user__username=request.user.username)
    if request.method == 'POST':
        form=DinningRoomControl(request.POST)
        if form.isvalid():
            Dinning_Room.on_off = form.cleaned_data["on_off"]
            Dinning_Room.temp = form.cleaned_data["temp"]
            Dinning_Room.save()
            return HttpResponseRedirect('/keenhome/control/dinning_room/')
        else:
            on_off = Dinning_Room.on_off
            temp = Dinning_Room.temp
            form = DinningRoomControl()      
            return render_to_response("control/control.html", {'form':form, 'on_off':on_off, 'temp':temp}, context_instance=RequestContext(request))
    else:
        on_off = Dinning_Room.on_off
        temp = Dinning_Room.temp
        form = DinningRoomControl()
        return render_to_response("control/control.html", {'form':form, 'on_off':on_off, 'temp':temp}, context_instance=RequestContext(request))    
        
    

def bed_room1(request):
    
    if not request.user.is_authenticated():
        return HttpResponseRedirect('/keenhome/accounts/login/')
    
    Bed_Room1 = BedRoom1.objects.get(user__username=request.user.username)
    if request.method == 'POST':
        form=BedRoom1Control(request.POST)
        if form.isvalid():
            Bed_Room1.on_off = form.cleaned_data["on_off"]
            Bed_Room1.temp = form.cleaned_data["temp"]
            Bed_Room1.save()
            return HttpResponseRedirect('/keenhome/control/bed_room1/')
        else:
            on_off = Bed_Room1.on_off
            temp = Bed_Room1.temp
            form = BedRoom1Control()      
            return render_to_response("control/bedroom1.html", {'form':form, 'on_off':on_off, 'temp':temp}, context_instance=RequestContext(request))
    else:
        on_off = Bed_Room1.on_off
        temp = Bed_Room1.temp
        form = BedRoom1Control()
        return render_to_response("control/bedroom1.html", {'form':form, 'on_off':on_off, 'temp':temp}, context_instance=RequestContext(request))    
    
    
    
    
def bed_room2(request):
    
    if not request.user.is_authenticated():
        return HttpResponseRedirect('/keenhome/accounts/login/')
    
    Bed_Room2 = BedRoom2.objects.get(user__username=request.user.username)
    if request.method == 'POST':
        form=BedRoom2Control(request.POST)
        if form.isvalid():
            Bed_Room2.on_off = form.cleaned_data["on_off"]
            Bed_Room2.temp = form.cleaned_data["temp"]
            Bed_Room2.save()
            return HttpResponseRedirect('/keenhome/control/bed_room2/')
        else:
            on_off = Bed_Room2.on_off
            temp = Bed_Room2.temp
            form = BedRoom2Control()      
            return render_to_response("control/bedroom2.html", {'form':form, 'on_off':on_off, 'temp':temp}, context_instance=RequestContext(request))
    else:
        on_off = Bed_Room2.on_off
        temp = Bed_Room2.temp
        form = BedRoom2Control()
        return render_to_response("control/bedroom2.html", {'form':form, 'on_off':on_off, 'temp':temp}, context_instance=RequestContext(request))    
    
    
    
def bed_room3(request):
    
    if not request.user.is_authenticated():
        return HttpResponseRedirect('/keenhome/accounts/login/')
    
    kit_chen = BedRoom3.objects.get(user__username=request.user.username)
    if request.method == 'POST':
        form=BedRoom3Control(request.POST)
        if form.isvalid():
            Bed_Room3.on_off = form.cleaned_data["on_off"]
            Bed_Room3.temp = form.cleaned_data["temp"]
            Bed_Room3.save()
            return HttpResponseRedirect('/keenhome/control/bed_room3/')
        else:
            on_off = Bed_Room3.on_off
            temp = Bed_Room3.temp
            form = BedRoom3Control()      
            return render_to_response("control/bedroom3.html", {'form':form, 'on_off':on_off, 'temp':temp}, context_instance=RequestContext(request))
    else:
        on_off = Bed_Room3.on_off
        temp = Bed_Room3.temp
        form = BedRoom2Control()
        return render_to_response("control/bedroom3.html", {'form':form, 'on_off':on_off, 'temp':temp}, context_instance=RequestContext(request))    
    
    

def kitchen(request):
    
    if not request.user.is_authenticated():
        return HttpResponseRedirect('/keenhome/accounts/login/')
    
    Kit_chen = Kitchen.objects.get(user__username=request.user.username)
    if request.method == 'POST':
        form=KitchenControl(request.POST)
        if form.isvalid():
            Kit_chen.on_off = form.cleaned_data["on_off"]
            Kit_chen.temp = form.cleaned_data["temp"]
            Kit_chen.save()
            return HttpResponseRedirect('/keenhome/control/kitchen/')
        else:
            on_off = Kit_chen.on_off
            temp = Kit_chen.temp
            form = KitchenControl()      
            return render_to_response("control/bedroom3.html", {'form':form, 'on_off':on_off, 'temp':temp}, context_instance=RequestContext(request))
    else:
        on_off = Kit_chen.on_off
        temp = Kit_chen.temp
        form = KitchenControl()
        return render_to_response("control/bedroom3.html", {'form':form, 'on_off':on_off, 'temp':temp}, context_instance=RequestContext(request))    
    
       
       
       
       
       
       
       
       
        
        
        
        
        