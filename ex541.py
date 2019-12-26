#ex 5.4.1

def func(num1, num2):
    """
    This function return the result of num1 by power of num2
    :param num1: number to be calculated on
    :param num2: number to be raised by
    :type num1: int
    :type num2: int
    :return: The result of raising base to the power num2
    :rtype: int
    """
    return num1 ** num2

def main():
    # Call the function func
    print(func(5,4))

if __name__ == "__main__": 
    main()
