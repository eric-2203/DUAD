my_first_dictionary = [
     {
        "nombre": "Eric's Hotel",
        "numero_de_estrellas": 5,
        "cantidad_de_habitaciones": 6,
        "cantidad_de_pisos": 2,
        "habitaciones": [
            {
                "numero": 1,
                "piso": 1,
                "precio_por_noche": "$25",
            },
            {
                "numero": 2,
                "piso": 1,
                "precio_por_noche": "$35",
            },
            {
                "numero": 3,
                "piso": 1,
                "precio_por_noche": "$45",
            },
            {
                "numero": 4,
                "piso": 1,
                "precio_por_noche": "$55",
            },
            {
                "numero": 5,
                "piso": 1,
                "precio_por_noche": "$65",
            },
            {
                "numero": 6,
                "piso": 2,
                "precio_por_noche": "$130",
            },
        ],
        
    },
]
print(my_first_dictionary[0]["habitaciones"][4])
