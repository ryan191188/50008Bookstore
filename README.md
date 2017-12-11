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

3. 

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






