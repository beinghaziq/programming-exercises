def flatten(array):
    flatten_array = []
    for element in array:
        if (isinstance(element, list)):
            flatten_array.extend(flatten(element))
        else:
            if not isinstance(element, str):
                flatten_array.append(element)
    return flatten_array

nested_list = [1, 2, [3, [4], 5, "6"], 6]
print(sum(flatten(nested_list)))
print(sum(flatten([])))
