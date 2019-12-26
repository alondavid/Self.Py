#Ex 8.3.3
def count_chars(my_str):
    my_dict = {}
    for char in my_str:
        if not char.isalpha():
            continue
        if char in my_dict.keys():
            my_dict[char] += 1
        else:
            my_dict[char] = 1
    return my_dict
