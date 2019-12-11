#PYTHON randint FUNCTION : randint(minimum number , maximum number) 
#take 2 arguments 
#Return arandom integer between a maximum and minimum number incloud
import random
import re
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
pattern = re.compile('[^A-Za-z]+')	
print(HANGMAN_ASCII_ART, MAX_TRIES)


letter_guessed_by_player = input("Please Guess a letter: ")
#the second and thred condution
if(len(letter_guessed_by_player) > 1) and (pattern.search(letter_guessed_by_player)):
    print('E3')
#If the player entered a letter string containing more than one character, print the string "E1".
elif(len(letter_guessed_by_player) > 1):
    print('E1')
#If the player has entered a non-English character check by regular expression print the string "E2".
elif (pattern.match(letter_guessed_by_player)):
    print("E2")
else:
    print(letter_guessed_by_player.lower())
word_typed_by_player = input("Please enter a word: ")
print("_ " * len(word_typed_by_player))
input("please press enter to exit")