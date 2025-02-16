#lager en vairabel som heter types_of_people fir den verdiden 10
types_of_people = 10 
#vi lager en variabel som innholder  en f-string.
x = f"There are {types_of_people} types of people."

binary = "binary"
do_not = "don't"
y = f"Those who know {binary} and those who {do_not}."#

print(x)
print(y)

print(f"I said: {x}")#
print(f"I also said: '{y}'")#

hilarious = False
joke_evaluation  = "Isn't that jok so funny?{}"

print(joke_evaluation.format(hilarious))

w = "this is the left of..."
e = "a sting with a right side."

#når vi legger samme to stinger legger de bare begge to vedisden av hverandre.
#bokstaver kan ikke plusses som tall, derfor legges de vedsiden av hverandre. 
print(w + e)