name = "Zed A. Shaw"
age = 35 # not a lie
haight = 74 # inches
haight_in_CM = haight * 2.54
weight = 180 # lbs
weight_in_KG = weight * 0.45359237
eyes = "Blue"
teeth = "White"
hair = "Brown"

print(f"let's talk about {name}.")
print(f"he's {haight} inches or {haight_in_CM} cm tall.")
print(f"he's {weight} pounds or {round(weight_in_KG)} kg heavy.")
print("Actually that's not too heavy.")
print(f"he's got {eyes} eyes and {hair} my_hair.")
print(f"his teeth are usually {teeth} depending on the coffee.")

#this line is tricky, try to get is exactly right 
total = age + haight + weight
print(f"if i add {age},{haight} and {weight} i get {total}")