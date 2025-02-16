ten_things = "apples Oranges crows telephone Light Suger"

print("wait there are not 10 things in that list. let's fix that")

stuff = ten_things.split(" ")
more_stuff = ["Day", "Night", "Song", "Frisbee",
				"corn", "Banana", "Gril", "Boy"]

while len(stuff) != 10:
	next_one = more_stuff.pop()
	print("adding:", next_one)
	stuff.append(next_one)
	print(f"there are {len(stuff)} items now")

print("There we go: ", stuff)

print("let's do som more things with stuff")

print(stuff[1])
print(stuff[-1])
print(stuff.pop())
print(stuff[-1])
print(' '.join(stuff))
print('#'.join(stuff))