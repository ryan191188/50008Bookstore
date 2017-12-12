# -*- coding: utf-8 -*-
from __future__ import unicode_literals

#from django.shortcuts import render

# Create your views here.
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect, render_to_response
from django.core.exceptions import PermissionDenied

from django.contrib import messages
from django.db import connection
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

# def login(request):
#     print "login"
#     username = request.POST['username']
#     password = request.POST['password']
#     user = authenticate(username=username, password=password)
#     if user is not None:
#         if user.is_active:
#             login(request, user)
#             HttpResponseRedirect('../user/%s/profile/'%username) 
#         else:
#             pass# Return a 'disabled account' error message
#     else:
#         pass# Return an 'invalid login' error message.

# def logout(request):
#     logout(request)
#     return redirect('/accounts/login/')

def loginSuccess(request):
    path = "/user/"+request.user.username+"/profile"
    return redirect(path)

def search(request):
    args ={}
    q = '''SELECT myapp_book.*,AVG(myapp_feedback.score) 
    FROM myapp_book,myapp_feedback 
    WHERE myapp_book.ISBN13 = myapp_feedback.ISBN13'''
    # firstKey = True
    for key in request.GET.keys():
        print (key,":",request.GET[key])
    # insert SQL query here
        
        # if request.GET[key] != '' and firstKey and key!='sortby':
        #     q += ' WHERE ' + key + ' LIKE ' + "'%" + (request.GET[key]) + "%'"
        #     firstKey = False
        if request.GET[key] != '' and key!='sortby':
            q += ' AND ' + key + ' LIKE ' + "'%" + (request.GET[key]) + "%'"
    q+=' GROUP BY myapp_book.ISBN13 '
    if 'sortby' in request.GET:
        q+= ' ORDER BY ' + (request.GET['sortby'] if request.GET['sortby'] == 'year' else 'AVG(myapp_feedback.score)') + ' DESC'
    print(q)
    cursor = connection.cursor()
    cursor.execute(q)
    #context = {"results": (('Photoshop Elements 9: The Missing Manual', 'paperback', '640', 'English', 'Barbara Brundage', 'Pogue Press', 'Science', '2010', '1449389678', '978-1449389673', 40),('Where Good Ideas Come From: The Natural History of Innovation', 'hardcover', '336', 'English', 'Steven Johnson', 'Riverhead Hardcover', 'Biology', '2010', '1594487715', '978-1594487712', 46))} #example results
    row = cursor.fetchall()
    args['results']=row
    print(row)
    return render(request, 'search.html', args)
    #return row


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
    #args = {'book':('Photoshop Elements 9: The Missing Manual', 'paperback', '640', 'English', 'Barbara Brundage', 'Pogue Press', 'Science', '2010', '1449389678', '978-1449389673', 40)}  #tuple that contains info on all the books. REPLACE THE TUPLE WITH A QUERY LANGUAGE TO GET THE BOOK. SHOULD GET THE ROWS
