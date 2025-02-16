the_count = [1, 2, 3, 4, 5]
fruits = ["apples", "ornges", "pears", "apricots"]
change = [1, "pennies", 2, "dimes", 3, "quarters"]

#this first kind of for loop goes through a list
for number in the_count:
	print(f"This is count {number}")

#same as above
for fruit in fruits:
	print(f"A fruit of type: {fruit}")

#also we can go thougt mix list  too
#notice we have to use {} sinse we don't know what's in it
for i in change:
	print(f"I got {i}")

#we can also build a list, frist we make a emty one 
elements = range(6)

#now we can print them out.
for i in elements:
	print("element was: {}".format(i))