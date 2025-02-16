people = 50# lager en vairabel med en verdi på 50 som heter people 
cars = 40# lager en vairabel med en verdi på 40 som heter cars
trucks = 15# lager en vairabel med en verdi på 15 som heter trucks

#hvis cars er større enn people. hvis det er true print det som stør under
#og gå til neste IF setning 
if cars > people:
	print("we should take the cars.")
elif cars < people:
	print("we should not take the cars.")
else:
	print("we can't decide.")

if trucks > cars:
	print("That's too many trucks.")
elif trucks < cars:
	print("Maybe we could take the trucks.")
else:
	print("we still can't decide.")

if people > trucks:
	print("ait, let's just take the trucks.")
else: 
	print("fine, let's stay home then. ")