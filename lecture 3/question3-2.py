str1=input("please enter string : ")
first_char=str1[0]
new_str=str1.replace(first_char, 'e')
new_str=new_str.replace('e', first_char, 1)
print(new_str)
new_str=input("please enter string: ")