def format_list(my_list):
    length = len(my_list)
    odd_list = my_list[0:length-3:2]
    s_string = ', '
    s=s_string.join( odd_list )
    return s+', and '+my_list[length-1]
	 
	
my_list = ["hydrogen", "helium", "lithium", "beryllium", "boron", "magnesium"]
s = format_list(my_list)
print(s)
input("Please enter a word: ") 