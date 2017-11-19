# -*- coding: utf-8 -*-
from __future__ import unicode_literals

#from django.shortcuts import render

# Create your views here.
from django.contrib.auth import login, authenticate, logout
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
    print (request.user.username)
    for key in request.GET.keys():
        print key,":",request.GET[key]
    # insert SQL query here
    context = {"results": ["Book 1","Book 2"]} #example results
    return render(request, 'search.html', context)

def orders(request):
	args = {}
	args.update(csrf(request))
	args['error'] = ""
	args['ProductOrderForm'] = ProductOrderForm()

	if request.method == 'POST':

		order = Order(user=request.user.storeuser, paid=False)
		order.save()
		product_order = ProductOrder(order=order)
		form = ProductOrderForm(request.POST, instance=product_order)

		if form.is_valid():
			form.save()
			args['order_id'] = order.pk
			return render(request, 'store/orders_more.html', args)
		else:
			order.delete()
			args['error'] = "Order Submission Failed!"
			render(request, 'store/order_form.html', args)

	return render(request, 'store/order_form.html', args)

