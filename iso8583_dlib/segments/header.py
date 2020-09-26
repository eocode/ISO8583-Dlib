"""Second segment"""

from .read_metadata_segments import read_json_to_dictionary


class Header:
    start_position = 3
    end_position = 12

    @staticmethod
    def get_header_pi(select):
        return read_json_to_dictionary(r'data\header\header_PI.json')[select]

    @staticmethod
    def get_header_rn(select):
        return read_json_to_dictionary(r'data\header\header_RN.json')[select]

    @staticmethod
    def get_header_status(select):
        return read_json_to_dictionary(r'data\header\header_Status.json')[select]

    @staticmethod
    def get_header_oc(select):
        return read_json_to_dictionary(r'data\header\header_OC.json')[select]

    @staticmethod
    def get_header_rc(select):
        return read_json_to_dictionary(r'data\header\header_RC.json')[select]

    @staticmethod
    def get_message(header):
        return {
            "Complete_header": header,
            "Product_indicator": Header.get_header_pi(header[0:2]),
            "Release_number": Header.get_header_rn(header[2:4]),
            "Status": Header.get_header_status(header[4:7]),
            "Originator_code": Header.get_header_oc(header[7:8]),
            "Responder_code": Header.get_header_rc(header[8:9]),
        }
