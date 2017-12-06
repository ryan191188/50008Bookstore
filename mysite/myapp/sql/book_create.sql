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