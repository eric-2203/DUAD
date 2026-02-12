#Crear tablas

CREATE TABLE Usuarios (
    id INTEGER PRIMARY KEY,
    Telefono VARCHAR(25) NOT NULL
);

CREATE TABLE Empleados (
    id INTEGER PRIMARY KEY,
    Nombre VARCHAR(25) NOT NULL,
    Apellidos VARCHAR(25) NOT NULL
);

CREATE TABLE Productos (
    id INTEGER PRIMARY KEY,
    Codigo VARCHAR(3) NOT NULL,
    Nombre VARCHAR(25) NOT NULL,
    Precio INT NOT NULL,
    Fecha_de_Ingreso VARCHAR(10) NOT NULL,
    Marca VARCHAR(25) NOT NULL
);

CREATE TABLE Facturas (
    id INTEGER PRIMARY KEY,
    Numero_Factura VARCHAR(10) NOT NULL,
    Fecha_de_Compra VARCHAR(10) NOT NULL,
    Usuario_id INT REFERENCES Usuarios(id),
    Monto_Total INT DEFAULT 0,
    Empleado_id INT REFERENCES Empleados(id)
);

CREATE TABLE Detalle_Factura (
    id INTEGER PRIMARY KEY,
    factura_id INT REFERENCES Facturas(id),
    producto_id INT REFERENCES Productos(id),
    precio_unitario INTEGER NOT NULL,
    cantidad INTEGER NOT NULL
);

