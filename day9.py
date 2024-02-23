#Dictionary
# program 1

vehicle = {
    'color':"red",
    'type':"sedane"
}
#print(vehicle)
#print(len(vehicle))

#print("hello")
#print(vehicle['color'])
#q1 = vehicle.get('coloa') 
#print(q1)
#print("bye")

# program 2

vehicle = {
    'color':"red",
    'type':"sedane"
}
# vehicle.clear()
# del vehicle
# print(vehicle)
# vehicle.pop('color)
e = vehicle.popitem()
print(e)
print(vehicle)

# program 3

animals = {
    "legs":4,
    "color":"red"
}
animals.update({"cityFound":'sangamner'})
print(animals)

# program 4

info3 = {
    "firstName":"krupa",
    "lastName":"kotkar",
    "rollNo":2,
    "age":25
}

# for key in info3.keys():
    # print(key)

# for val in info3.values():
   # print(val)

for k,v in info3.items():
    print(k,v)
    


