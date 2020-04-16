#ex 5.3.7
def chocolate_maker(small, big, x):
    ''' int, int, int > bool
    We recieve Small cubes of chocolate (1 cm), Big cubes (5cm) and requested
    length in centimeters.
    we return true if we can create the requested length with the cubes we have
    >>> chocolate_maker(3, 1, 8) 
    True
    >>> chocolate_maker(3, 1, 9) 
    False
    >>> chocolate_maker(3, 2, 10) 
    True
    '''
    large = 5

    num_of_big = x // large
    num_of_small = x % large
    if num_of_big <= big and num_of_small <= small:
        return True
    return False
