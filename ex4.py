#vi lager en vaiabel som heter cars og gir den verdein 100
cars = 100

#vi lager en vairbale som heter space_in_a_car og gir den veriden 4.0
space_in_a_car = 4.0

#vi lager en variabel som heter drivers og gir den veriden 30
drivers = 30

#vi lager en variabel som heter passengers og gir den verdien 90
passengers = 90

#vi lager en variabel som heter cars_not_driven og veriden den er bestemt 
#ved å ta variablene cars minus dirvers 
cars_not_driven = cars - drivers

#vi lager en variabel som heter cars_driven. veriden til 
#den variablen er den samme veriden som antall drivers/sjåfører  
cars_driven = drivers

#vi lager en variabel som heter carpool_capacity. 
#veriden på den variablen er bestemt ved å gange cars_driven og space_in_a_car
#da får vi antall pasasjerer vi kan kjøre. 
carpool_capacity = cars_driven * space_in_a_car

#vi lager en varibale som heter average_passengers_per_car
#veriden på denne variablen settes ved å dele passengers og cars_driven
#da vet vi hvor mange pasasjere det trengs i hver tilgjnglige bil 
average_passengers_per_car = passengers / cars_driven 


print("there are", cars, "cars available.")
print("there are only", drivers, "drivers available.")
print("there will be", cars_not_driven, "empty cars today.")
print("we can transport",carpool_capacity, "people today.")
print("we have", passengers, "to carpool today.")
print("we need to put about", average_passengers_per_car, "in each car.")