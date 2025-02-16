#create a mapping of state to abbrevation
states = {
		"Oregon":"OR",
		"Florida":"FL",
		"california": "CA",
		"New York": "NY",
		"Michigan":"MI"
}

#create a basic set of states and some cities in them
cities = {
	"CA":"San Francisco"
	"MI":"Detroit"
	"FL":"Jacksonville"
}

#add some more cities
cities["NY"] = "New Yourk"
cities["OR"] = "Portland"

#print out some cities
print("-"*10)
print("NY State has: ", cities["NY"])
print("OR State has: ", cities["OR"])

#print some states
print("-"*10)
