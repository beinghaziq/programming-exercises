def list_converter(my_list):
    my_hash = {'REQUIRED': [], 'OPTIONAL': []}
    my_hash_1 = {'REQUIRED': [], 'OPTIONAL': []}
    for value, key in my_list:
        if (key == 'OPTIONAL' and value in my_hash['REQUIRED']) or value.lower() in my_hash_1[key]:
            continue
        else:
            if key == 'REQUIRED' and value in my_hash['OPTIONAL']:
                my_hash['OPTIONAL'].remove(value)
            my_hash[key].append(value)
            my_hash_1[key].append(value.lower())

    return my_hash
    

print(list_converter([
    ['aBc@example.com', 'OPTIONAL'],
    ['sdsd@example.com', 'OPTIONAL'],
    ['xyz@example.com', 'REQUIRED'],
    ['ops@example.com', 'OPTIONAL'],
    ['ops@example.com', 'REQUIRED'],
    ['abc@example.com', 'REQUIRED']]))
