SET search_path TO modulo2_pgsql;

CREATE TABLE users (
    user_id VARCHAR(50) PRIMARY KEY,
    user_name VARCHAR(25),
	last_purchase DATE
);

CREATE TABLE products_inventory (
    product_code VARCHAR(4) PRIMARY KEY,
    product_name VARCHAR(50) NOT NULL,
	quantity INTEGER CHECK (Quantity >= 0)
);

CREATE TABLE bills (
    bill_id VARCHAR(50) PRIMARY KEY,
	product_id VARCHAR(4) REFERENCES products_inventory(Product_code),
    user_id VARCHAR(50) REFERENCES users(User_id),
	created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
	quantity_purchased INT NOT NULL,
	status VARCHAR(15) NOT NULL
);