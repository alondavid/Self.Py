#Ex 8.3.4

def inverse_dict(my_dict):
    '''
      Recieve a Dictionary and return a reversed version.
      :param my_dict: A dictionary to reverse
      :type my_dict: Dictionary
      :return rev_dict: Dictionary with my_dict.keys as values and vice versa
      :rtype: Dictionary
    '''
    rev_dict = {}
    for key,value in my_dict.items():
        if value in rev_dict.keys():
            rev_dict[value].append(key)
        else:
            rev_dict[value] = [key]
    return rev_dict
