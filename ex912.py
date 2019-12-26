#EX 9.1.2
import tkinter as tk
from tkinter import filedialog

root = tk.Tk()
root.withdraw()


def sort(long_line):
    return sorted(list(set(long_line.split())))
 
def rev(long_line):
    lines = long_line.split('\n')
    return lines[0][-1::-1] + '\n' +lines[1][-1::-1]
 
def last(long_line, num):
    lines = long_line.split('\n')
    last_lines = []
    length = len(lines)
    return lines[-1:(-1 - num):-1]


def main():
    file_name = filedialog.askopenfilename()
    action = input('Enter a task: ')
    number = 0
    if action == 'last':
        number = int(input('Please enter a number '))
    
    with open(file_name,'r') as f1:
    #f1 = open(file_name,'r')
        long_line = f1.read()
               # 'last':last(file_name)}
        action_dict = {'sort':sort(long_line),
                   'rev':rev(long_line),
                   'last':last(long_line, number)}
 
    print(action_dict[action])
    #f1.close()

if __name__ == '__main__':
    main()
