#Ex 6.3.2

def longest(my_list):
    '''
       Find the longest string in a list
       :param my_list: A list of strings
       :type my_list: List
       :return: The longest string
       :rtype: string
    '''
    return sorted(my_list, key=len)[-1]
    
    
