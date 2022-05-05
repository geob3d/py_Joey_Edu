from lib2to3.pytree import convert


name = 'Zed A. Shaw'
age = 35 # not a lie
height = 74 # inches
weight = 180 #lbs
eyes = 'Blue'
teeth ="white"
hair = "Brown"
print (f"Let's talk about {name}.")
print (f"He'sc{height} inches tall.")
print ("Actually that's not too heavy.")
print (f"He's got {eyes} eyes and {hair} hair")
print (f"His teeth are usually {teeth} depending on the coffee.")
#this line is tricky, try to get it exactly right
total = age + height + weight
print (f"If I add {age} + {height}, and {weight} I get {total}.")
b = 30/12
c = 1/2.2
print (height * b) # height in centimeters
print (weight * c) # weight in kilos