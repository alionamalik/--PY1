src = not False and True or False and not True

# TODO расписать упрощение выражения

# result = True and True or False and False # избавляемся от отрицаний
# result = True or False # избавляемся от "И"
# result = True #избавляемся от "ИЛИ"
result = True

print(src == result)
