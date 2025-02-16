import random 

liste = []
for i in range(10):
	liste.append(random.randint(1,10))

print(liste)
antall_elementer = len(liste)



for pos in range(antall_elementer):
	print(liste[antall_elementer - pos - 1 ])

	if 8 == liste[antall_elementer - pos - 1]:
		liste.pop(antall_elementer - pos - 1)
	else:
		continue


print(liste)