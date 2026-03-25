SET search_path TO modulo2_pgsql;

CREATE TABLE Users (
    User_id VARCHAR(50) PRIMARY KEY,
    Name VARCHAR(25),
	last_purchase DATE
);

CREATE TABLE Products (
    Product_code VARCHAR(4) PRIMARY KEY,
    Product_name VARCHAR(50) NOT NULL,
	Quantity INTEGER CHECK (Quantity >= 0)
);

CREATE TABLE Bills (
    Bill_id VARCHAR(50) PRIMARY KEY,
	product_id VARCHAR(4) REFERENCES Products(Product_code),
    user_id VARCHAR(50) REFERENCES Users(User_id),
	created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
	Status VARCHAR(15) NOT NULL
);