
# list
#             0        1      2      3       4
# names = ["krupali","sona","mona","alka","krupali"]
# retrive
# print(names[0])
# update
# names[0] = "tanmay"
# add
# names.append("omi")
# names.insert(2,"shiv")
# delete
# names.pop()
#names.pop(1)
# names.remove("krupali")
# in
# print("tanmay" in names)

# program 2
info = ["krupali","kotkar",25,2]
info2 = {
    #"key":value
    #property: value
    "firstName":"krupali",
    "lastName":"kotkar",
    "age":25,
    "rollno":2
}
# print(info2[0])
# retrive
e = info2["firstName"]
print(e)

# update
info2["firstName"] = "mona"
print(info2)

# add
info2["city"] = "pune"
print(info2)

# delete
info2.pop("firstName")
print(info2)

# program 2
vehicle = {
    "color":"red",
    "type":"sedane",
    "color":"white"
}
print(type(vehicle))

# len()
print(len(vehicle))

# in 
print("color" in vehicle)

# duplicate keys
print(vehicle)

# retrive
vehicle['color']
vehicle['color'] = "red"
vehicle['regno'] = "123"
