SELECT Nombre, Cantidad
    FROM Productos;

SELECT Nombre, Precio
    FROM Productos
    WHERE Precio > 50000;

SELECT *
    FROM Detalle_Factura
    WHERE producto_id = 5;

SELECT producto_id, precio_unitario, COUNT(id), SUM(precio_unitario)
    FROM Detalle_Factura
    GROUP BY producto_id;

SELECT *
    FROM Facturas
    WHERE Usuario_id = 2;

SELECT *
    FROM Facturas
    ORDER BY Monto_Total DESC;

SELECT *
    FROM Facturas
    WHERE Numero_Factura = "F005";