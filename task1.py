# TODO решить с помощью list comprehension и распечатать его
from pprint import pprint
list_dict = [{'dec': n, 'bin': bin(n), 'oct': oct(n), 'hex': hex(n)} for n in range(16)]
pprint(list_dict)