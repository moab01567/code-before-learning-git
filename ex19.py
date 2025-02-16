#vi lager en funksjon med to argumenter
def cheese_and_crackers(cheese_count, boxes_of_crackers):
	print(f"You have{cheese_count} cheeses!")
	print(f"you have {boxes_of_crackers}boxes of crackers!")
	print("Man that's enough for a party!")
	print("get a blanket.\n")

#printer ut på terminalen 
print("we can just give the function numbers directly!")
cheese_and_crackers(20, 30)


print("or, we can use variables from our script:")
#lager to variabler med ulike verider
amount_of_cheese = 10
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese, amount_of_crackers)


print("we can even do math inside too")
#kaller på funksjoen med to argumenter, men plusser på de først.
cheese_and_crackers(10 + 20, 5 + 6)


print("and we can combine the tow, variables and math:")
#kaller på funksjoen med to argumenter, men plusser på de først.
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)