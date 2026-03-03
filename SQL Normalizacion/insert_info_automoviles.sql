INSERT INTO Makes(Name)
    VALUES("Honda");

INSERT INTO Makes(Name)
    VALUES("Chevrolet");

INSERT INTO Models(Name, Year)
    VALUES("Accord", 2003);

INSERT INTO Models(Name, Year)
    VALUES("CR-V", 2014);

INSERT INTO Models(Name, Year)
    VALUES("Volt", 2015);

INSERT INTO Colors(Name)
    VALUES("Silver");

INSERT INTO Colors(Name)
    VALUES("Blue");

INSERT INTO Colors(Name)
    VALUES("Red");

INSERT INTO Owners(Name, Phone)
    VALUES("Alice", "123-456-7890");

INSERT INTO Owners(Name, Phone)
    VALUES("Bob", "987-654-3210");

INSERT INTO Owners(Name, Phone)
    VALUES("Claire", "555-123-4567");

INSERT INTO Owners(Name, Phone)
    VALUES("Dave", "111-222-3333");

INSERT INTO Insurance_Companies(Name)
    VALUES("ABC Insurance");

INSERT INTO Insurance_Companies(Name)
    VALUES("XYZ Insurance");

INSERT INTO Insurance_Companies(Name)
    VALUES("DEF Insurance");

INSERT INTO Insurance_Companies(Name)
    VALUES("GHI Insurance");

INSERT INTO Policies(Name, company_id)
    VALUES("POL12345", 1);

INSERT INTO Policies(Name, company_id)
    VALUES("POL54321", 2);

INSERT INTO Policies(Name, company_id)
    VALUES("POL67890", 3);

INSERT INTO Policies(Name, company_id)
    VALUES("POL98765", 4);

INSERT INTO Automoviles(VIN, make_id, model_id, color_id, owner_id, policy_id)
    VALUES("1HGCM82633A", 1, 1, 1, 1, 1);

INSERT INTO Automoviles(VIN, make_id, model_id, color_id, owner_id, policy_id)
    VALUES("1HGCM82633A", 1, 1, 1, 2, 2);

INSERT INTO Automoviles(VIN, make_id, model_id, color_id, owner_id, policy_id)
    VALUES("5J6RM4H79EL", 1, 2, 2, 3, 3);

INSERT INTO Automoviles(VIN, make_id, model_id, color_id, owner_id, policy_id)
    VALUES("1G1RA6H1FU", 2, 3, 3, 4, 4);