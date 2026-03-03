INSERT INTO Customers(Name, Phone)
    VALUES("Alice", "123-456-7890");

INSERT INTO Customers(Name, Phone)
    VALUES("Bob","987-654-3210");

INSERT INTO Customers(Name, Phone)
    VALUES("Claire", "555-123-4567");

INSERT INTO Customers(Name, Phone)
    VALUES("Claire","555-123-4567");

INSERT INTO Addresses(Address, customer_id)
    VALUES("123 Main St", 1);

INSERT INTO Addresses(Address, customer_id)
    VALUES("456 Elm St", 2);

INSERT INTO Addresses(Address, customer_id)
    VALUES("789 Oak St", 3);

INSERT INTO Addresses(Address, customer_id)
    VALUES("789 Georgia St", 3);

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

INSERT INTO Ordenes(customer_id, address_id, item_id, Quantity, special_request_id, Delivery_Time)
    VALUES(1, 1, 1, 2, 5, "6:00 pm");

INSERT INTO Ordenes(customer_id, address_id, item_id, Quantity, special_request_id, Delivery_Time)
    VALUES(1, 1, 2, 1, 2, "6:00 pm");

INSERT INTO Ordenes(customer_id, address_id, item_id, Quantity, special_request_id, Delivery_Time)
    VALUES(2, 2, 3, 1, 3, "7:30 pm");

INSERT INTO Ordenes(customer_id, address_id, item_id, Quantity, special_request_id, Delivery_Time)
    VALUES(2, 2, 2, 2, 1, "7:30 pm");

INSERT INTO Ordenes(customer_id, address_id, item_id, Quantity, special_request_id, Delivery_Time)
    VALUES(3, 3, 4, 1, 4, "12:00 pm");

INSERT INTO Ordenes(customer_id, address_id, item_id, Quantity, special_request_id, Delivery_Time)
    VALUES(3, 4, 5, 1, 1, "5:00 pm");