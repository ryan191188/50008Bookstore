# -*- coding: utf-8 -*-
from __future__ import unicode_literals

#from django.shortcuts import render

# Create your views here.
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect, render_to_response

from django.contrib import messages
def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
	print (form.is_valid())
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            #user = authenticate(username=username, password=raw_password)
            #login(request, user)
	    messages.info(request, 'User created!')
            return redirect('/accounts/login') #Create a new page late
	
    else:
        form = UserCreationForm()
    
    return render(request, 'signup.html', {'form': form})
