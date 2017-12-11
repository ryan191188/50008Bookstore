# 50008Bookstore
Web application with a database backend using Django.

```
Group Members:
Dily 100
Runner 100
So Young 100
Nam 100
Ryan 100
```

## ER Diagram
<br>
<img height = "700" src="https://github.com/leepeckfern/50008Bookstore/blob/ryan_sql/erdplus-diagram.jpg"/>
<br>

## Preparing computer

1. Install MySql

DATABASE CONFIGURATION (MySQL)
```
'NAME'    : 'bookstoreproject',
'USER'    : 'root',
'PASSWORD': 'password'  <set own password>,
'HOST'    : ''          <localhost>
```

DATABASE CONFIGURATION (Django)

/50008Bookstore/mysite/mysite/settings.py
```
ALLOWED_HOSTS = ['localhost',u'10.12.171.173',u'10.0.2.15',u'10.12.232.80',u'127.0.0.1']

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_extensions',
    'myapp', #(name of app)
]

DATABASES = {
    'default': {
        'ENGINE'  : 'django.db.backends.mysql',
        'NAME'    : 'bookstoreproject',
        'USER'    : 'root',
        'PASSWORD': 'password',
        'HOST'    : '',
    }
}
```

/50008Bookstore/mysite/myapp/settings.py
```
ALLOWED_HOSTS = ['localhost',u'10.12.171.173',u'10.0.2.15',u'10.12.255.182']

INSTALLED_APPS = [
    'myapp.apps.MyAppConfig', #(name of app)
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

DATABASES = {
    'default': {
        'ENGINE'  : 'django.db.backends.mysql',
        'NAME'    : 'bookstoreproject',
        'USER'    : 'root',
        'PASSWORD': 'password',
        'HOST'    : '',
    }
}
```

2. Open Terminal(MacOS) / Command Prompt(Windows) 

Log in to mysql client to create database

```
> cd C:\Program Files\MySQL\MySQL Server 5.7\bin
> mysql -u root -p
Enter password: ********

mysql> CREATE DATABASE bookstoreproject;
mysql> USE bookstoreproject;

mysql> exit
Bye
```

3. Load initial user data to auth_user table
(not very sure if auth_user table is created already)
```
> python manage.py runscript users
```

4. Create tables and load initial data (through SQL scripts)

```
> python manage.py makemigrations <myapp> (myapp - name of app)
> python manage.py migrate
```

## Relational Schema

1. Users Table

```sql
CREATE TABLE auth_user(
id int(11) NOT NULL AUTO_INCREMENT,
password varchar(128) NOT NULL,
last_login datetime(6) DEFAULT NULL,
is_superuser tinyint(1) NOT NULL,
username varchar(150) NOT NULL,
first_name varchar(30) NOT NULL,
last_name varchar(30) NOT NULL,
email varchar(254) NOT NULL,
is_staff tinyint(1) NOT NULL,
is_active tinyint(1) NOT NULL,
date_joined datetime(6) NOT NULL,
PRIMARY KEY (id),
UNIQUE (username));
```

2. Books Table
```sql
CREATE TABLE myapp_book(
title VARCHAR(256) NOT NULL,
format CHAR(9),
pages INT,
language VARCHAR(32),
authors VARCHAR(256) NOT NULL,
publisher VARCHAR(64) NOT NULL,
bookSubject VARCHAR(64),
year CHAR(4) NOT NULL,
ISBN10 CHAR(10) NOT NULL UNIQUE,
ISBN13 CHAR(14),
numberOfCopies INT,
PRIMARY KEY (ISBN13),
CHECK (format = 'paperback' OR format='hardcover'))
```

3. Orders Table
```sql
CREATE TABLE myapp_orders(
loginName VARCHAR(64),
ISBN13 CHAR(14),
quantityOrdered INT NOT NULL,
orderDate DATETIME NOT NULL,
PRIMARY KEY (loginName, ISBN13, orderDate),
FOREIGN KEY (loginName) REFERENCES auth_user(username) ON DELETE CASCADE ON UPDATE CASCADE,
FOREIGN KEY (ISBN13) REFERENCES myapp_book(ISBN13) ON DELETE CASCADE ON UPDATE CASCADE)
```

