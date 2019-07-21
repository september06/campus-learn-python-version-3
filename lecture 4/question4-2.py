str1 = input("Insert the temperature you would like to convert : ")
f_or_c = str1[-1]
len_string = int(len(str1))
the_temperature = float(str1[:-1])
if (f_or_c == 'c') or (f_or_c == 'C'): 
    print((str(((the_temperature * 9.0)+(32.0 *5.0))/5))+"f")	
else:
    print((str(((the_temperature*5.0)-160.0)/9.0))+"c")	
input("Insert the temperature you would like to convert :")