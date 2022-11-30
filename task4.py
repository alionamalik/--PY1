import json

INPUT_FILE = "input.csv"


def csv_to_list_dict(filename) -> list[dict]:
 #TODO реализовать конвертер из csv в json
    list_dict = []
    values = []
    with open(filename, 'r') as f:
        headers = f.readline().rstrip().split(sep=',')
        for row in f:
            values.append(row.rstrip().split(sep=','))
            print(list_dict)
        for element in values:
            dict_element = dict(zip(headers, element))
            list_dict.append(dict_element)

    return list_dict


csv_to_list_dict(INPUT_FILE)
print(json.dumps(csv_to_list_dict(INPUT_FILE), indent=4))
