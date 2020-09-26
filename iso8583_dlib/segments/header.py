"""Second segment"""

from .data.header import header_PI, header_RN, header_Status, header_OC, header_RC


class Header:
    start_position = 3
    end_position = 12

    @staticmethod
    def get_header_pi(select):
        return header_PI.pi[select]

    @staticmethod
    def get_header_rn(select):
        return header_RN.rn[select]

    @staticmethod
    def get_header_status(select):
        return header_Status.status[select]

    @staticmethod
    def get_header_oc(select):
        print(select)
        return header_OC.oc[select]

    @staticmethod
    def get_header_rc(select):
        return header_RC.rc[select]

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
