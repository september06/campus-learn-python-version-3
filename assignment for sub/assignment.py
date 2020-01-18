#PYTHON randint FUNCTION : randint(minimum number , maximum number) 
#take 2 arguments 
#Return arandom integer between a maximum and minimum number incloud
import random
import re
import os
from hangman_text import hangman_text
from hangman_print import hangman_print

def check_valid_input(letter_guessed, old_letters_guessed):
#the second and thred condution
    pattern = re.compile('[^A-Za-z]+')	
    if(len(letter_guessed) > 1) and (pattern.search(letter_guessed)):
        print('E3 : Non-English character and letter string containing more than one character ')
        return False
#If the player entered a letter string containing more than one character, print the string "E1".
    elif(len(letter_guessed) > 1):
        print('E1 : Letter string containing more than one character  ')
        return False
#If the player has entered a non-English character check by regular expression print the string "E2".
    elif (pattern.match(letter_guessed)):
        print("E2 : Non-English character ")
        return False
    elif (letter_guessed in old_letters_guessed):
        print(letter_guessed.lower() + ' : Already guessing ')
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
        print("X\n" + 'guessed letters until now :')
        print( ' =' + '='*len(old_letters_guessed)*5 + '\n|| ' + ' -> '.join(sorted(old_letters_guessed))+ ' ||\n' + ' =' + '='*5*len(old_letters_guessed))
        return False
            		
					
def show_hidden_word(secret_word, old_letters_guessed):
    show_hidden = '_ ' * len(secret_word)
    for i in range(len(secret_word)):
       if secret_word[i] == " ":
            show_hidden = show_hidden[:2*(i)] + '  ' + show_hidden[(i+1)*2:]
    for k in range(0,len(old_letters_guessed)):
        for j in range(0,len(secret_word)):
             if old_letters_guessed[k] in secret_word[j]:
                temp_string = list(show_hidden)
                temp_string[j*2] = old_letters_guessed[k]
                show_hidden = "".join(temp_string)
    return show_hidden 
		    

def check_win(secret_word, old_letters_guessed): 
    for elem_a in list(secret_word): 
        if elem_a not in old_letters_guessed :
            return False   
    return True
    
	
def print_function(word_path = 'c:', index_word = -1, MAX_TRIES = 7, old_letters_guessed = 'X', player_guess = 'none'):
    hangman_text.print_hangman()
    print(MAX_TRIES)
    print("Please Enter Docminet Path : " + word_path )
    print("Please Enter index for word in file :  " + index_word)
    print('guessed letters until now :')
    print( ' =' + '='*len(old_letters_guessed)*5 + '\n|| ' + ' -> '.join(sorted(old_letters_guessed))+ ' ||\n' + ' =' + '='*5*len(old_letters_guessed)) 
    print ('guessed letters until now  :' + player_guess)

def main():
    hangman_print_doll	= {
        1: hangman_print.hangman_print1,
        2: hangman_print.hangman_print2,
        3: hangman_print.hangman_print3,
        4: hangman_print.hangman_print4,
        5: hangman_print.hangman_print5,
        6: hangman_print.hangman_print6,
        7: hangman_print.hangman_print7
    }					
    hangman_text.print_hangman()
    MAX_TRIES = 7 #random.randint(5, 10)
    game_over = 0 # counter for fieal gusses
    letters_guessed = []
    secret_word = "llwl"
    i=1
    print(MAX_TRIES)
    word_path = input("Please Enter Docminet Path : ")
    index_word = input("Please Enter index for word in file :  ")
    while (game_over != MAX_TRIES):
        hangman_print_doll[i]()
        letter_guessed_by_player = input("Please Guess a letter: ")
        letter_guessed_by_player_lowerLitr = letter_guessed_by_player.lower()
        print(letter_guessed_by_player_lowerLitr)
        legail = try_update_letter_guessed(letter_guessed_by_player_lowerLitr, letters_guessed)
        while(legail == False ):
            print('====>illegail input please try agine<====')
            letter_guessed_by_player = input("Please Guess a letter: ")
            letter_guessed_by_player_lowerLitr = letter_guessed_by_player.lower()
            legail = try_update_letter_guessed(letter_guessed_by_player_lowerLitr,letters_guessed)
        player_guess = show_hidden_word(secret_word, letters_guessed)
        result = check_win(secret_word, letters_guessed)
        if(result == False):
            i=i+1
            game_over = game_over + 1
        else:
           break 
        os.system('cls')
        print_function(word_path, index_word, MAX_TRIES, letters_guessed, player_guess)
    word_typed_by_player = input("Please enter a word: ")
    print("_ " * len(word_typed_by_player))
    input("please press enter to exit")
        
	
if __name__ == "__main__":
    main()