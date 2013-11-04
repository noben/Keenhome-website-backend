# Create your views here.
from django.http import HttpResponseRedirect, HttpResponse
from django.template import RequestContext, loader
from django.template.context import RequestContext
from django.core.urlresolvers import reverse
from django.shortcuts import render, get_object_or_404
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
from polls.models import Poll, Choice, UserProfile
from polls.forms import RegisterForm, LoginForm

def index(request):
    if not request.user.is_authenticated():
        return HttpResponseRedirect('/keenhome/accounts/login/')
    latest_poll_list = Poll.objects.all().order_by('-pub_date')[:5]
    context = {'latest_poll_list': latest_poll_list}
    return render(request, 'polls/index.html', context)

def detail(request, poll_id):
    if not request.user.is_authenticated():
        return HttpResponseRedirect('/keenhome/accounts/login/')
    poll = get_object_or_404(Poll, pk=poll_id)
    return render(request, 'polls/detail.html', {'poll': poll})
    
def results(request, poll_id):
    if not request.user.is_authenticated():
        return HttpResponseRedirect('/keenhome/accounts/login/')
    poll = get_object_or_404(Poll, pk=poll_id)
    return render(request, 'polls/results.html', {'poll': poll})
    
def vote(request, poll_id):
    if not request.user.is_authenticated():
        return HttpResponseRedirect('/keenhome/accounts/login/')
    p = get_object_or_404(Poll, pk=poll_id)
    try:
        selected_choice = p.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the poll voting form.
        return render(request, 'polls/detail.html', {
            'poll': p,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(p.id,)))

#User Login/logout:
def login(request):
    '''login view'''   
    if request.method == 'POST':
        form=LoginForm(request.POST)
        if form.is_valid():
            user = auth.authenticate(username=form.cleaned_data["username"], password=form.cleaned_data["password"])
            if user is not None and user.is_active:
                # Correct password, and the user is marked "active"
                auth.login(request, user)
                # Redirect to a success page.
                return HttpResponseRedirect('/keenhome/')
            else:
                # Show an error page/redirect to the login page for reinputting
                return HttpResponseRedirect('/keenhome/accounts/login/')
    else:
        form = LoginForm()
        return render_to_response("polls/login.html", {'form':form}, context_instance=RequestContext(request))

def logout(request):
    auth.logout(request)
    # Redirect to a success page.
    return HttpResponse('<title>Logout Page</title> <center><h1>Logout Success</h1></center>')

#User Register View    
def register(request):  
    '''signup view'''     
    if request.method=="POST":  
        form=RegisterForm(request.POST)  
        if form.is_valid():  
            username=form.cleaned_data["username"]  
            email=form.cleaned_data["email"]  
            password=form.cleaned_data["password"]  
            user=User.objects.create_user(username, email, password)  
            user.save()
            return HttpResponseRedirect('/keenhome/accounts/login/')
        else: 
            form = RegisterForm()      
            return render_to_response("polls/register.html", {'form':form}, context_instance=RequestContext(request))  

    #This is used for reinputting if failed to register    
    else: 
        form = RegisterForm()      
        return render_to_response("polls/register.html", {'form':form}, context_instance=RequestContext(request))

#List all the items of an user's profile
def user_profile(request):
    if not request.user.is_authenticated():
        return HttpResponseRedirect('/keenhome/accounts/login/')
    UserProfile = request.user.get_profile()
    
    name = UserProfile.name
    productNo = UserProfile.productNo
    location = UserProfile.location
    average_temp = UserProfile.average_temp
    home_type = UserProfile.home_type
    
    context = {'name': name,
               'productNo': productNo,
               'location': location, 
               'average_temp': average_temp,
               'home_type': home_type
               }
    return render(request, 'polls/user_profile.html', context)

