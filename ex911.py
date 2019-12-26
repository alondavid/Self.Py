#EX9.1.1

with open('chat.txt','w') as w_file1:
    w_file1.write('who goes there?')

with open('response.txt','w') as w_file2:
    w_file2.write ('It is I!')   #('who goes there?') #('It is I!')

def are_files_equal(file1, file2):
    f1 = open(file1,'r')
    f2 = open(file2,'r')
    if f1.read() == f2.read():
        return True
    return False

print(are_files_equal('chat.txt','response.txt'))
    