#NEED TO DO HTML FOR 'book' TO DO BOOK DETAILS
    args = {}
    ISBN13 = (request.path).split('/')[2]

    if request.method =="POST":
        if 'orderbutton' in request.POST:
            quantity = request.POST['quantity']
            print(quantity)
            q= "INSERT INTO myapp_orders VALUES ('" \
                + request.user.username + "', '" + ISBN13 + "', " + quantity + ", NOW() )"
            print(q)
            cursor = connection.cursor()
            cursor.execute(q)
        elif "bookRatingbutton"in request.POST:
            score = request.POST['BookRating']
            print(score)
            q= "INSERT INTO myapp_feedback VALUES ('" \
                + request.user.username + "', '" + ISBN13 + "', " +  score \
                + ", ' " + request.POST['comments'] + "' , "+ " CURDATE() )"
            print(q)
            cursor = connection.cursor()
            try:
                cursor.execute(q)
            except:
                raise PermissionDenied("안녕")
        elif "0" in request.POST  or "1" in request.POST or "2" in request.POST:
            rating = None
            if "0" in request.POST:
                rating = 0
            elif "1" in request.POST:
                rating = 1
            elif "2" in request.POST:
                rating = 2    

            if request.user.username == request.POST[str(rating)]:
                raise PermissionDenied("qwertyuiop")

            q= "INSERT INTO myapp_usefulness (loginName,userBeingRated,ISBN13,score)VALUES ('" \
                + request.user.username + "', '" + request.POST[str(rating)] + "', '" +  ISBN13 \
                + "', " + str(rating) + ")"
            print(q)
            cursor = connection.cursor()
            try:
                cursor.execute(q)
            except:
                raise PermissionDenied("u voted already")
    #print(request.path).split('/')[2]  ##this is the ISBN13 number used to query
    q = "SELECT * FROM myapp_book WHERE ISBN13 = "
    q+="'"+ISBN13+"'"
    #print(q)
    cursor = connection.cursor()
    cursor.execute(q)
    #context = {"results": (('Photoshop Elements 9: The Missing Manual', 'paperback', '640', 'English', 'Barbara Brundage', 'Pogue Press', 'Science', '2010', '1449389678', '978-1449389673', 40),('Where Good Ideas Come From: The Natural History of Innovation', 'hardcover', '336', 'English', 'Steven Johnson', 'Riverhead Hardcover', 'Biology', '2010', '1594487715', '978-1594487712', 46))} #example results
    row = cursor.fetchall()
    args['book']=row

    #search for feedback query
    if 'topn' in request.POST:
        query = 'SELECT F.* '\
                + 'FROM myapp_feedback F, '\
                + '(SELECT T.userBeingRated,T.ISBN13,avg(T.score) '\
                + 'FROM (SELECT R.* '\
                + 'FROM myapp_feedback F, myapp_usefulness R '\
                + 'WHERE F.ISBN13 = R.ISBN13) as T '\
                + "WHERE T.ISBN13 = '" + ISBN13 +"' "\
                + 'GROUP BY T.userBeingRated '\
                + 'ORDER BY avg(T.score) '\
                + 'DESC) as T2 '\
                + 'WHERE F.loginName = T2.userBeingRated '\
                + 'AND F.ISBN13 = T2.ISBN13 '\
                + "LIMIT "+ request.POST['topn'] +  ";"
    else:
        query = "SELECT * FROM myapp_feedback NATURAL JOIN myapp_book " \
            + "WHERE ISBN13 = " + "'" + ISBN13 +"'"\
            + " ORDER BY feedbackDate DESC;"
    #print query
    cursor = connection.cursor()
    cursor.execute(query)


    #context = {"results": (('Photoshop Elements 9: The Missing Manual', 'paperback', '640', 'English', 'Barbara Brundage', 'Pogue Press', 'Science', '2010', '1449389678', '978-1449389673', 40),('Where Good Ideas Come From: The Natural History of Innovation', 'hardcover', '336', 'English', 'Steven Johnson', 'Riverhead Hardcover', 'Biology', '2010', '1594487715', '978-1594487712', 46))} #example results
    row = cursor.fetchall()
    args['feedback']= row
    print(row)
 
    q = "SELECT title,ISBN13,COUNT(ISBN13) FROM myapp_orders NATURAL JOIN myapp_book " \
        + "WHERE loginName IN " \
            + "(SELECT b2.loginName FROM myapp_orders b1, myapp_orders b2 " \
            + "WHERE b1.ISBN13 = b2.ISBN13 " \
            + "AND b1.loginName <> b2.loginName " \
            + "AND b1.ISBN13 = '" + ISBN13 + "') " \
        + "AND ISBN13 <> '" + ISBN13 + "' " \
        + "GROUP BY ISBN13 " \
        + "ORDER BY COUNT(ISBN13) DESC;"


    # 978-0072465631 has alot of orders
    # 978-0672325670 also

    #print(q)
    cursor = connection.cursor()
    cursor.execute(q)
    row = cursor.fetchall()

    recommendations = list()
    for i in range(len(row) if len(row)<=3 else 3):
        recommendations.append(row[i])
    recommendations=tuple(recommendations)
    #print recommendations

    args['recommendation']= recommendations


    return render(request, 'books/book_details.html',args)

def userdata(request):
    if not request.user.username == request.path.split('/')[2]:
        raise PermissionDenied('NOT LOGGED IN')
    args={}
    return render(request, 'users.html',args)

