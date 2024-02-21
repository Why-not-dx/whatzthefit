from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .models import Message


class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    username = forms.CharField(
        widget=forms.TextInput(attrs ={
            "placeholder":"Your username", "class": "w-full py-4 px-6 rounded-xl"
            } ), )
    email = forms.CharField(
        widget=forms.EmailInput(attrs ={
            "placeholder":"Your email address", "class": "w-full py-4 px-6 rounded-xl"
            } ), )
    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs ={
            "placeholder":"Enter your password", "class": "w-full py-4 px-6 rounded-xl"
            } ), )
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs ={
            "placeholder":"Re-enter your password here", "class": "w-full py-4 px-6 rounded-xl"
            } ), )
    

class LoginForm(AuthenticationForm):

    username = forms.CharField(
        widget=forms.TextInput(attrs ={
            "placeholder":"Your username", "class": "w-full py-4 px-6 rounded-xl"
            } ), )  
    
    password = forms.CharField(
        widget=forms.PasswordInput(attrs ={
            "placeholder":"Enter your password", "class": "w-full py-4 px-6 rounded-xl"
            } ), )

class ContactForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ["topic", "content"]
        widgets = {
            "topic": forms.TextInput(
                attrs={"placeholder":"What is your message about ?", "class": "w-full py-4 px-6 rounded-xl border"}
            ),
            "content": forms.Textarea(
                attrs={"class": "w-full py-4 px-6 rounded-xl border-2 border-gray-500"}
            ),
        }