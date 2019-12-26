#ex 8.2.3

def mult_tuple(tuple1, tuple2):
    list_of_tuples = []
    for item in tuple1:
        for item2 in tuple2:
            if (item, item2) not in list_of_tuples:
                list_of_tuples += [(item, item2)]
            if (item2, item) not in list_of_tuples:
                list_of_tuples += [(item2, item)]
    return list_of_tuples
