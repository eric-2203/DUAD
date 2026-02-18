CREATE TABLE Customers (
    id INTEGER PRIMARY KEY,
    Name VARCHAR(10) NOT NULL,
    Phone VARCHAR(12) NOT NULL,
    Adress VARCHAR(20)
);

CREATE TABLE Items (
    id INTEGER PRIMARY KEY,
    Name VARCHAR(15) NOT NULL,
    Price VARCHAR(10) NOT NULL
);

CREATE TABLE Special_request (
    id INTEGER PRIMARY KEY,
    Request VARCHAR(15) NOT NULL
);

CREATE TABLE Delivery_times (
    id INTEGER PRIMARY KEY,
    Time VARCHAR(8) NOT NULL
);

CREATE TABLE Ordenes (
    id INTEGER PRIMARY KEY,
    customer_id INT REFERENCES Customers(id),
    item_id INT REFERENCES Items(id),
    Quantity INT NOT NULL,
    special_request_id INT REFERENCES Special_request(id),
    delivery_time_id INT REFERENCES Delivery_times(id)
);