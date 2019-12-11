#if the last letter apper in the word befor ?
def last_early(my_str):
    
	char1 = my_str[ len(my_str)-1]
	print(char1)
	if (char1 in my_str[0:len(my_str)-1]):
	    print("true")
	else:
	    print("false")
my_str = input("Please enter a word: ")
last_early(my_str)
input("Please enter a word: ")