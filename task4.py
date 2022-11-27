import json

INPUT_FILE = "input.csv"


def csv_to_list_dict(filename) -> list[dict]:
 #TODO реализовать конвертер из csv в json
    list_dict = []
    values = []
    with open(filename, 'r') as f:
        list_ = f.readlines()
        headers = list_[0].rstrip().split(sep=',')
        for row in list_[1:]:
            values.append(row.rstrip().split(sep=','))
    for element in values:
        dict_element = dict(zip(headers, element))
        list_dict.append(dict_element)

    return list_dict


csv_to_list_dict(INPUT_FILE)
print(json.dumps(csv_to_list_dict(INPUT_FILE), indent=4))
