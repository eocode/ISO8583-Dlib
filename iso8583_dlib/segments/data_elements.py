"""Fifth segment"""
from iso8583_dlib.segments.read_metadata_segments import read_json_to_dictionary


class DataElements:
    start_position = 32

    @staticmethod
    def get_element(select):
        return read_json_to_dictionary(r'\data\data_elements\list_elements.json')[select]

    @staticmethod
    def get_all_data_elements(active_elements, data_elements):
        data = []
        for i in active_elements:
            if i <= 7:
                data.append(DataElements.get_element(str(i)))
                pass
        return data
