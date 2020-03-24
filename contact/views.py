from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.core.mail import EmailMessage
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from django.template.loader import get_template

class ContactForm(forms.Form):
    fname = forms.CharField(required=True)
    #lname = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    subject = forms.CharField(required=True)
    message= forms.CharField(required=True)

def detail(request):
    return render(request,'contact/detail.html')
def Contact(request):
    Contact_Form = ContactForm
    if request.method == 'POST':
        form = Contact_Form(data=request.POST)
        #print("hello")

        if form.is_valid():
            fname = request.POST.get('fname')
            #lname=request.POST.get('lname')

            email = request.POST.get('email')
            subject = request.POST.get('subject')
            message=request.POST.get('message')

            template = get_template('contact/contactform.txt')
            context = {
                'fname' : fname,
                #'lname' : lname,
                'email' : email,
                'subject' : subject,
                'message' : message,

            }

            content = template.render(context)

            email1 = EmailMessage(
                "New contact form email",
                content,
                "Creative web" + '',
                ['mkjaipur13@gmail.com'],
                headers = { 'Reply To': email }
            )

            email1.send()
        #return redirect('success')
        #else:
        #    print("Not valid")


    #return render(request, 'detail.html')
    return redirect('detail')