@login_required
def userorders(request):
    if not request.user.username == request.path.split('/')[2]:
        raise PermissionDenied('NOT LOGGED IN')
    args={}

    q = "SELECT myapp_book.title,myapp_orders.* FROM myapp_orders,myapp_book WHERE myapp_orders.loginName = '" + request.user.username \
        + "' AND myapp_orders.ISBN13 = myapp_book.ISBN13 ORDER BY orderDate DESC"
    print(q)
    cursor = connection.cursor()
    cursor.execute(q)
    #context = {"results": (('Photoshop Elements 9: The Missing Manual', 'paperback', '640', 'English', 'Barbara Brundage', 'Pogue Press', 'Science', '2010', '1449389678', '978-1449389673', 40),('Where Good Ideas Come From: The Natural History of Innovation', 'hardcover', '336', 'English', 'Steven Johnson', 'Riverhead Hardcover', 'Biology', '2010', '1594487715', '978-1594487712', 46))} #example results
    row = cursor.fetchall()
    print(row)
    args['results'] = row
    return render(request, 'user_orders.html',args)

@login_required
def userfeedback(request):
    if not request.user.username == request.path.split('/')[2]:
        raise PermissionDenied('NOT LOGGED IN')
    args={}

    q = "SELECT * FROM myapp_feedback NATURAL JOIN myapp_book " \
        + "WHERE loginName = '" + request.user.username + "' " \
        + "ORDER BY feedbackDate DESC"

    print(q)
    cursor = connection.cursor()
    cursor.execute(q)
    row = cursor.fetchall()
    print(row)

    args['results'] = row
    return render(request, 'user_feedback.html',args)

@login_required
def userratings(request):
    if not request.user.username == request.path.split('/')[2]:
        raise PermissionDenied('NOT LOGGED IN')
    args={}    
    q = "SELECT t1.*,t2.feedbackText, t3.title "\
    + "FROM myapp_usefulness t1, myapp_feedback t2, myapp_book t3 "\
    + "WHERE t1.userBeingRated = t2.loginName "\
    + "AND t1.ISBN13 = t2.ISBN13 "\
    + "AND t1.loginName = '" + request.user.username +"' "\
    + "AND t1.ISBN13 = t3.ISBN13 " \
    + "ORDER BY t1.score DESC;"     
    print(q)
    cursor = connection.cursor()
    cursor.execute(q)
    row = cursor.fetchall()
    print(row)
    args['results']=row
    return render(request, 'user_ratings.html',args)

@login_required
def newbook(request):
    if not request.user.username=='admin':
        raise PermissionDenied('NOT LOGGED IN')
    args={}
    if request.method=='POST':
        for key in request.POST.keys():
            print(key, request.POST[key])
        q = 'INSERT INTO myapp_book (title, format, pages, language, authors, publisher, bookSubject, year, ISBN10, ISBN13, numberOfCopies) VALUES'\
        + "('" + request.POST['title'] + "', '" + request.POST['format'] + "', '" + request.POST['pages'] + "', '" + request.POST['language']\
        + "', '" + request.POST['authors'] + "', '" + request.POST['publisher'] + "', '" + request.POST['subject'] + "', '" + request.POST['year'] + "', '"\
        + request.POST['isbn10'] + "', '" + request.POST['isbn13'] + "', 1)" 


         
        print(q)
        cursor = connection.cursor()
        cursor.execute(q)
        row = cursor.fetchall()
        args['results']=row
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
        q = "UPDATE myapp_book SET myapp_book.numberOfCopies = myapp_book.numberOfCopies + " + request.POST["quantity"] + " WHERE myapp_book.ISBN13 = '" + request.POST["isbn13"] +"'"
        print(q)
        cursor = connection.cursor()
        cursor.execute(q)
        row = cursor.fetchall()
        return render(request, 'arrivebook.html',args)
    else:     
        return render(request, 'arrivebook.html',args)



@login_required
def statistics(request):
    args={}
    if not request.user.username=='admin':
        raise PermissionDenied('NOT LOGGED IN')

    return render(request, 'arrivebook.html',args)