Create Trigger for Orders Table during INSERT
```sql
CREATE TRIGGER update_qty AFTER INSERT ON myapp_orders 
	FOR EACH ROW 
		UPDATE myapp_book SET numberOfCopies = numberOfCopies - NEW.quantityOrdered
        WHERE ISBN13 = NEW.ISBN13
```

4. FeedbackOnBooks Table
```sql
CREATE TABLE myapp_feedback(
loginName VARCHAR(32),
ISBN13 CHAR(14),
score INT NOT NULL,
feedbackText VARCHAR(100),
feedbackDate DATE NOT NULL,
PRIMARY KEY (loginName, ISBN13),
FOREIGN KEY (loginName) REFERENCES auth_user(username) ON DELETE CASCADE ON UPDATE CASCADE,
FOREIGN KEY (ISBN13) REFERENCES myapp_orders(ISBN13) ON DELETE CASCADE ON UPDATE CASCADE,
CHECK (score >= 0 and score <= 10))
```

5. RatingOnUserFeedback Table
```sql
CREATE TABLE myapp_usefulness(
loginName VARCHAR(64),
score INT NOT NULL,
userBeingRated VARCHAR(64),
ISBN13 CHAR(14),
PRIMARY KEY (loginName, userBeingRated, ISBN13, orderDate),
FOREIGN KEY (loginName) REFERENCES auth_user(username) ON DELETE CASCADE ON UPDATE CASCADE,
FOREIGN KEY (userBeingRated) REFERENCES myapp_feedback(loginName) ON DELETE CASCADE ON UPDATE CASCADE,
FOREIGN KEY (ISBN13) REFERENCES myapp_feedback(ISBN13) ON DELETE CASCADE ON UPDATE CASCADE,
CHECK (loginName <> userBeingRated),
CHECK (score = 0 or score = 1 or score = 2))
```

## Summary of Features

- Registration
- Ordering
- User Records (Account info, orders, feedbacks and usefulness ratings)
- Arrival of new books
- Arrival of more copies
- Feedback Recordings
- Usefulness Ratings
- Book Browsing
- Top n most useful feedbacks
- Book Recommendation
- Statistics (m most popular books, authors publishers)

## Registration

New users will sign up at the registration page in order to log in to their account 

To register, the user will have to input the following information:

- Username
- Password

Checks are made in the registration form to ensure that the fields are not empty and the username is not taken by another person. The code below checks for the validity of the user registration form input:

```python
def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
                form.save()
                username = form.cleaned_data.get('username')
                raw_password = form.cleaned_data.get('password1')
                user = authenticate(username=username, password=raw_password)
```

During the signup page, the user needs to enter the password twice for password confirmation
New users are inserted into the auth_user table, with their passwords hashed in the password field.

Once a user has successfully registered, he will then be able to log in into his account in the future, as shown in the code below:

```python
if form.is_valid():
                form.save()
                username = form.cleaned_data.get('username')
                raw_password = form.cleaned_data.get('password1')
                user = authenticate(username=username, password=raw_password)
                login(request, user)
                messages.info(request, 'User created!')
                return redirect('/accounts/login')
```

## Ordering

Once a user decides on a book he/she wants to order through the search function, the user simply clicks on the `order` button to purchase the book. THe user can select the quantity of books he/she wants to purchase.

The SQL query in the `def orders(request)` checks whether there is sufficient quantity for the users to purchase. The below query is executed once the order is successful.

```sql
INSERT INTO myapp_orders(loginName,ISBN13,quantityOrdered,orderDate)
VALUES ('%s','%s','%s','%s')"%(username,ISBN13,numberOfCopies,orderDate)
```

The trigger in the myapp_orders table will automatically decrease the numberOfCopies in myapp_book table according to ISBN13 key.

## User Records
- Account info
- Orders
- Feedbacks
- Usefulness ratings

