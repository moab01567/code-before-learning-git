#this one is like your scripts with argv
def print_tow(*args):
	arg1, arg2 = args
	print(f"args1: {arg1}, args2: {arg2}")

#ok thats *args is actually pointless, we can just do this
def print_tow_agin(args1, args2):
	print(f"args1: {args1}, args2: {args2}")

#this take just one argument
def print_one(args1):
	print(f"args1: {args1}")

#this one takes no argument
def print_no_argument():
	print("no args")

print_tow("zed", "shaw")
print_tow_agin("zed", "shaw")
print_one("mohemmed")
print_no_argument()