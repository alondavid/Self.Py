#Ex 7.2.1
def is_greater(my_list, n):
    '''
       Recive a list of numbers and a number
       :param my_list: A list of numbers
       :param n: A number to find numbers that are greater then him
       :type my_list: List
       :type n: Number
       :return: A list of the numbers that are greater then n
       :rtype: List
    '''
    new_list = []
    for number in my_list:
        if number > n:
            new_list.append(number)
    return new_list
