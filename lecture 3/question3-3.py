str1=input("please enter string : ")
chars=len(str1)
chars=int(chars/2)
new_str=str1[chars:]

print(str1[:chars]+new_str.upper())
new_str=input("please enter string: ")