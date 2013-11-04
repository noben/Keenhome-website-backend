from django import forms
from django.contrib.auth.models import User

class RegisterForm(forms.Form):  
    email=forms.EmailField(label="Email",max_length=30,widget=forms.TextInput(attrs={'size': 30,}))      
    password=forms.CharField(label="Password",max_length=30,widget=forms.PasswordInput(attrs={'size': 20,}))  
    username=forms.CharField(label="Name",max_length=30,widget=forms.TextInput(attrs={'size': 20,}))  
      
    def clean_username(self):  
        '''checking if name is a existed name'''  
        users = User.objects.filter(username__iexact=self.cleaned_data["username"])  
        if not users:  
            return self.cleaned_data["username"]  
        raise forms.ValidationError("This username has been used.")  
          
    def clean_email(self):  
        '''Checking if email is a existed email'''  
        emails = User.objects.filter(email__iexact=self.cleaned_data["email"])  
        if not emails:  
            return self.cleaned_data["email"]  
        raise forms.ValidationError("This email address has been used.")
        
class LoginForm(forms.Form):
    username=forms.CharField(label="Name",max_length=30,widget=forms.TextInput(attrs={'size': 20,}))
    password=forms.CharField(label="Password",max_length=30,widget=forms.PasswordInput(attrs={'size': 20,}))

        
        
        