INSERT INTO Authors(Name)
    VALUES("Miguel de Cervantes");

INSERT INTO Authors(Name)
    VALUES("Dante Alighieri");

INSERT INTO Authors(Name)
    VALUES("Takehiko Inoue");

INSERT INTO Authors(Name)
    VALUES("Akira Toriyama");

INSERT INTO Authors(Name)
    VALUES("Walt Disney");

INSERT INTO Books(Name, author_id)
    VALUES("Don Quijote" , 1);

INSERT INTO Books(Name, author_id)
    VALUES("La Divina Comedia" , 2);

INSERT INTO Books(Name, author_id)
    VALUES("Vagabond 1-3" , 3);

INSERT INTO Books(Name, author_id)
    VALUES("Dragon Ball 1" , 4);

INSERT INTO Books(Name)
    VALUES("The Book of the 5 Rings");

INSERT INTO Customers(Name, Email)
    VALUES("John Doe", "j.doe@email.com");

INSERT INTO Customers(Name, Email)
    VALUES("Jane Doe", "jane@doe.com");

INSERT INTO Customers(Name, Email)
    VALUES("Luke Skywalker", "darth.son@email.com");

INSERT INTO Rents(book_id, customer_id, State)
    VALUES(1, 2, "Returned");

INSERT INTO Rents(book_id, customer_id, State)
    VALUES(2, 2, "Returned");

INSERT INTO Rents(book_id, customer_id, State)
    VALUES(1, 1, "On time");

INSERT INTO Rents(book_id, customer_id, State)
    VALUES(3, 1, "On time");

INSERT INTO Rents(book_id, customer_id, State)
    VALUES(2, 2, "Overdue");