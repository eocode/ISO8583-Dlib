class MTI:
    start_position = 12
    end_position = 16
    message_types = {
        "0200": {
            "value": "0200",
            "description": "Financial transaction request"
        },
        "0210": {
            "value": "0210",
            "description": "Financial Transaction Request Response"
        },
        "0400": {
            "value": "0400",
            "description": "Petición de reverso (para revertir una operación 0200 previa)"
        },
        "0410": {
            "value": "0410",
            "description": "Respuesta de reverso"
        },
        "0600": {
            "value": "0600",
            "description": "Una consulta (por ejemplo de saldo o de una operación previa)"
        },
        "0610": {
            "value": "0610",
            "description": "Respuesta de consulta"
        },
        "0800": {
            "value": "0800",
            "description": "Petición de eco (para mantener viva una conexión y asegurarse que el otro lado de la conexión sigue respondiendo)"
        },
        "0810": {
            "value": "0810",
            "description": "Respuesta de eco"
        },
    }
