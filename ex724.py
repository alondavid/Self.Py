#Ex 7.2.4
def seven_boom(end_number):
    '''
       Compose a list of numbers from 0 to end_number(included).
       replace the number with the word 'BOOM' if the number % 7 == 0 or contain 7
       :param end_number: A num
       :param type: Integer
       :return: list of numbers/'BOOM'
       :rtype: List
    '''
    list_of_numbers = []
    x = 0
    while x <= end_number:
        if x % 7 == 0 or '7' in str(x):
            list_of_numbers += ['BOOM']
        else:
            list_of_numbers += [x]
        x += 1
    return list_of_numbers

def main():
    print(seven_boom(17))

if __name__ == '__main__':
    main()
