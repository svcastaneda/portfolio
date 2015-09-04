from django import forms
# from .models import *
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect

class send_email(forms.Form):
    sender = forms.CharField()
    subject = forms.CharField()
    message = forms.CharField()
    from_email = forms.EmailField()