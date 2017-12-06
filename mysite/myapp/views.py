# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.views.generic.edit import CreateView
from django.views.generic.edit import UpdateView
from django.template import RequestContext
#from .models import Author

#from .models import Person
from django.core.exceptions import *

#from django.shortcuts import render

# Create your views here.
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect, render_to_response, HttpResponse

from django.contrib import messages
def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
    #print (form.is_valid())
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

def logout(request):
    logout(request)
    return redirect('/accounts/login/')

def search(request):
    for key in request.GET.keys():
        print (key,":",request.GET[key])
    # insert SQL query here
    context = {"results": ["Book 1","Book 2"]} #example results
    return render(request, 'search.html', context)

def get_object(self, queryset=None):
    obj = X.objects.get(id=self.kwargs['id'])
    return obj

# class AuthorCreate(CreateView):
#     model = Author
#     fields = ['name']


# class AuthorUpdate(UpdateView):
#     model = Author
#     fields = ['name']
#     template_name_suffix = '_update_form'


def index(request):
    #return render(request, 'form.html')
    return HttpResponse("<h1>bookstore!!!</h1>")

def search(request):
    if request.method == 'POST':
        search_id = request.POST.get('textfield', None)
        try:
            user = Person.objects.get(name = search_id)
            #do something with user
            html = ("<H1>%s</H1>", user)
            return HttpResponse(html)
        except Person.DoesNotExist:
            return HttpResponse("no such user")
    else:
        return render(request, 'form.html')

# def user_login(request):
#     if request.method == 'POST':
#         username = request.POST.get('username')
#         password = request.POST.get('password')

#         user = authenticate(username=username, password=password)

#         if user:
#             if user.is_active:
#                 login(request, user)
#                 return HttpResponseRedirect('login.html')
#                 #return redirect('/')
#             else:
#                 return HttpResponse('Your user account is disabled!')
#         else:
#             return HttpResponse("Invalid login details supplied!")
#     else:
#         return render(request, 'login.html')