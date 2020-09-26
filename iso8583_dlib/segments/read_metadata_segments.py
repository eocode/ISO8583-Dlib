"""Read metadata segments"""
import json
import pkgutil


def read_json_to_dictionary(path):
    file = 'iso8583_dlib/segments/' + path
    try:
        f = open(file, 'r')
        data = json.load(f)
        f.close()
        return data
    except NameError:
        print("Error: ", NameError)
        return {}
