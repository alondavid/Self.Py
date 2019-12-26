#ex 9.3.1

import tkinter as tk
from tkinter import filedialog

root = tk.Tk()
root.withdraw()

def my_mp3_playlist(file_path):
    '''
       The function recieve the path to a file.
       return the longest song, number of songs and the performer with the most
       songs in the list.
       :param file_path: Path to file to read
       :param type: String
       :return: tuple with the longest song, number of songs, the performer with
       the most sings
       :rtype: tuple
    '''
    longest_song = ''
    longest_song_time = 0
    with open(file_path,'r') as f1:
        lines = f1.readlines()
        list_of_lines = []
        performers = {}
        most_performed = ''
        number_of_most_performed = 0
        for line in lines:
            list_of_lines.append(line.split(';'))
            
        number_of_songs = len(list_of_lines)
        
        for line in list_of_lines:
            #  Find the longest song, keep it's length and name
            if float(line[2].replace(':','.')) > longest_song_time:
                longest_song_time = float(line[2].replace(':','.'))
                longest_song = line[0]
            # Build a dictionary of performers with num of songs they perform    
            if line[1] in performers.keys():
                performers[line[1]] += 1
            else:
                performers[line[1]] = 1
        # Go over the dictionary, the performer with the most songs(highest value)        
        for key,value in performers.items():
            if value > number_of_most_performed:
                most_performed ,number_of_most_performed = key, value
                
    return longest_song, number_of_songs, most_performed 
                


def main():
    in_file = filedialog.askopenfilename()
    print(my_mp3_playlist(in_file))
    
    

if __name__ == '__main__':
    main()
