#ex 6.1.2
def shift_left(my_list):
    '''
       The function recieve a list and return a new list shifted 1
       position to the left
       :param my_list: original list
       :type my_list: list
       :return: a new list, shifted to the left
       :rtype: a list
    '''
    if len(my_list) > 1:
        return my_list[1:] + [new_list[0]]
    else:
        return my_list
