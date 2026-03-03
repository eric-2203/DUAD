
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
    Name VARCHAR(15) NOT NULL,
    company_id INT REFERENCES Insurance_Companies(id)
);

CREATE TABLE Automoviles(
    id INTEGER PRIMARY KEY,
    VIN VARCHAR(12) NOT NULL,
    make_id INT REFERENCES Makes(id),
    model_id INT REFERENCES Models(id),
    color_id INT REFERENCES Colors(id),
    owner_id INT REFERENCES Owners(id),
    policy_id INT REFERENCES Policies(id)
);

CREATE TABLE Colors(
    id INTEGER PRIMARY KEY,
    Name VARCHAR(12) NOT NULL
);