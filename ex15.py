from sys import argv

script, file_name  = argv

txt = open(file_name)
print(f"Here's your file {file_name}:")
print(txt.read())
txt.close()

print("type the file name agin.")
file_agin = input(">")
txt = open(file_agin)

print(txt.read())
txt.close()

