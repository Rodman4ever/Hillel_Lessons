from typing import Any

import requests

import MSG
import files
import pprint
import string

# import statistics
#
# n = statistics.mean([6, 6, 0])
# print(n)

URLs = (
    'https://script.google.com/macros/s/AKfycbxz5kcXERFg18yv0-' \
    'G5EGevFXYdfMKi4WKWnHTZzQuyJ_lTpzeJLUTFZzHJOOK4n0MOtA/exec',
    'https://script.google.com/macros/s/AKfycbxz5kcXERFg18yv0-' \
    'G5EGevFXYdfMKi4WKWnHTZzQuyJ_lTpzeJLUTFZzHJOOK4n0MOtA/exec',
    # 'https://dummyjson.com/products',
)


def get_data(url: str = None) -> dict:
    """
    get data from given url
    :param url: str
    :return: dict
    """

    response = requests.get(url)
    data = response.json()

    return data


def is_valid_length(string: str, length: int = 160) -> bool:
    """

    :param string:
    :param length: >0
    :return:
    """
    if len(string) <= length:
        return True
    return False


def is_string(string: Any) -> bool:
    """
    Args:
        string (Any):
    Returns:
        (True|False):
    """
    if type(string) == str:
        return True
    return False


my_func = {
    1: lambda string, length: string * length,
    2: is_valid_length,
    3: print,
}


def main_google(google_api_url) -> bool:
    google_data = get_data(google_api_url)['data']
    for dictionary in google_data:
        obj_to_validate = dictionary['code']
        if is_string(obj_to_validate):
            continue

        files.work_with_files_append(data=MSG.MSG_INVALID_DICT.format(dictionary, dictionary) + '\n')

        return False
    return True


if __name__ == '__main__':
    assert type(get_data('http://api.open-notify.org/astros.json')) == dict, MSG.MSG_NOT_DICT
    # print(get_data('http://api.open-notify.org/astros.json'))
    assert is_valid_length('dad')
    assert is_valid_length('*' * 190) is False
    assert is_valid_length('*' * 190, 56) is False

    assert is_string('mhdvg')
    assert is_string(5656) is False

if __name__ == '__main__':
    # data = get_data(URLs[0])
    # pprint.pprint(data)
    # pprint.pprint(get_data(URL_DUMMY))

    print(my_func[1]())

    for url in URLs:
        main_google(url)

    print(my_func[1]())

    # result = my_func[1]('fhgg', 2)
    # result2 = my_func[2]('fhgg', 2)
    # print(result)
    # print(result2)
