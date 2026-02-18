INSERT INTO Customers(Name, Phone, Address)
    VALUES("Alice", "123-456-7890", "123 Main St");

INSERT INTO Customers(Name, Phone, Address)
    VALUES("Bob","987-654-3210", "456 Elm St");

INSERT INTO Customers(Name, Phone, Address)
    VALUES("Claire", "555-123-4567", "789 Oak St");

INSERT INTO Customers(Name, Phone, Address)
    VALUES("Claire","555-123-4567", "789 Georgia St");

INSERT INTO Items(Name, Price)
    VALUES("Cheeseburger", "$8");

INSERT INTO Items(Name, Price)
    VALUES("Fries", "$3");

INSERT INTO Items(Name, Price)
    VALUES("Pizza", "$12");

INSERT INTO Items(Name, Price)
    VALUES("Salad", "$6");

INSERT INTO Items(Name, Price)
    VALUES("Water", "$1");

INSERT INTO Special_request(Request)
    VALUES("None");

INSERT INTO Special_request(Request)
    VALUES("Extra Ketchup");

INSERT INTO Special_request(Request)
    VALUES("Extra cheese");

INSERT INTO Special_request(Request)
    VALUES("No croutons");

INSERT INTO Special_request(Request)
    VALUES("No onions");

INSERT INTO Delivery_times(Time)
    VALUES("12:00 pm");

INSERT INTO Delivery_times(Time)
    VALUES("5:00 pm");

INSERT INTO Delivery_times(Time)
    VALUES("6:00 pm");

INSERT INTO Delivery_times(Time)
    VALUES("7:30 pm");

INSERT INTO Delivery_times(Time)
    VALUES("8:00 pm");

INSERT INTO Ordenes(customer_id, item_id, Quantity, special_request_id, delivery_time_id)
    VALUES(1, 1, 2, 5, 3);

INSERT INTO Ordenes(customer_id, item_id, Quantity, special_request_id, delivery_time_id)
    VALUES(1, 2, 1, 2, 3);

INSERT INTO Ordenes(customer_id, item_id, Quantity, special_request_id, delivery_time_id)
    VALUES(2, 3, 1, 3, 4);

INSERT INTO Ordenes(customer_id, item_id, Quantity, special_request_id, delivery_time_id)
    VALUES(2, 2, 2, 1, 4);

INSERT INTO Ordenes(customer_id, item_id, Quantity, special_request_id, delivery_time_id)
    VALUES(3, 4, 1, 4, 1);

INSERT INTO Ordenes(customer_id, item_id, Quantity, special_request_id, delivery_time_id)
    VALUES(4, 5, 1, 1, 2);