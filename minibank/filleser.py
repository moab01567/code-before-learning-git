
with open("pyobjc.txt") as f:
	liste = f.readlines()
	print(liste)


for i in liste:
	i = i.replace("9.0","")
	i = i.replace("\n","")
	print(i.replace(" ",""),end=" ")


