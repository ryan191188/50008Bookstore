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
orderDate DATETIME NOT NULL,
score INT NOT NULL,
feedbackText VARCHAR(100)
PRIMARY KEY (loginName, ISBN13, orderDate)
FOREIGN KEY (loginName) REFERENCES auth_user(username) ON DELETE CASCADE ON UPDATE CASCADE,
FOREIGN KEY (ISBN13) REFERENCES myapp_orders(ISBN13) ON DELETE CASCADE ON UPDATE CASCADE,
FOREIGN KEY (orderDate) REFERENCES myapp_orders(orderDate) ON DELETE CASCADE ON UPDATE CASCADE,
CHECK (score >= 0 and score <= 10))
```

5. RatingOnUserFeedback Table
```sql
CREATE TABLE myapp_usefulness(
loginName VARCHAR(64),
score INT NOT NULL,
userBeingRated VARCHAR(64),
ISBN13 CHAR(14),
orderDate DATETIME NOT NULL,
PRIMARY KEY (loginName, userBeingRated, ISBN13, orderDate),
FOREIGN KEY (loginName) REFERENCES auth_user(username) ON DELETE CASCADE ON UPDATE CASCADE,
FOREIGN KEY (userBeingRated) REFERENCES myapp_feedback(loginName) ON DELETE CASCADE ON UPDATE CASCADE,
FOREIGN KEY (ISBN13) REFERENCES myapp_feedback(ISBN13) ON DELETE CASCADE ON UPDATE CASCADE,
FOREIGN KEY (orderDate) REFERENCES myapp_feedback(orderDate) ON DELETE CASCADE ON UPDATE CASCADE,
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