The SQL query below is used to display the information found in the user's account:
```sql
SELECT username,first_name,last_name,email FROM auth_user 
WHERE username='%s'"%(username)
```

Similarly, the user's order history can be retrieved with the following query:
```sql
SELECT myapp_orders.*, myapp_book.title
FROM myapp_orders, myapp_book
WHERE myapp_orders.ISBN13 = myapp_book.ISBN13
AND myapp_orders.loginName = '%s'"%(username)
```

For the user's feedback history on each book:
```sql
SELECT *
FROM myapp_feedback
WHERE myapp_feedback.loginName = '%s'
Order by feedbackDate
DESC"%(username)
```

For the user's usefulness ratings on each feedback:
```sql
SELECT myapp_usefulness.loginName,myapp_usefulness.score, myapp_feedback.*
FROM myapp_usefulness, myapp_feedback
WHERE myapp_usefulness.loginName = '%s'
AND myapp_feedback.loginName= myapp_usefulness.userBeingRated
Order by feedbackDate
DESC"%(username)
```

## Arrival of New Books

As a user with admin privileges (store manager), the `def newbook(request)` allows the admin user to enter the details of the new book as well as specify the quantity of the new book.

The below function has an INSERT sql query into the myapp_book table:
```python
if request.method=='POST':
        for key in request.POST.keys():
            print(key, request.POST[key])
        q = 'INSERT INTO myapp_book (title, format, pages, language, authors, publisher, bookSubject, year, ISBN10, ISBN13, numberOfCopies) VALUES'\
        + "('" + request.POST['title'] + "', '" + request.POST['format'] + "', '" + request.POST['pages'] + "', '" + request.POST['language']\
        + "', '" + request.POST['authors'] + "', '" + request.POST['publisher'] + "', '" + request.POST['subject'] + "', '" + request.POST['year'] + "', '"\
        + request.POST['isbn10'] + "', '" + request.POST['isbn13'] + "', 1)" 
```

To create an admin user, run the following using manage.py:
```
> python manage.py createsuperuser
Username (leave blank to use 'user'): admin
Email address: admin@sutd.edu.sg
Password: ********
Password (again): ********
Superuser created successfully.
```

## Arrival of more Copies

Store manager increases number of copies in the bookstore, which the following function `def arrivebook(request)` executes the UPDATE 
sql query to update the numberOfCopies in the myapp_book table according to the book ISBN13 number.

```python
def arrivebook(request):
    args={}
    if not request.user.username=='admin':
        raise PermissionDenied('NOT LOGGED IN')

    if request.method == 'POST':
        for key in request.POST.keys():
            print (key,":",request.POST[key])
        
        q = "UPDATE myapp_book SET myapp_book.numberOfCopies = myapp_book.numberOfCopies + " + request.POST["quantity"] + " WHERE myapp_book.ISBN13 = '" + request.POST["isbn13"] +"'"
        
        cursor = connection.cursor()
        cursor.execute(q)
        row = cursor.fetchall()
        return render(request, 'arrivebook.html',args)
    else:     
        return render(request, 'arrivebook.html',args)
```

## Feedback Recordings

For each book, a user can leave a personal feedback, but he/she cannot leave more than 1 feedback for the same book. 
A feedback includes:

- Description of the feedback (optional)
- Rating from 0 - 10

The following sql query is executed when the user submits the feedback for the book
```sql
INSERT INTO myapp_feedback(loginName,ISBN13,score,feedbackText,feedbackDate)
VALUES ('%s','%s','%s','%s','%s')"%(username,ISBN13,score,feedbackText,feedbackDate)
```

## Usefulness Ratings

Users may rate the feedback submitted by other users according to a certain book. However, users are not allowed to rate their own feedback

Users can either rate the feedback:

- Very useful (2)
- Useful      (1)
- Useless     (0)

The SQL query below is executed when a user enters his rating for a particular user's feedback:
```sql
INSERT INTO myapp_usefulness(loginName,score,userBeingRated,ISBN13)
VALUES ('%s','%s','%s','%s')"%(username,score,userBeingRated,ISBN13)
```

## Book Browsing

