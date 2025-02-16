from sys import exit

def gold_room():
	print("this room is full og gold. How much do you take?")

	choice = input("> ")
	if choice.isnumeric():
		how_much = int(choice)
	else:
		dead("man, learn to type a number.")

	if how_much < 50:
		print("Nice, you'ar not greedy, you win!")
		exit(0)
	else:
		dead("you greedy bastard!")

def bear_room():
	print("There is a bear here.")
	print("the bear has a bunch of hony.")
	print("the fat bear is in front of another door.")
	print("How are you going to move the bear?")
	bear_moved = False 

	while True:
		choice = input("> ")

		if choice == "take hony":
			dead("the bear look at you then slaps ypu face off.")
		elif choice == "taunt bear" and not bear_moved:
			print("the bear has moved from the door")
			print("you can go though it now")
			bear_moved = True
		elif choice == "taunt bear" and bear_moved:
			dead("the bear gets pissed off and chewa you legg off.")
		elif "open door" and bear_moved:
			gold_room()
		else:
			print("I got no idea what that means.")


def cthulhu_room():
	print("here you see the great evil cthulhu")
	print("He, it, whatever stares at you and you go insane")
	print("do you flee for you life og eat yeaur head?")

	choice = input("> ")

	if "flee" in choice:
		start()
	elif "head" in choice:
		dead("Well that was nasty!")
	else:
		cthulhu_room()


def dead(why):
	print(why, "good job!")
	exit(0)

def start():
	print("you are in a dark room.")
	print("There is a door to your right and left.")
	print("wich one do you take?")

	choice = input("> ")

	if choice == "left":
		bear_room()
	elif choice == "right":
		cthulhu_room()
	else:
		dead("you stumble around the room untill you starve")


start()





















