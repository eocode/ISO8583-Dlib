"""Main Parser Class"""

import json
from .segments.utilities.operations import convert_bitmap_to_active_bits
from .segments.iso import ISO
from .segments.header import Header
from .segments.mti import MTI
from .segments.primary_bitmap import PrimaryBitmap
from .segments.data_elements import DataElements


class Parser:
    """Main parser class"""

    def __init__(self, message):
        """Init class require a message as input"""
        # Parser variables
        self.message = message
        self.active_data_elements = []
        self.json_data = None

        # Parser segments
        self.iso = self.message[ISO.start_position:ISO.end_position]
        self.header = self.message[Header.start_position:Header.end_position]
        self.mti = self.message[MTI.start_position:MTI.end_position]
        self.primary_bitmap = self.message[PrimaryBitmap.start_position:PrimaryBitmap.end_position]
        self.data_elements = self.message[DataElements.start_position:]

        # Parser function
        self.iso_8583()

    def iso_8583(self):
        """Processing data"""

        self.active_data_elements = convert_bitmap_to_active_bits(self.primary_bitmap)

    def get_json(self, save=False):
        """Return json format data"""
        print(self.active_data_elements)
        to_convert = {
            "literal": self.iso,
            "header": Header.get_message(self.header),
            "mti": MTI.get_type(self.mti),
            "primary_bitmap": self.primary_bitmap,
            "data_elements": DataElements.get_all_data_elements(self.active_data_elements, self.data_elements)
        }
        if save:
            with open('data.json', 'w', encoding='utf-8') as f:
                json.dump(to_convert, f, ensure_ascii=False, indent=4)

        return json.dumps(to_convert)
