#EX 9.2.3

import tkinter as tk
from tkinter import filedialog

root = tk.Tk()
root.withdraw()

def who_is_missing(file_name):
    '''
    Looking over a file and find the missing number
    :param file_name: a file to  look at
    :param type: string
    :return: The missing number
    :rtype: number
    '''
    with open(file_name,'r') as f1:
        long_line = f1.read()
        list_of_numbers = sorted(long_line.split(','))
        highest = int(list_of_numbers[-1])
        for number in range(1, highest):
            if number != int(list_of_numbers[number - 1]):
                out_name = filedialog.askopenfilename()
                with open(out_name,'w') as f2:
                    f2.write(str(number))
                return number






def main():
    in_file = filedialog.askopenfilename()
    print(who_is_missing(in_file))



if __name__ == '__main__':
    main()
