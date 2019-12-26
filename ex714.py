#Ex 7.1.4
def squared_numbers(start, stop):
    '''
      Raise the numbers in the range by power of 2.
      :param start: The first numer
      :param stop: The last number
      :type start: Integer
      :type stop: Integer
      :return: A list of squared numbers
      :rtype: List
    '''
    lst = []
    i = start
    while  (i <= stop):
        lst += [i ** 2]
        i += 1
    return lst

def main():
    print(squared_numbers(4, 8))
    print(squared_numbers(-3, 3))

if __name__ == '__main__':
    main()
