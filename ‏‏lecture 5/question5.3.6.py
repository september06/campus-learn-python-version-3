import re

def fix_age(age):
    if(age == 16) or (age == 15): 
        return age
    return 0
	
def chocolate_maker(small, big, x):
    if (x%5==0):
	    if(x/5<=big)
            print("true")
			return
    else:	
	    if(x%5<=small)
            print("true")
			return
        	
    print(false)
	
my_str = input("Please enter the lengh of the chocolate,number of picec 1cm^2 and number of picec 5cm^2 : ")
matches = re.findall("(\d+)",my_str) 
print(matches)
chocolate = int(matches[0])
small_piece = int(matches[1])
big_piece = int(matches[2])
chocolate_maker(small_piece, big_piece, chocolate)
my_str = input("Please enter a 3 numbers: ")
	