# Rolling assignment.
# Hangman Game.
# Koby Galanty

# For selecting file name
import tkinter as tk
from tkinter import filedialog as fd

root = tk.Tk()
root.withdraw()

# For identifing the system - Clear Screen order
import os
os.system('cls' if os.name == 'nt' else 'clear')


#EX 1.4.1
import random

#EX 2.5.1
MAX_TRIES = 6
HANGMAN_ASCII_ART = '''   _    _\n  | |  | | \n  | |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __    
  |  __  |/ _` | \'_ \\ / _` | \'_ ` _ \ / _\ | \'_ \   
  | |  | | (_| | | | | (_| | | | | | | (_| | | | | \n  |_|  |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
    \t\t       __/ | \n   \t\t       |___/\n'''

def open_credit(tries):
# Write HANGMAN on screen in ascii
    print(HANGMAN_ASCII_ART + '\n\n')


#Ex 7.3.1
def show_hidden_word(secret_word, old_letters_guessed):
    '''
    Show the right guessed letters from the secret word
    :param secret_word: The word the user have to guess
    :param old_letter_guessed: A list of previus guessed letters
    :type secret_word: String
    :type old_letter_guessed: List
    :return: A list composed of guessed letters and under scores
    :rtype: String
    >>> secret_word = "mammals"
    >>> old_letters_guessed = ['s', 'p', 'j', 'i', 'm', 'k']
    >>> print(show_hidden_word(secret_word, old_letters_guessed))
    m _ m m _ _ s
    '''
    current_status = 'The word so far:'
    for char in secret_word:
        if char in old_letters_guessed:
            current_status += char + ' '
        else:
            current_status += '_ '
    return current_status


#Ex 7.3.2
def check_win(secret_word, old_letters_guessed):
    '''
    Check if the user won.
    :param secret_word: The word the user have to guess
    :param old_letter_guessed: A list of previus guessed letters
    :type secret_word: String
    :type old_letter_guessed: List
    :return: True if all the letters that compose the secret word are in old_letters_guessed
             False if not
    :rtype: Bool
    >>> secret_word = "friends"
    >>> old_letters_guessed = ['m', 'p', 'j', 'i', 's', 'k']
    >>> print(check_win(secret_word, old_letters_guessed))
    False
    >>> secret_word = "yes"
    >>> old_letters_guessed = ['d', 'g', 'e', 'i', 's', 'k', 'y']
    >>> print(check_win(secret_word, old_letters_guessed))
    True
    '''
    test_word = show_hidden_word(secret_word, old_letters_guessed)
    if '_' in test_word:
        return False
    return True


#EX 6.4.1
def check_valid_input(letter_guessed, old_letters_guessed):
    '''
    Test if the letter the user guessed is a valid letter/input
    and if the user allready guessed the letter.
    :param letter_guessed: A string the user guess
    :param old_letter_guessed: A list of previus guessed letters
    :type letter_guessed: String
    :type old_letter_guessed: List
    :return: A boolean value is letter_guessed is a letter or not
    :rtype: Bool
    '''
    if len(letter_guessed) == 1 and letter_guessed.isalpha():
        if letter_guessed not in old_letters_guessed:
            return True
    return False


#EX 6.4.2
def try_update_letter_guessed(letter_guessed, old_letters_guessed):
    '''
    Test if the letter the user guessed is a valid letter/input
    and if the user allready guessed the letter.
    Will add new letters to the list
    :param letter_guessed: A string the user guess
    :param old_letter_guessed: A list of previus guessed letters
    :type letter_guessed: String
    :type old_letter_guessed: List
    :return: A boolean value is letter_guessed is a letter or not
    :rtype: Bool
    '''
    answer = check_valid_input(letter_guessed, old_letters_guessed)
    if answer:
        old_letters_guessed.append(letter_guessed)
    else:
        print('\nX')
        print(" ->".join(old_letters_guessed))
    return answer


HANGMAN_PHOTOS = {
0:'\n\n\n\n\n\nx-------x',
1:'\n|\n|\n|\n|\n|\nx-------x',
2:' -------\n|       |\n|       0\n|\n|\n|\nx-------x',
3:' -------\n|       |\n|       0\n|       |\n|\n|\nx-------x',
4:' -------\n|       |\n|       0\n|      /|\\\n|\n|\nx-------x',
5:' -------\n|       |\n|       0\n|      /|\\\n|      /\n|\nx-------x',
6:' -------\n|       |\n|       0\n|      /|\\\n|      / \\\n|\nx-------x'}

def print_hangman(num_of_tries):
    '''
        This function print the status of the "hangman", based on number of tries
        :param num_of_tries: Number of tries the user failed so far
        :type num_of_tries: number
        :return: None
    '''
    if num_of_tries > 0:
        print(':(')
    print(HANGMAN_PHOTOS[num_of_tries])
    print('\nYou have another ' + str(MAX_TRIES - num_of_tries) + ' attempts to fail')

#Ex 9.4.1
def choose_word(file_path, index):
    '''
       This function select a word to guess.
       :param file_path: The path to the file to choose from
       :type file_path: string
       :return: number of words and the word it choossed
       :rtype: tuple
    '''
    with open(file_path,'r') as f1:
        list_of_words = f1.read().split(' ')
    set_of_words = set(list_of_words)
    num_of_words = len(set_of_words)
    j = index % num_of_words
    word = list(set_of_words)[j]
    return word

def main():
    # We shell recieve the file from the user and he will pick a number for the word
    num_of_tries = 0
    #open_credit(num_of_tries)
    print(HANGMAN_ASCII_ART +str('\n\n'))
    print('Hello there, let us play a little game of "Hangman".')
    print("I'm going to pick a word out of a file you will provide.")
    print('Then you will have to guess the word, letter by letter.')
    print('A letter you allready picked or a wrong guess will cost you a strike.')
    print('You get 6 strikes. \nReady? lets go')
    input('press any key...\n')

    print('Please select a file')
    in_file = fd.askopenfilename()
    inde = int(input('Choose a number: '))
    print("\nLet's start!")

    #Ex 6.4.1
    old_letters_guessed = []
    word_chosen = choose_word(in_file, inde)
    current_word = ''
    after_guess_word = ''
    while(num_of_tries <= MAX_TRIES):
        os.system('cls' if os.name == 'nt' else 'clear')
        open_credit(num_of_tries)
        print_hangman(num_of_tries)

        #EX 2.5.2 #EX 4.3.1
        print(show_hidden_word(word_chosen, old_letters_guessed))
        a_guess = input('Guess a letter: ').lower()
        current_word = show_hidden_word(word_chosen, old_letters_guessed)
        try_update = try_update_letter_guessed(a_guess, old_letters_guessed)
        after_guess_word = show_hidden_word(word_chosen, old_letters_guessed)
        print(after_guess_word)
        # If the guess haven't changed the status of word and the input is valid
        # the num of tries go up by 1.
        if try_update and (current_word == after_guess_word):
            num_of_tries += 1

        if check_win(word_chosen, old_letters_guessed):
            print('WON')
            break
        if num_of_tries == MAX_TRIES:
            break

    #print_hangman(num_of_tries)
    if num_of_tries >= MAX_TRIES:
        print('LOSE')


if __name__ == '__main__':
    main()
