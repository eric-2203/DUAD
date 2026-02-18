CREATE TABLE VINs(
    id INTEGER PRIMARY KEY,
    VIN VARCHAR(11) NOT NULL
);

CREATE TABLE Makes(
    id INTEGER PRIMARY KEY,
    Name VARCHAR(15)
);

CREATE TABLE Models(
    id INTEGER PRIMARY KEY,
    Name VARCHAR(8),
    Year INT NOT NULL
);

CREATE TABLE Owners(
    id INTEGER PRIMARY KEY,
    Name VARCHAR(15) NOT NULL,
    Phone VARCHAR(12) NOT NULL
);

CREATE TABLE Insurance_Companies(
    id INTEGER PRIMARY KEY,
    Name VARCHAR(15) NOT NULL
);

CREATE TABLE Policies(
    id INTEGER PRIMARY KEY,
    Name VARCHAR(15) NOT NULL
);

CREATE TABLE Automoviles(
    id INTEGER PRIMARY KEY,
    vin_id INT REFERENCES VINs(id),
    make_id INT REFERENCES Makes(id),
    model_id INT REFERENCES Models(id),
    color_id INT REFERENCES Colors(id),
    owner_id INT REFERENCES Owners(id),
    insurance_id INT REFERENCES Insurance_Companies(id),
    policy_id INT REFERENCES Policies(id)
);

CREATE TABLE Colors(
    id INTEGER PRIMARY KEY,
    Name VARCHAR(12) NOT NULL
);