def data_elements_rules():
    return {
        1: {
            "dynamic": False,
            "len": 16,
            "format": 'AN',
            "start_position": 0,
            "end_position": 16,
        },
        3: {
            "dynamic": False,
            "len": 6,
            "format": 'N',
            "start_position": 16,
            "end_position": 22,
        },
        4: {
            "dynamic": False,
            "len": 12,
            "format": 'N',
            "start_position": 22,
            "end_position": 34,
        },
        7: {
            "dynamic": False,
            "len": 10,
            "format": 'N',
            "start_position": 22,
            "end_position": 34,
        }
    }
