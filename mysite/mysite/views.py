# -*- coding: utf-8 -*-
from __future__ import unicode_literals

#from django.shortcuts import render

# Create your views here.
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect, render_to_response

from django.contrib import messages

#from lib.utils import pagination
#from lib.decorators import json_response


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
    #print (form.is_valid())
        if form.is_valid():
                form.save()
                username = form.cleaned_data.get('username')
                raw_password = form.cleaned_data.get('password1')
                user = authenticate(username=username, password=raw_password)
                login(request, user)
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
    context = {"results": (('Photoshop Elements 9: The Missing Manual', 'paperback', '640', 'English', 'Barbara Brundage', 'Pogue Press', 'Science', '2010', '1449389678', '978-1449389673', 40),('Where Good Ideas Come From: The Natural History of Innovation', 'hardcover', '336', 'English', 'Steven Johnson', 'Riverhead Hardcover', 'Biology', '2010', '1594487715', '978-1594487712', 46))} #example results
    return render(request, 'search.html', context)

# @json_response
# def orders(request):

#     """Get order history of logged-in user."""
#     if not request.user.is_authenticated:
#         raise PermissionDenied(NOT_LOGGED_IN)

#     query = ''#sql query here
#     pg = pagination(request)

#     for row in sql(q + page(**pg), request.user.id):
#         yield order.__wrapped__(request, details=row)

#     args = {}
#     #args.update(csrf(request))
#     #args['error'] = ""
#     #args['ProductOrderForm'] = ProductOrderForm()

#     if request.method == 'POST':

#         order = Order(user=request.user.storeuser, paid=False)
#         order.save()
#         product_order = ProductOrder(order=order)
#         form = ProductOrderForm(request.POST, instance=product_order)
#         if form.is_valid():
#             form.save()
#             args['order_id'] = order.pk
#             return render(request, 'store/orders_more.html', args)
#         else:
#             order.delete()
#             args['error'] = "Order Submission Failed!"
#             return render(request, 'store/order_form.html', args)

#     return render(request, 'store/order_form.html', args)


def books(request):
    args = {'book':('Photoshop Elements 9: The Missing Manual', 'paperback', '640', 'English', 'Barbara Brundage', 'Pogue Press', 'Science', '2010', '1449389678', '978-1449389673', 40)}  #tuple that contains info on all the books. REPLACE THE TUPLE WITH A QUERY LANGUAGE TO GET THE BOOK. SHOULD GET THE ROWS
#NEED TO DO HTML FOR 'book' TO DO BOOK DETAILS
    print (request.path).split('/')[2]  ##this is the ISBN13 number used to query


    #search for feedback query

    args['topNfeedback']= (1,2)

    args['recommendation']=('samplebook','details')


    return render(request, 'books/book_details.html',args)

def userdata(request):
    if not request.user.username==request.path.split('/')[2]:
        raise PermissionDenied('NOT LOGGED IN')
    args={}
    return render(request, 'users.html',args)

@login_required
def userorders(request):
    if not request.user.username==request.path.split('/')[2]:
        raise PermissionDenied('NOT LOGGED IN')
    args={}
    args['results'] = (('Today', 'booktitle'),('date','anothrbook'))
    return render(request, 'user_orders.html',args)

@login_required
def userfeedback(request):
    if not request.user.username==request.path.split('/')[2]:
        raise PermissionDenied('NOT LOGGED IN')
    args={}
    args['results'] = (('Today', 'booktitle'),('date','anothrbook'))
    return render(request, 'user_feedback.html',args)

@login_required
def userratings(request):
    if not request.user.username==request.path.split('/')[2]:
        raise PermissionDenied('NOT LOGGED IN')
    args={}
    args['results'] = (('Today', 'booktitle'),('date','anothrbook'))
    return render(request, 'user_ratings.html',args)

@login_required
def newbook(request):
    if not request.user.username=='admin':
        raise PermissionDenied('NOT LOGGED IN')
    args={}
    return render(request, 'newbook.html',args)

@login_required
def arrivebook(request):
    args={}
    if not request.user.username=='admin':
        raise PermissionDenied('NOT LOGGED IN')

    if request.method == 'POST':
        for key in request.POST.keys():
            print (key,":",request.POST[key])
        # insert SQL query here
        #add more book copies
        return render(request, 'arrivebook.html',args)
    else:
        args = {"results": (('Photoshop Elements 9: The Missing Manual', 'paperback', '640', 'English', 'Barbara Brundage', 'Pogue Press', 'Science', '2010', '1449389678', '978-1449389673', 40),('Where Good Ideas Come From: The Natural History of Innovation', 'hardcover', '336', 'English', 'Steven Johnson', 'Riverhead Hardcover', 'Biology', '2010', '1594487715', '978-1594487712', 46))} #example results        
        return render(request, 'arrivebook.html',args)





