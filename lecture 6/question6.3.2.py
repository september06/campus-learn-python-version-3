def longest(my_list):
    s=sorted(my_list,key=len)  
    return s[len(my_list)-1]



list1 = ["111", "234", "2000", "goru", "birthday", "09"]
s = longest(list1)
print(s)

input("Please enter a word: ") 