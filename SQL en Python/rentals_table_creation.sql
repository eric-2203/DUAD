SET search_path TO lyfter_car_rental;

CREATE TABLE rentals(
	ID SERIAL  PRIMARY KEY,
	user_id INT REFERENCES users(id),
	car_id INT REFERENCES cars(id),
	rent_date DATE DEFAULT CURRENT_DATE,
	rent_status VARCHAR(12) DEFAULT 'pending' NOT NULL
);