CREATE DATABASE BookStoreProject
USE BookStoreProject


CREATE TABLE User(
userName VARCHAR(32),
loginName VARCHAR(64),
password VARCHAR(32) NOT NULL,
PRIMARY KEY (loginName))


CREATE TABLE Book(
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


CREATE TABLE BookOrder(
loginName VARCHAR(64),
ISBN13 CHAR(14),
quantityOrdered INT NOT NULL,  # QUANTITY ORDERED MUST BE SMALLER OR EQUAL TO QUANTITY AVAILABLE
orderDate DATETIME NOT NULL,
PRIMARY KEY (loginName, ISBN13),
FOREIGN KEY (loginName) REFERENCES User(loginName),
FOREIGN KEY (ISBN13) REFERENCES Book(ISBN13))


CREATE TABLE FeedbackOnBook (
loginName VARCHAR(64),
ISBN13 CHAR(14),
feedbackScore INT NOT NULL,
feedbackText VARCHAR(100),
feedbackDate DATE NOT NULL,
PRIMARY KEY (loginName, ISBN13),
FOREIGN KEY (loginName) REFERENCES User(loginName),
FOREIGN KEY (ISBN13) REFERENCES Book(ISBN13),
CHECK (score >= 0 and score <= 10))



CREATE TABLE RatingFeedback(
loginName VARCHAR(64),
userBeingRated VARCHAR(64) NOT NULL,
ISBN13 CHAR(14),
ratingScore INT NOT NULL,
PRIMARY KEY (loginName,ISBN13,userBeingRated),
FOREIGN KEY (loginName) REFERENCES User(loginName),
FOREIGN KEY (userBeingRated) REFERENCES FeedbackOnBook(loginName),
FOREIGN KEY (ISBN13) REFERENCES FeedbackOnBook(ISBN13),
CHECK (loginName <> userBeingRated),
CHECK (score = 0 or score = 1 or score = 2))





-- NEED TO CREATE A TRIGGER TO UPDATE THE BOOK QUANITY WHEN THERE IS AN ORDER OF THAT BOOK





-- Question 3
SELECT User.*
FROM User
WHERE loginName = "huangwenxin2010@msn.com"


SELECT BookOrder.*, Book.*
FROM BookOrder, Book
WHERE BookOrder.ISBN13 = Book.ISBN13
AND BookOrder.loginName = "..."


SELECT *
FROM FeedbackOnBook
WHERE FeedbackOnBook.loginName = 'liuzhanpeng2011@msn.com'

SELECT FeedbackOnBook.*
FROM FeedbackOnBook, RatingFeeback
WHERE User.loginName = "..."
AND FeedbackOnBook.loginName= RatingFeeback.userBeingRated

-- QUESTION 4

INSERT INTO Book (title,format,pages,language,authors,publisher,bookSubject,year,ISBN10,ISBN13,numberOfCopies)
VALUES (...)

-- QUESTION 5
UPDATE BOOK
SET Book.numberOfCopies = ...
WHERE Book.ISBN13 = "..."

-- QUESTION 6
INSERT INTO FeedbackOnBook (loginName,ISBN13,feedbackScore,feedbackText,feedbackDate)
VALUES (...)

-- QUESTION 7
INSERT INTO RatingFeeback (loginName,ratingScore,userBeingRated,ISBN13)
VALUES (...)

-- QUESTION 8 PART a
SELECT ISBN13, year
FROM Book
WHERE title = "..."
AND/OR authors = "..."
AND/OR publisher = "..."
AND/OR bookSubject = "..."
GROUP BY year

-- QUESTION 8 PART a
SELECT B.ISBN13, AVG(FeedbackOnBook.feedbackScore)
FROM Book B, FeedbackOnBook
WHERE Book.ISBN13 = FeedbackOnBook.ISBN13
AND B.title = "..."
AND/OR B.authors = "..."
AND/OR B.publisher = "..."
AND/OR B.bookSubject = "..."
GROUP BY B.ISBN13

-- QUESTION 9
CREATE VIEW AverageScoreOfFeedback AS
(SELECT userBeingRated, AVG(ratingScore)
FROM RatingFeeback
WHERE ISBN13 = '...'
GROUP BY userBeingRated)

CREATE VIEW userBeingRatedOnly AS
(SELECT userBeingRated
FROM AverageScoreOfFeedback)

SELECT F.loginName, F.feedbackScore, F.feedbackText
FROM userBeingRatedOnly U, FeedbackOnBook F
Where U.userBeingRated = F.loginName
And F.ISBN13 = '...'



-- QUESTION 11
SELECT ISBN13
FROM (SELECT ISBN13, SUM(quantityOrdered)
FROM BookOrder
WHERE orderDate LIKE 'YYYY-MM'
GROUP BY ISBN13)
LIMIT m


SELECT authors
FROM Book
WHERE Book.ISBN13 in (SELECT ISBN13, SUM(quantityOrdered)
                    FROM BookOrder
                    WHERE orderDate LIKE 'YYYY-MM'
                    GROUP BY ISBN13)

SELECT publishers
FROM Book
WHERE Book.ISBN13 in (SELECT ISBN13, SUM(quantityOrdered)
                    FROM BookOrder
                    WHERE orderDate LIKE 'YYYY-MM'
                    GROUP BY ISBN13)
