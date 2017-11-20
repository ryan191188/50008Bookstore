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
CREATE TRIGGER update_qty AFTER INSERT ON bookorder 
	FOR EACH ROW 
		UPDATE book SET numberOfCopies = numberOfCopies - NEW.quantityOrdered
        WHERE ISBN13 = NEW.ISBN13
#DROP TRIGGER IF EXISTS update_qty


-- Question 3
SELECT User.*
FROM User
WHERE loginName = "huangwenxin2010@msn.com"


SELECT BookOrder.*, Book.*
FROM BookOrder, Book
WHERE BookOrder.ISBN13 = Book.ISBN13
AND BookOrder.loginName = "anupamaanghan2010@yahoo.com"

#alternative - Ryan (remove ISBN13 & numberOfCopies)
/*
SELECT BookOrder.*,
Book.title, Book.format, Book.pages, Book.language,
Book.authors, Book.publisher, Book.bookSubject, Book.ISBN10
FROM BookOrder, Book
WHERE BookOrder.ISBN13 = Book.ISBN13
AND BookOrder.loginName = "anupamaanghan2010@yahoo.com"
*/

SELECT *
FROM FeedbackOnBook
WHERE FeedbackOnBook.loginName = 'anupamaanghan2010@yahoo.com'

SELECT RatingFeedback.loginName as PersonWhoRates,RatingFeedback.ratingScore, FeedbackOnBook.*
FROM FeedbackOnBook, RatingFeedback
WHERE RatingFeedback.loginName = "anupamaanghan2010@yahoo.com"
AND FeedbackOnBook.loginName= RatingFeedback.userBeingRated

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
SELECT ISBN13, title, Book.year
FROM Book
WHERE -- title = "A Beginner s Guide to Constructing the Universe: The Mathematical Archetypes of Nature, Art, and Science"
-- AND/OR authors = "Shon Harris"
-- AND/OR publisher = "..."
bookSubject = "Mathematics"
ORDER BY Book.year

-- QUESTION 8 PART b
SELECT B.ISBN13, AVG(FeedbackOnBook.feedbackScore)
FROM Book B, FeedbackOnBook
WHERE B.ISBN13 = FeedbackOnBook.ISBN13
-- AND B.title = "..."
-- AND/OR B.authors = "..."
-- AND/OR B.publisher = "..."
AND B.bookSubject = "Mathematics"
GROUP BY B.ISBN13

-- QUESTION 9
select F.*
From FeedbackOnBook F, (select T.userBeingrated,T.ISBN13,avg(T.ratingScore)
						from (select R.*
							From FeedbackOnbook F, ratingFeedback R
							Where F.ISBN13 = R.ISBN13) as T
						where T.ISBN13 = '978-0735627086'
						group by T.userBeingRated
						DESC
						limit 5) as T2
where F.loginName = T2.userBeingRated
And F.ISBN13 = T2.ISBN13



-- QUESTION 11
SELECT T3.ISBN13
FROM (SELECT ISBN13, SUM(quantityOrdered) AS totalQuantitySold
FROM BookOrder
WHERE orderDate like '2017-01%'
GROUP BY ISBN13
ORDER BY totalQuantitySold
DESC ) as T3
LIMIT 5


SELECT authors
FROM Book
WHERE Book.ISBN13 in (SELECT T4.ISBN13
					FROM (SELECT ISBN13, SUM(quantityOrdered) AS totalQuantitySold
                    FROM BookOrder
                    WHERE orderDate LIKE '2017-01%'
                    GROUP BY ISBN13
                    ORDER BY totalQuantitySold DESC) AS T4)
LIMIT 2



SELECT publisher
FROM Book
WHERE Book.ISBN13 in (SELECT T5.ISBN13
					FROM (SELECT ISBN13, SUM(quantityOrdered) AS totalQuantitySold
                    FROM BookOrder
                    WHERE orderDate LIKE '2017-01%'
                    GROUP BY ISBN13
                    ORDER BY totalQuantitySold DESC) AS T5)
LIMIT 2