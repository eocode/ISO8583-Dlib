"""Third segment"""
from .data.mti import mti_types


class MTI:
    start_position = 12
    end_position = 16

    @staticmethod
    def get_type(select):
        return mti_types.types[select]
