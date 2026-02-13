-- SQLite
INSERT INTO Productos (Codigo, Nombre, Precio, Fecha_de_Ingreso, Marca, Cantidad)
    VALUES ("P01", "Proteina 24g", 45000, "24/12/2025", "GNC", 25);

INSERT INTO Productos (Codigo, Nombre, Precio, Fecha_de_Ingreso, Marca, Cantidad)
    VALUES ("C01", "Creatina", 16000, "26/12/2025", "SAN", 30);

INSERT INTO Productos (Codigo, Nombre, Precio, Fecha_de_Ingreso, Marca, Cantidad)
    VALUES ("M01", "Magnesio", 9000, "30/12/2025", "Alfa", 40);

INSERT INTO Productos (Codigo, Nombre, Precio, Fecha_de_Ingreso, Marca, Cantidad)
    VALUES ("O01", "Omega 3", 9000, "30/12/2025", "Alfa", 40);

INSERT INTO Productos (Codigo, Nombre, Precio, Fecha_de_Ingreso, Marca, Cantidad)
    VALUES ("P02", "Preentreno", 20000, "31/12/2025", "C-4", 15);

INSERT INTO Productos (Codigo, Nombre, Precio, Fecha_de_Ingreso, Marca, Cantidad)
    VALUES ("P03", "Proteina 30g", 55000, "31/12/2025", "Carnivor", 18);

INSERT INTO Productos (Codigo, Nombre, Precio, Fecha_de_Ingreso, Marca, Cantidad)
    VALUES ("P04", "Proteina 25g", 60000, "31/12/2025", "MuscleTech", 22);

INSERT INTO Productos (Codigo, Nombre, Precio, Fecha_de_Ingreso, Marca, Cantidad)
    VALUES ("A01", "Aminoacidos", 25000, "25/12/2025", "SAN", 35);

INSERT INTO Productos (Codigo, Nombre, Precio, Fecha_de_Ingreso, Marca, Cantidad)
    VALUES ("M02", "Multivitaminico", 22000, "10/01/2026", "Animal Pak", 26);

INSERT INTO Empleados (Nombre, Apellidos)
    VALUES ("Juan", "Novoa");

INSERT INTO Empleados (Nombre, Apellidos)
    VALUES ("Kevin", "Prieto");

INSERT INTO Empleados (Nombre, Apellidos)
    VALUES ("Stephen", "Boyer");

INSERT INTO Empleados (Nombre, Apellidos)
    VALUES ("Mitzy", "Hoffman");

INSERT INTO Empleados (Nombre, Apellidos)
    VALUES ("Daniela", "Campos");

INSERT INTO Usuarios (Telefono)
    VALUES ("+50671303490");

INSERT INTO Usuarios (Telefono)
    VALUES ("+50688080428");

INSERT INTO Usuarios (Telefono)
    VALUES ("+50672022778");

INSERT INTO Usuarios (Telefono)
    VALUES ("+50680256398");

INSERT INTO Usuarios (Telefono)
    VALUES ("+50640518796");

INSERT INTO Usuarios (Telefono)
    VALUES ("+50660652125");


INSERT INTO Facturas (Numero_Factura, Fecha_de_Compra, Usuario_id, Monto_Total, Empleado_id)
    VALUES ("F001", "28/12/2025", 2, 65000, 1);

INSERT INTO Facturas (Numero_Factura, Fecha_de_Compra, Usuario_id, Monto_Total, Empleado_id)
    VALUES ("F002", "28/12/2025", 4, 63000, 2);

INSERT INTO Facturas (Numero_Factura, Fecha_de_Compra, Usuario_id, Monto_Total, Empleado_id)
    VALUES ("F003", "30/12/2025", 6, 82000, 3);

INSERT INTO Facturas (Numero_Factura, Fecha_de_Compra, Usuario_id, Monto_Total, Empleado_id)
    VALUES ("F004", "15/01/2026", 4, 75000, 5);

INSERT INTO Facturas (Numero_Factura, Fecha_de_Compra, Usuario_id, Monto_Total, Empleado_id)
    VALUES ("F005", "18/01/2026", 2, 160000, 1);

INSERT INTO Facturas (Numero_Factura, Fecha_de_Compra, Usuario_id, Monto_Total, Empleado_id)
    VALUES ("F006", "30/01/2026", 5, 67000, 4);

INSERT INTO Detalle_Factura (factura_id, producto_id, precio_unitario, cantidad)
    VALUES (1, 1, 45000, 1);

INSERT INTO Detalle_Factura (factura_id, producto_id, precio_unitario, cantidad)
    VALUES (1, 5, 20000, 1);

INSERT INTO Detalle_Factura (factura_id, producto_id, precio_unitario, cantidad)
    VALUES (2, 4, 9000, 2);

INSERT INTO Detalle_Factura (factura_id, producto_id, precio_unitario, cantidad)
    VALUES (2, 5, 20000, 1);

INSERT INTO Detalle_Factura (factura_id, producto_id, precio_unitario, cantidad)
    VALUES (2, 6, 25000, 1);

INSERT INTO Detalle_Factura (factura_id, producto_id, precio_unitario, cantidad)
    VALUES (3, 9, 60000, 1);

INSERT INTO Detalle_Factura (factura_id, producto_id, precio_unitario, cantidad)
    VALUES (3, 7, 22000, 1);

INSERT INTO Detalle_Factura (factura_id, producto_id, precio_unitario, cantidad)
    VALUES (4, 8, 55000, 1);

INSERT INTO Detalle_Factura (factura_id, producto_id, precio_unitario, cantidad)
    VALUES (4, 5, 20000, 1);

INSERT INTO Detalle_Factura (factura_id, producto_id, precio_unitario, cantidad)
    VALUES (5, 1, 45000, 1);

INSERT INTO Detalle_Factura (factura_id, producto_id, precio_unitario, cantidad)
    VALUES (5, 8, 55000, 1);

INSERT INTO Detalle_Factura (factura_id, producto_id, precio_unitario, cantidad)
    VALUES (5, 9, 60000, 2);

INSERT INTO Detalle_Factura (factura_id, producto_id, precio_unitario, cantidad)
    VALUES (6, 8, 55000, 1);

INSERT INTO Detalle_Factura (factura_id, producto_id, precio_unitario, cantidad)
    VALUES (6, 7, 22000, 1);