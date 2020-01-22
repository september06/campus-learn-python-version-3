# Hangman Game for training 
import random
import re #a regular expression for check_valid_input meathod 
import os
from hangman_text import hangman_text
from hangman_print import hangman_print

def choose_word(file_path, index):
    """
    Receiving Function as Parameters: A string representing a path to a text file that contains spaces separated by words thes word we will use it as secret_word,
	and an integer representing the location of a particular word in the file.
	it also built a list that contains words without their duplicates and counts them.
    The function returns a tuple consisting of two organs in the following order: the number of different words in the file
	a word in the position obtained as an argument to the function (index).
	:param file_path : the path for the words file  .
	:param index : index of word in file.
	:type file_path : string .
    :type index : char .
	: return :  the number of different words in the file a word in the position obtained as an argument to the function.
	: return type : tuple.
    """
    MY_SPACE = " "
    different_data = []
    all_data = []	
    words_in_file = open(file_path, "r")
    for row in words_in_file:        
        for word in row.split(MY_SPACE):
            all_data.append(word)   
            if word not in different_data:
                different_data.append(word)
    number_of_DWords = len(different_data)
    number_of_AWords = len(all_data)
    amount_and_word = (number_of_DWords, all_data[(int(index) - 1) % number_of_AWords]) # we use 
    words_in_file.close()
    return amount_and_word
    		
def check_valid_input(letter_guessed, old_letters_guessed):
    """
	A boolean function that receives a character and a footer that the user has previously guessed.
	The function checks two things: the correctness of the input and whether it is legal to guess this letter,
	returns true or false accordingly.
	:param letter_guessed : the letter that guessed by the user .
	:param old_letters_guessed : The list holds the letters the player has guessed so far.
	:type letter_guessed : char .
    :type old_letters_guessed : list .
	: return :  TRUE or FALSE.
	: return type : boolean.
    """
    #the second and thred condution
    pattern = re.compile('[^A-Za-z]+')	# we use a regular expression for any letter
    if(len(letter_guessed) > 1) and (pattern.search(letter_guessed)):
        print(' E3 : Non-English character and letter string containing more than one character ')
        return False
    #If the player entered a letter string containing more than one character, print the string "E1".
    elif(len(letter_guessed) > 1):
        print(' E1 : Letter string containing more than one character  ')
        return False
    #If the player has entered a non-English character check by regular expression print the string "E2".
    elif (pattern.match(letter_guessed)):
        print(" E2 : Non-English character ")
        return False
    elif (letter_guessed in old_letters_guessed):
        print( " [ " + letter_guessed.lower() + ' ] : Already guessing ')
        return False
    else:
        print(letter_guessed.lower())
        return True
		
		
def try_update_letter_guessed(letter_guessed, old_letters_guessed):
    """ 
   	The function uses the check_valid_input function to know if the character is invalid and not previously guessed or the character is invalid and / or already in the guess list.
    If the character is invalid or has already guessed the character in the past, the function prints the character X (as a big letter), 
	below it the list of letters already guessed and returns false.
	If the character is incorrect and has not been guessed before - the function adds the character to the guess list and returns true.
	:param letter_guessed : the letter that guessed by the user .
	:param old_letters_guessed : The list holds the letters the player has guessed so far.
	:type letter_guessed : char .
    :type old_letters_guessed : list .
	:return :  TRUE or FALSE.
	:return type : boolean.
	 
    """
    if(check_valid_input(letter_guessed, old_letters_guessed)):
        old_letters_guessed.append(letter_guessed)
        print(old_letters_guessed)
        return True
    else:
        print(" X\n" + 'guessed letters until now :')
        print( ' =' + '='*len(old_letters_guessed)*5 + '\n|| ' + ' -> '.join(sorted(old_letters_guessed))+ ' ||\n' + ' =' + '='*5*len(old_letters_guessed))
        return False
            		
					
def show_hidden_word(secret_word, old_letters_guessed):
    """
    This is a function that returns a string consisting of letters and underscores. 
    The string displays the letters from the old_letters_guessed list that are in the secret_word string in their respective positions, 
    and the rest of the letters in the string (which the player has not yet guessed) as underscores.
	:param secret_word : That's the word the user has to guess .
    :param old_letters_guessed : The list holds the letters the player has guessed so far.
    :type secret_word : string .
    :type old_letters_guessed : list .
	:return show_hidden : show_hidden is a string consisting of letters and underscores.
	:return type : string . 
    """
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
    """
    A boolean function that returns true if all the letters that make up the secret word are included in the list of letters the user guessed.
    therwise, the function returns false.
    :param secret_word : That's the word the user has to guess .
    :param old_letters_guessed : The list holds the letters the player has guessed so far.
    :type secret_word : string .
    :type old_letters_guessed : list .
    :return : TRUE \ FALSE.
    :return type : boolean.
    """
    for elem_a in list(secret_word): 
        if elem_a not in old_letters_guessed :
            return False   
    return True
    
	
def print_function(word_path = 'c:', index_word = -1, MAX_TRIES = 7, old_letters_guessed = 'X', player_guess = 'none',num_of_tries = 7 ):
    """
	this function just for print what we need every time .
	:param word_path : That's the word the user has to guess .
    :param old_letters_guessed : The list holds the letters the player has guessed so far.
	:param index : index of word in file.
	:param MAX_TRIES : index of word in file.
	:param player_guess : user so correct gusse so fare.
	:param num_of_tries : The number represents the number of failed attempts by the user so far.
	:type word_path : string .
    :type old_letters_guessed : list .
	:type index : char .
    :type MAX_TRIES : int .
	:type player_guess : string .
    :type num_of_tries : int .
	:return: none
	"""
    hangman_text.print_hangman()
    print(MAX_TRIES)
    print("Please Enter Docminet Path : " + word_path )
    print("Please Enter index for word in file :  " + index_word)
    print('guessed letters until now :')
    print( ' =' + '='*len(old_letters_guessed)*5 + '\n|| ' + ' -> '.join(sorted(old_letters_guessed))+ ' ||\n' + ' =' + '='*5*len(old_letters_guessed)) 
    print( "===>you still have [ %d ] tries<=== " % (num_of_tries))
    print ('guessed letters until now  :' + player_guess)

