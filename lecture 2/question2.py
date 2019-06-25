 
number=input(" Enter three digits (each digit for one pig):")
number_of_ston=int(int(number)/100)+int((int(number)/10)%10)+int(number)%10
print(number_of_ston)
print(int(number_of_ston/3))
print(int(number_of_ston%3))
print(int(number_of_ston%3)==0)
input(" Enter three digits (each digit for one pig):")