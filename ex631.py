#ex 6.3.1
def are_lists_equal(list1, list2):
    '''
       Recieve lists of int/float numbers and return True
       if the lists are the same.
       :param list1: list of numbers
       :param list2: list of numbers
       :type list1: List
       :type list2: List
       :return: Comparison between 2 lists
       :rtype: Bool
    '''
    if sorted(list1) == sorted(list2):
        return True
    return False

def main():
    list1 = [0.6, 1, 2, 3] 
    list2 = [3, 2, 0.6, 1] 
    list3 = [9, 0, 5, 10.5]
    print(are_lists_equal(list1, list2))
    print(are_lists_equal(list1, list3))

if __name__ == '__main__':
    main()
