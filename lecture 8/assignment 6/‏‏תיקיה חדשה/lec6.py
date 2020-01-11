#PYTHON randint FUNCTION : randint(minimum number , maximum number) 
#take 2 arguments 
#Return arandom integer between a maximum and minimum number incloud
import random
import re
from hangman_text import hangman_text
from hangman_print import hangman_print

def check_valid_input(letter_guessed, old_letters_guessed):
#the second and thred condution
    pattern = re.compile('[^A-Za-z]+')	
    if(len(letter_guessed) > 1) and (pattern.search(letter_guessed)):
        print('E3')
        return False
#If the player entered a letter string containing more than one character, print the string "E1".
    elif(len(letter_guessed) > 1):
        print('E1')
        return False
#If the player has entered a non-English character check by regular expression print the string "E2".
    elif (pattern.match(letter_guessed)):
        print("E2")
        return False
    elif (letter_guessed in old_letters_guessed):
        return False
    else:
        print(letter_guessed.lower())
        return True
		
		
def try_update_letter_guessed(letter_guessed, old_letters_guessed):
    if(check_valid_input(letter_guessed, old_letters_guessed)):
        old_letters_guessed.append(letter_guessed)
        print(old_letters_guessed)
        return True
    else:
        print("X\n"+'guessed letters until now :')
        print( ' ='+'='*len(old_letters_guessed)*5+'\n|| '+' -> '.join(sorted(old_letters_guessed))+' ||\n'+' ='+'='*5*len(old_letters_guessed))
        return False
            		
					
def main():
    hangman_printD = {
        1: hangman_print.hangman_print7,
        2: hangman_print.hangman_print7,
        3: hangman_print.hangman_print7,
        4: hangman_print.hangman_print7,
        5: hangman_print.hangman_print7,
        6: hangman_print.hangman_print7,
        7: hangman_print.hangman_print7
    }					
    hangman_text.print_hangman()
    MAX_TRIES = random.randint(5, 10)
    letters_guessed = ['b','a','z','w','d','h']
    print(MAX_TRIES)
    letter_guessed_by_player = input("Please Guess a letter: ")
    letter_guessed_by_player_lowerLitr = letter_guessed_by_player.lower()
    print(letter_guessed_by_player_lowerLitr)
    legail = try_update_letter_guessed(letter_guessed_by_player_lowerLitr,letters_guessed)
    print(legail)
    word_typed_by_player = input("Please enter a word: ")
    print("_ " * len(word_typed_by_player))
    input("please press enter to exit")

	
if __name__ == "__main__":
    main()