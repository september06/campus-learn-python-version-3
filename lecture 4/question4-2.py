str = input("Insert the temperature you would like to convert : ")
f_or_c = str[-1]
len_string = int(len(str))
the_temperature = float(str[:-1])
if (f_or_c == 'c') or (f_or_c == 'C'): 
    print(((the_temperature * 9.0)+(32.0 *5.0))/5)	
else:
    print(((the_temperature*5.0)-160.0)/9.0)	
input("Insert the temperature you would like to convert :")