#PYTHON randint FUNCTION : randint(minimum number , maximum number) 
#take 2 arguments 
#Return arandom integer between a maximum and minimum number incloud
import random
import re

def is_valid_input(letter_guessed):
#the second and thred condution
    pattern = re.compile('[^A-Za-z]+')	
    if(len(letter_guessed) > 1) and (pattern.search(letter_guessed)):
        print('E3')
        return 'False'
#If the player entered a letter string containing more than one character, print the string "E1".
    elif(len(letter_guessed) > 1):
        print('E1')
        return 'False'
#If the player has entered a non-English character check by regular expression print the string "E2".
    elif (pattern.match(letter_guessed)):
        print("E2")
        return 'False'
    else:
        print(letter_guessed.lower())
        return 'True'
HANGMAN_ASCII_ART = """
   _    _
  | |  | |
  | |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __
  |  __  |/ _` | '_ \\/  _ `| '_ ` _ \\ / _ `| '_ \\
  | |  | | (_| | | | | (_| | | | | | | (_| | | | |
  |_|  |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                       __/ |
                      |___/
 """
MAX_TRIES=random.randint(5, 10)
print(HANGMAN_ASCII_ART, MAX_TRIES)
letter_guessed_by_player = input("Please Guess a letter: ")
legail = is_valid_input(letter_guessed_by_player)
print(legail)
word_typed_by_player = input("Please enter a word: ")
print("_ " * len(word_typed_by_player))
input("please press enter to exit")