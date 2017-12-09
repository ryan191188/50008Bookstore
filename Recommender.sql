SELECT ISBN13 FROM myapp_orders
WHERE loginName IN
(SELECT b2.loginName 
FROM myapp_orders b1, myapp_orders b2
WHERE b1.ISBN13 = b2.ISBN13
AND b1.loginName <> b2.loginName
AND b1.loginName = 'tayweiguo1989@msn.com'
AND b1.ISBN13 = '978-1594487712')
AND ISBN13 <> '978-1594487712'
GROUP BY ISBN13
ORDER BY COUNT(ISBN13) DESC;
