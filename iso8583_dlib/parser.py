import json
from iso8583_dlib.utilities.operations import hex_to_binary
from iso8583_dlib.utilities.rules import data_elements_rules


class Parser:

    def __init__(self, message):
        self.message = message
        self.active_data_elements = []

        self.iso = self.message[:3]  # 3
        self.header = self.message[3:12]  # 9
        self.mti = self.message[12:16]  # 4
        self.primary_bitmap = self.message[16:32]  # 16
        self.data_elements = self.message[32:]

    def iso_8583(self):

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
