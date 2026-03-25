SET search_path TO modulo2_pgsql;

DO $$
DECLARE
	v_available_stock INTEGER;

BEGIN 
	SELECT Quantity INTO v_available_stock
	FROM products
	WHERE Product_code = 'EB01';

	IF v_available_stock is NULL or v_available_stock < 1 THEN
		RAISE EXCEPTION 'Stock insuficiente. Abortando transaccion.';
	END IF;

	INSERT INTO bills (Bill_id, product_id, user_id, created_at, Status)
	VALUES('F001', 'EB01', 'C002', CURRENT_DATE, 'Pending');

	UPDATE products
	SET Quantity = Quantity - 1
	WHERE Product_code = 'EB01';

	BEGIN

		UPDATE users
		SET last_purchase = CURRENT_DATE
		WHERE User_id = 'C002';

		UPDATE bills
		SET Status = 'Registrada'
		WHERE Bill_id = 'F001';

	EXCEPTION 
		WHEN OTHERS THEN 
			RAISE NOTICE 'Error en la facturacion. Intente nuevamente.';

	END;

	RAISE NOTICE 'Factura creada exitosamente.';

END $$;