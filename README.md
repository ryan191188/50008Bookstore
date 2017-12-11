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

## Preparing computer




