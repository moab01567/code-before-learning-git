from sys import argv

script, filname = argv

print(f"we're going to erase {filname}.")



input("?")

print("opning the file...")
target = open(filname, "w")

line1 = input("line1: ") 
line2 = input("line2: ")
line3 = input("line3: ")

print(f"I'm goining to write these to file {filname}")

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)

print("closing file")
target.close()
