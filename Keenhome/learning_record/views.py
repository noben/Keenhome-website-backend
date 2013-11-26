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
from learning_record.models import RecordLivingRoom, RecordDinningRoom, RecordKitchen

def show_records(request):
    pass


