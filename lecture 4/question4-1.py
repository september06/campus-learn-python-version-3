str = input("please enter string : ")
new_str = str.lower()
str = new_str.replace(" ", "")
num_chars=int(len(str)/2)
print(str[:(num_chars):-1])
print(str[0:(num_chars)])
if (str[0:(num_chars)] == str[:(num_chars):-1]):
    print("OK")
else:
    print("NOT")

input("please enter string : ")
	
	

