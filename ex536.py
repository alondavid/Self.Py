#ex 536

def fix_age(age):
    '''int > int
       if age = 13/ 14/ 17/ 18/ 19 return 0
       else return age
    '''
    if (age > 12 and age < 15) or (age > 16 and age < 20):
        return 0
    return age
    
def filter_teens(a = 13, b = 13, c = 13):
    '''int, int, int > int
       if a/ b/ c = 13/ 14/ 17/ 18/ 19 > fix_age(int) to 0
       return sum(a,b,c)
       >>> filter_teens() 
       0
       >>> filter_teens(1, 2, 3) 
       6
       >>> filter_teens(2, 13, 1) 
       3
       >>> filter_teens(2, 1, 15) 
       18
    '''
    return fix_age(a) + fix_age(b) + fix_age(c) 
    
