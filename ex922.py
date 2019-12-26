#EX9.2.2

import tkinter as tk
from tkinter import filedialog

root = tk.Tk()
root.withdraw()

def copy_file_content(source, destination):
    with open(source,'r') as f1:
        long_line = f1.read()
    with open(destination,'w') as f2:
        f2.write(long_line)   #('who goes there?') #('It is I!')

    
in_file = filedialog.askopenfilename()
out_file = filedialog.askopenfilename()
copy_file_content(in_file, out_file)
