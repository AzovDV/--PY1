def delete(list_, index=None):
    list_copy = list_.copy()
    index_ = -1 if index is None else index
    list_copy.pop(index_)
    return list_copy


print(delete([0, 0, 1, 2], index=0))  # [0, 1]
print(delete([0, 1, 1, 2, 3], index=1))  # [0, 1, 2]
print(delete([0, 1, 2, 3, 4, 4]))  # [0, 1, 2, 3]
