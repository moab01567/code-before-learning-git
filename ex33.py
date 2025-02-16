
def go(start, slutt, økning): 
	numbers = []
	for i in range(start, slutt, økning): 
		print(f"At the top \"i\" is {i}")
		numbers.append(i)
	
	return numbers

numbers = go(0, 102, 2)

print("the numbers:")

for num in numbers:
	print(num)


