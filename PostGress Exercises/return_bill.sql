SET search_path TO modulo2_pgsql;

DO $$
DECLARE
	existing_bill VARCHAR(50);

BEGIN 
	SELECT Bill_id INTO existing_bill
	FROM bills
	WHERE Bill_id = 'F001';

	IF existing_bill is NULL THEN
		RAISE EXCEPTION 'Factura invalida. Ingrese una factura valida.';
	END IF;

	UPDATE products
	SET Quantity = Quantity + 1
	WHERE Product_code = 'EB01';

	BEGIN 
		UPDATE bills
		SET Status = 'Retornada'
		WHERE Bill_id = 'F001';

	EXCEPTION 
		WHEN OTHERS THEN 
			RAISE NOTICE 'Hubo un error en el proceso. Vuelva a intentarlo.';

	END;

	RAISE NOTICE 'Factura retornada exitosamente.';

END $$;