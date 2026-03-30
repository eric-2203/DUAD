SET search_path TO modulo2_pgsql;

DO $$
DECLARE
	existing_bill VARCHAR(50);
	bill_status VARCHAR(15);
	items_purchased INT;

BEGIN 
	SELECT bill_id INTO existing_bill
	FROM bills
	WHERE bill_id = 'F001';

	SELECT Status INTO bill_status
	FROM bills
	WHERE bill_id = 'F001';

	SELECT quantity_purchased INTO items_purchased
	FROM bills
	WHERE bill_id = 'F001';

	IF existing_bill = '' OR existing_bill IS NULL THEN
		RAISE EXCEPTION 'Factura invalida. Ingrese una factura valida.';
	END IF;

	IF bill_status = 'Retornada' THEN
		RAISE EXCEPTION 'Esta factura ya fue retornada.';
	END IF;

	UPDATE products_inventory
	SET quantity = quantity + items_purchased
	WHERE product_code = 'EB01';

	BEGIN 
		UPDATE bills
		SET status = 'Retornada'
		WHERE bill_id = 'F001';

	EXCEPTION 
		WHEN OTHERS THEN
			ROLLBACK;
			RAISE NOTICE 'Hubo un error en el proceso. Vuelva a intentarlo.';

	END;

	RAISE NOTICE 'Factura retornada exitosamente.';

END $$;