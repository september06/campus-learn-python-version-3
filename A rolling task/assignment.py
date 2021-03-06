#PYTHON randint FUNCTION : randint(minimum number , maximum number) 
#take 2 arguments 
#Return arandom integer between a maximum and minimum number incloud
import random
import re

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
        print("X\n" + 'guessed letters until now :')
        print( ' =' + '='*len(old_letters_guessed)*5 + '\n|| ' + ' -> '.join(sorted(old_letters_guessed))+ ' ||\n' + ' =' + '='*5*len(old_letters_guessed))
        return False
            		
					
def show_hidden_word(secret_word, old_letters_guessed):
    show_hidden = '_ ' * len(secret_word)
    for i in range(len(secret_word)):
       if secret_word[i] == " ":
            show_hidden = show_hidden[:2*(i)] + '  ' + show_hidden[(i+1)*2:]
            print(show_hidden)
    for k in range(0,len(old_letters_guessed)):
        for j in range(0,len(secret_word)):
             if old_letters_guessed[k] in secret_word[j]:
                temp_string = list(show_hidden)
                print(temp_string)
                temp_string[j*2] = old_letters_guessed[k]
                show_hidden = "".join(temp_string)
    return show_hidden 
		    
def check_win(secret_word, old_letters_guessed):
    player_guess = show_hidden_word(secret_word, old_letters_guessed)		
    if(player_guess.replace(" ", "") in secret_word.replace(" ", "")):
        return True
    print(player_guess)
    print(secret_word)
    return False			
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
MAX_TRIES = random.randint(5, 10)
secret_word = "llwl"
letters_guessed = ['b','a','z','w']
print(HANGMAN_ASCII_ART, MAX_TRIES)

letter_guessed_by_player = input("Please Guess a letter: ")
letter_guessed_by_player_lowerLitr = letter_guessed_by_player.lower()
print(letter_guessed_by_player_lowerLitr)

legail = try_update_letter_guessed(letter_guessed_by_player_lowerLitr,letters_guessed)
while(legail == False ):
    letter_guessed_by_player = input("Please Guess a letter: ")
    letter_guessed_by_player_lowerLitr = letter_guessed_by_player.lower()
    legail = try_update_letter_guessed(letter_guessed_by_player_lowerLitr,letters_guessed)
    print(legail)
result = check_win(secret_word, letters_guessed)
print(result)
word_typed_by_player = input("Please enter a word: ")
print("_ " * len(word_typed_by_player))
input("please press enter to exit")