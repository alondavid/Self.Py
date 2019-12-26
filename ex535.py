#ex 535

def distance(num1, num2, num3):
    '''int,int,int > Bool
       the Function return True if:
         (num2 - num1 or num3 - num1 = abs(1))
          and (num2 - num1 or num2 - num3 or num3 - num1 > abs(2)).
        >>> distance(1, 2, 10)
        True
        >>> distance(4, 5, 3)
        False

    '''
    if (abs(num3 - num1) == 1 or abs(num2 - num1) == 1) and (abs(num2 - num3) > 2 or abs(num2 - num1) > 2 or abs(num3 - num1) > 2):
           return True
    return False
    
