from sys import argv
from os.path import exists 

script, from_file, to_file = argv

print(f"copying from {from_file} to {to_file}")

#we could do these tow one line, how?
in_file = open(from_file).read()


print(f"the input file is {len(in_file)} bytes long")

print(f"Does th output file exists?{exists(to_file)}")
print("ready, hit Return to continue, CTRL-C to abort.")
input()

out_file = open(to_file,"w")
print(in_file)
out_file.write(in_file)
	
print("alright, all done.")

out_file.close()

		