def is_greater(my_list, n):
    lst = []
    for num in my_list:
        if num > n:
            lst += [num]
    return lst
