"""Fifth segment"""
from .data.data_elements import list_elements
from .utilities.operations import convert_bitmap_to_active_bits


class DataElements:
    start_position = 32

    @staticmethod
    def get_element(select):
        return list_elements.elements[select]

    @staticmethod
    def get_all_data_elements(active_elements, data_elements):
        data = [{"Active_elements": active_elements}]
        for i in active_elements:
            # Only support some data elements
            if i <= 14:
                element = DataElements.process_element(DataElements.get_element(i), data_elements)
                data.append(element)
                pass
        return data

    @staticmethod
    def process_element(element, data_elements):
        result = {}
        data = {}
        value = data_elements[element["start_position"]:element["end_position"]]
        data["value"] = value
        if element["bitmap"]:
            data["active_elements"] = convert_bitmap_to_active_bits(bitmap=value,
                                                                    position=65)
        if element["dynamic"]:
            # For implement
            pass
        else:
            pass
        data["data_element"] = element["element"]
        data["description"] = element["description"]
        data["len"] = element["len"]
        data["format"] = element["format"]
        result[str(element["element"])] = data
        return result
