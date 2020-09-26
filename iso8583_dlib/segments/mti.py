"""Third segment"""
from .read_metadata_segments import read_json_to_dictionary


class MTI:
    start_position = 12
    end_position = 16

    @staticmethod
    def get_type(select):
        return read_json_to_dictionary(r'data\mti\mti_types.json')[select]
