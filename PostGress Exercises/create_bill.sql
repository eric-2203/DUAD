SET search_path TO modulo2_pgsql;

DO $$
DECLARE
	v_available_stock INTEGER;
	u_user_purchasing VARCHAR(50);

BEGIN 
	SELECT quantity INTO v_available_stock
	FROM products_inventory
	WHERE product_code = 'EB01';

	SELECT user_id INTO u_user_purchasing
	FROM users
	WHERE user_id = 'C002';
	

	IF v_available_stock is NULL or v_available_stock < 1 THEN
		RAISE EXCEPTION 'Stock insuficiente. Abortando transaccion.';
	END IF;

	IF u_user_purchasing = '' OR u_user_purchasing IS NULL THEN 
		RAISE EXCEPTION 'El usuario es incorrecto o no existe en la base de datos.';
	END IF;

	INSERT INTO bills (bill_id, product_id, user_id, created_at, quantity_purchased, status)
	VALUES('F001', 'EB01', 'C002', CURRENT_DATE, 5, 'Pending');

	UPDATE products_inventory
	SET quantity = quantity - 5
	WHERE product_code = 'EB01';

	BEGIN

		UPDATE users
		SET last_purchase = CURRENT_DATE
		WHERE user_id = 'C002';

		UPDATE bills
		SET status = 'Registrada'
		WHERE bill_id = 'F001';

	EXCEPTION 
		WHEN OTHERS THEN 
			ROLLBACK;
			RAISE NOTICE 'Error en la facturacion. Intente nuevamente.';

	END;

	RAISE NOTICE 'Factura creada exitosamente.';

END $$;