"""ISO 8583 Parser implementation"""

import json
from iso8583_dlib.utilities.operations import hex_to_binary
from iso8583_dlib.utilities.rules import data_elements_rules
from iso8583_dlib.segments.iso import ISO
from iso8583_dlib.segments.header import Header
from iso8583_dlib.segments.mti import MTI
from iso8583_dlib.segments.primary_bitmap import PrimaryBitmap
from iso8583_dlib.segments.data_elements import DataElements


class Parser:
    """Main parser class"""

    def __init__(self, message):
        """Init class require a message as input"""
        # Parser variables
        self.message = message
        self.active_data_elements = []
        self.json_data = None

        # Parser segments
        self.iso = self.message[ISO.start_position:ISO.end_position]  # 3
        self.header = self.message[Header.start_position:Header.end_position]  # 9
        self.mti = self.message[MTI.start_position:MTI.end_position]  # 4
        self.primary_bitmap = self.message[PrimaryBitmap.start_position:PrimaryBitmap.end_position]  # 16
        self.data_elements = self.message[DataElements.start_position:]

        # Parser function
        self.iso_8583()

    def iso_8583(self):
        """Processing data"""

        position = 1
        for element in self.primary_bitmap:
            for bit in hex_to_binary(element):
                if bit == '1':
                    self.active_data_elements.append(position)
                position += 1

        print(self.active_data_elements)
        print('Data Elements')
        # print(self.data_elements)
        print(data_elements_rules()[3])

    def get_json(self):
        """Return json format data"""

        to_convert = {
            "iso": self.iso,
            "header": self.header,
            "mti": MTI.message_types[self.mti],
            "primary_bitmap": self.primary_bitmap,
            "data_elements": self.data_elements
        }
        return json.dumps(to_convert)
