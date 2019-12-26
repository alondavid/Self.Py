#ex 6.2.3

def format_list(my_list):
    '''
       The function will return even number objects from the list
       divided by ', ' & the last one will contain 'and'
       >>> my_list = ["hydrogen", "helium", "lithium", "beryllium", "boron", "magnesium"] 
       >>> format_list(my_list) 
       hydrogen, lithium, boron, and magnesium
    '''
    return ', '.join(my_list[0::2]) + ', and ' + my_list[-1]
    
