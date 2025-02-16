def add(a, b):
	print(f"adding {a} + {b}")
	return a + b

def subtract(a, b):
	print(f"subtracting {a} - {b}")
	return a - b

def multiply(a, b):
	print(f"multiplying {a} * {b}")
	return a * b

def divide(a, b):
	print(f"divading {a} / {b}")
	return a / b


print("let's do som math with just functions!")

age = add(30, 5)
height = subtract(78, 4)
weight = multiply(90, 2)
iq = divide(100, 2)

print(f"Age: {age}, Height: {height}, Weight: {weight}, IQ: {iq}")


#a puxxle for the extra credit, type it in anyway.
print("here is a puzzle.")

what =  add(age,subtract(height, multiply(weight, divide(iq, 2))))

print("that becomes: ", what, "can you do it by hand?")

what2 = subtract(add(24, divide(34, 100)), 1023)
print(what2)