#PYTHON randint FUNCTION : randint(minimum number , maximum number) 
#take 2 arguments 
#Return arandom integer between a maximum and minimum number incloud
import random
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
								
print(HANGMAN_ASCII_ART,MAX_TRIES)


letter_guessed_by_player = input("Please Guess a letter: ")

print(letter_guessed_by_player.lower())

word_typed_by_player = input("Please enter a word: ")
print("_ "*len(word_typed_by_player))
input("please press enter to exit")