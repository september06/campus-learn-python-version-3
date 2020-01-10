def sort_prices(list_of_tuples):
    sorted_tap=list_of_tuples
    sorted_tap.sort(key = lambda price: float(price[1]))
    print (list_of_tuples)
    print (sorted_tap[::-1])
	
	
products = [('milk', '5.5'), ('candy', '2.5'), ('bread', '9.0')]
sort_prices(products)
input("please enter string : ")