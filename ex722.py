def numbers_letters_count(my_str):
    '''
       Count the digits in a sstring
       :param my_str: A string
       :type my_str: String
       :return: List with the num of digits, and not digits
       :rtype: List
    '''
    count_num = 0
    count_not_num = 0
    for char in my_str:
        if char.isdigit():
            count_num += 1
        else:
            count_not_num += 1
    return [count_num, count_not_num]