def main():
    while(1):
	    #The variable holds the pictures of the hangmann in each of the situations.
        hangman_print_doll	= {
	        0: hangman_print.hangman_print0,
            1: hangman_print.hangman_print1,
            2: hangman_print.hangman_print2,
            3: hangman_print.hangman_print3,
            4: hangman_print.hangman_print4,
            5: hangman_print.hangman_print5,
            6: hangman_print.hangman_print6,
            7: hangman_print.hangman_print7
        }					
        hangman_text.print_hangman()
        MAX_TRIES = 7    # random.randint(5, 10)
        num_of_tries = 0 # The number represents the number of failed attempts by the user so far.
        letters_guessed = []
        hangman_print_state = 0
        print(MAX_TRIES)
        word_path = input("Please Enter Docminet Path by using [\\\\] between folders : ")
        index_word = input("Please Enter index for word in file :  ")
        tuple_of_amount_word = choose_word(word_path , index_word)
        print( tuple_of_amount_word ) # for the checker
        print("^^^^^^ <== this row for the checker to see what the function returns is correctly and it will delete the next iteration||")  # for checker
        secret_word = tuple_of_amount_word[1]
        print ('guesse the word : ' + len(secret_word)*'_ ')
        while (num_of_tries != MAX_TRIES):
            hangman_print_doll[hangman_print_state]()
            while True :              # in case user insert empty input 
                    letter_guessed_by_player = input("Please Guess a letter: ")
                    if letter_guessed_by_player :
                        break		
            letter_guessed_by_player_lowerLitr = letter_guessed_by_player.lower()
            legail = try_update_letter_guessed(letter_guessed_by_player_lowerLitr, letters_guessed)
            while(legail == False ):
                print('====>illegail input please try agine<====')
                while True :          # in case user insert empty input 
                    letter_guessed_by_player = input("Please Guess a letter: ")
                    if letter_guessed_by_player :
                        break		
                letter_guessed_by_player_lowerLitr = letter_guessed_by_player.lower()
                legail = try_update_letter_guessed(letter_guessed_by_player_lowerLitr,letters_guessed)
            player_guess = show_hidden_word(secret_word, letters_guessed)
            result = check_win(secret_word, letters_guessed)
            if(result == True):
                break
            elif (letter_guessed_by_player not in secret_word):
                hangman_print_state = hangman_print_state + 1
                num_of_tries = num_of_tries + 1		   
            os.system('cls')
            print_function(word_path, index_word, MAX_TRIES, letters_guessed, player_guess, MAX_TRIES-num_of_tries)
        if(result == True):
            os.system('cls')
            hangman_text.print_hangman()
            print(""" 
					====================================
					||     Congratulations,YOU WIN   ||
					===================================""")
            print("""
					░░░░░░░░░░░░░░░░░░░░░░█████████
					░░███████░░░░░░░░░░███▒▒▒▒▒▒▒▒███
					░░█▒▒▒▒▒▒█░░░░░░░███▒▒▒▒▒▒▒▒▒▒▒▒▒███
					░░░█▒▒▒▒▒▒█░░░░██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██
					░░░░█▒▒▒▒▒█░░░██▒▒▒▒▒██▒▒▒▒▒▒██▒▒▒▒▒███
					░░░░░█▒▒▒█░░░█▒▒▒▒▒▒████▒▒▒▒████▒▒▒▒▒▒██
					░░░█████████████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██
					░░░█▒▒▒▒▒▒▒▒▒▒▒▒█▒▒▒▒▒▒▒▒▒█▒▒▒▒▒▒▒▒▒▒▒██
					░██▒▒▒▒▒▒▒▒▒▒▒▒▒█▒▒▒██▒▒▒▒▒▒▒▒▒▒██▒▒▒▒██
					██▒▒▒███████████▒▒▒▒▒██▒▒▒▒▒▒▒▒██▒▒▒▒▒██
					█▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒█▒▒▒▒▒▒████████▒▒▒▒▒▒▒██
					██▒▒▒▒▒▒▒▒▒▒▒▒▒▒█▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██
					░█▒▒▒███████████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██
					░██▒▒▒▒▒▒▒▒▒▒████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒█
					░░████████████░░░█████████████████
			     """)			
        else:
            os.system('cls')
            hangman_text.print_hangman()
            print('YOU Lost')
            print('THE SECRET WORD WAS [ ' + secret_word + ' ] AND YOUR GUESSED WAS  [ ' + player_guess + "]")
            hangman_print_doll[7]()
		
        more_round = input("DO YOU WANT TO PLAY AGAIN ?? [Y\\N] ")
        if (more_round == 'n' or more_round =='N'):
            print("""
			******************************************************
			***** GOOD BYE, WE WILL BY HAPPY TO SEE YOU AGAIN ****
			******************************************************	
			""")
            input("please press enter to exit... ")
            break
        else:
            os.system('cls') 
            
	
        
	
if __name__ == "__main__":
    main()
	
	
	
	

	