import re
def distance(num1, num2, num3):
    print(num1+num2+num3)
    if (((abs(num1-num2) == 1) or (abs(num1-num3) == 1)) and (((abs(num1-num2)>=2)or (abs(num1-num3)>=2)) and (abs(num3-num2)>=2))):
	    print("true")
    else: 
	    print("false")
		
my_str = input("Please enter a 3 numbers: ")
matches = re.findall("(\d+)",my_str) 
print(matches)
number1 = int(matches[0])
number2 = int(matches[1])
number3 = int(matches[2])

distance(number1, number2, number3)
my_str = input("Please enter a 3 numbers: ")
	