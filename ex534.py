#ex 534
# Return true if the last char appered in the str earlier
#
def last_early(my_str):
    ''' str -> bool
    Return true if the last char appered in the str earlier
    >>> last_early("happy birthday") 
    True 
    >>> last_early("best of luck") 
    False 
    >>> last_early("Wow") 
    True 
    >>> last_early("X") 
    False
    '''
    char_to_test = my_str[-1]
    num_of_appearences = my_str.lower().count(char_to_test)
    if num_of_appearences > 1:
        return True
    return False
    
