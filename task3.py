def delete(list_, index=None):
    ...  # TODO реализовать функцию удаления элемента из списка по индексу
    if index is None:
        index = len(list_)-1
        list1_ = list_[:index]
        return list1_
    else:
        return list_[:index] + list_[index+1:]

print(delete([0, 0, 1, 2], index=0))  # [0, 1]
print(delete([0, 1, 1, 2, 3], index=1))  # [0, 1, 2]
print(delete([0, 1, 2, 3, 4, 4]))  # [0, 1, 2, 3]
