def are_lists_equal(list1, list2):
    return True if( sorted (list1) == sorted(list2)) else False  




list1 = [0.6, 1, 2, 3]
list2 = [3, 2, 0.6, 1]
list3 = [9, 0, 5, 10.5]

s = are_lists_equal(list1, list2)
print(s)
s = are_lists_equal(list1, list3)
print(s)
input("Please enter a word: ") 