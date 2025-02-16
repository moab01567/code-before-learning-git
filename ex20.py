#importerer modoulen 
from sys import argv
#setter de utgitte variabelen fra commandlinen
script, input_file = argv
#denne funksjoen leser hele programmet 
def print_all(f):
	print(f.read())
#denne funksjoen lar leseren gå tilbake  
def rewind(f):
	f.seek(0)
#printer hver line for seg selv. denne funskjoen tar i mot to arguemnter. 
def print_a_line(line_count, f):
	print(line_count, f.readline())
#åpner fila i en variabel
current_file = open(input_file)

print("first let's print the whole file\n")

print_all(current_file)

print("now lets rewind, kind of like a tape.")

rewind(current_file)

print("let's print three lines")

current_line = 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)
