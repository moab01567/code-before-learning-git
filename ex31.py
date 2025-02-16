print("""You enter a dark room with tow doors.
Do you go though door #1 or door #2""")

door = input(">")

if door == "1":
	print("there is a giant bear here eating a cheese cake.")
	print("what do you do?")
	print("1. take the cake.")
	print("2. scream at the bear.")

	bear = input(">")

	if bear == "1":
		print("the bear eats your face off. good job!")
	elif bear == "2":
		print("The bear eats your leg off. good job!")
	else:
		print(f"Well doning {bear} is probably better.")
		print("bear runs away.")

elif door == "2":
	print("you stare into the endless abyss at cthulu's retina.")
	print("1. blueberries.")
	print("2. Yellow jacket clothespins.")
	print("3. understanding recolvers yelling melodies.")

	insanity = input(">")

	if insanity == "1" or insanity == "2":
		print("your body suvives powered by a mind of jello.")
		print("good job!")
	else:
		print("the insanity rots your eyes into a pool of muck.")
		print("good job!")

else:
	print("you stumble around and fall on a knife and die. good job!")