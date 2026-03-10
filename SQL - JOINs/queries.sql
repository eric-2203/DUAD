SELECT books.Name, Authors.Name 
    FROM Books AS books
INNER JOIN Authors AS authors
    ON books.author_id = authors.ID;

SELECT books.Name, Authors.Name 
    FROM Books AS books
LEFT JOIN Authors AS authors
    ON books.author_id = authors.ID
WHERE authors.ID IS NULL;

SELECT Authors.Name, Books.Name
    FROM Authors AS authors
LEFT JOIN Books AS books
    ON  authors.ID = books.author_id
WHERE books.author_id IS NULL;

SELECT books.Name, Rents.book_id 
    FROM Books AS books
INNER JOIN Rents AS rents
    ON books.ID = rents.book_id
GROUP BY books.ID;

SELECT books.Name, Rents.book_id 
    FROM Books AS books
LEFT JOIN Rents AS rents
    ON books.ID = rents.book_id
WHERE rents.book_id IS NULL;

SELECT customers.Name, Rents.customer_id 
    FROM Customers AS customers
LEFT JOIN Rents AS rents
    ON Customers.ID = rents.customer_id
WHERE rents.customer_id IS NULL;

SELECT books.Name, Rents.book_id, Rents.State
    FROM Books AS books
INNER JOIN Rents AS rents
    ON books.ID = rents.book_id
WHERE rents.State = "Overdue";