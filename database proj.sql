CREATE TABLE User(
loginName VARCHAR(32),
password VARCHAR(32) NOT NULL,
fullName VARCHAR(32) NOT NULL,
PRIMARY KEY (loginName))


CREATE TABLE BookArrival (
title VARCHAR(256) NOT NULL,
format CHAR(9),
pages INT,
language VARCHAR(32),
authors VARCHAR(256),
publisher VARCHAR(64),
year DATE,
ISBN10 CHAR(10) NOT NULL UNIQUE,
ISBN13 CHAR(14),
numberOfCopiesArrived INT,
PRIMARY KEY (ISBN13),
CHECK (format = 'paperback' OR format='hardcover'))



CREATE TABLE BookInStore (
TotalNumberOfCopies INT
PRIMARY KEY (ISBN13),
FOREIGN KEY (ISBN13) REFERENCES BookArrival (ISBN13))



-- Question 5
CREATE TRIGGER copyAvailableUpdate AFTER UPDATE ON BookArrival
for each row
UPDATE BookInStore SET BookInStore.TotalNumberOfCopies = BookInStore.TotalNumberOfCopies + BookArrival.orderQuantity WHERE BookInStore.ISBN13 = BookArrival.ISBN13




CREATE TABLE Order(
loginName VARCHAR(32),
ISBN13 CHAR(14),
orderQuantity INT NOT NULL,
orderDate DATE NOT NULL,
PRIMARY KEY (loginName, ISBN13),
FOREIGN KEY (loginName) REFERENCES User(loginName),
FOREIGN KEY (ISBN13) REFERENCES Book(ISBN13))


CREATE TABLE Feedback (
loginName VARCHAR(32),
ISBN13 CHAR(14),
score INT NOT NULL,
feedbackText VARCHAR(100)
PRIMARY KEY (loginName, ISBN13)
FOREIGN KEY (loginName) REFERENCES User(loginName),
FOREIGN KEY (ISBN13) REFERENCES BookInStore(loginName))
CHECK (score >= 0 and score <= 10))



CREATE TABLE myapp_usefulness (
loginName VARCHAR(64),
score INT NOT NULL,
userBeingRated VARCHAR(64),
ISBN13 CHAR(14),
PRIMARY KEY (loginName, userBeingRated, ISBN13),
FOREIGN KEY (loginName) REFERENCES auth_user(username),
FOREIGN KEY (userBeingRated) REFERENCES myapp_feedback(loginName),
FOREIGN KEY (ISBN13) REFERENCES myapp_feedback(ISBN13),
CHECK (loginName <> userBeingRated),
CHECK (score = 0 or score = 1 or score = 2))



-- Question 11

Select sum, ISBN13
FROM (Select ISBN13, sum(orderQuantity) AS sum
From Order
Where MONTH(orderDate) = 11
GROUP BY ISBN13)
LIMIT m
