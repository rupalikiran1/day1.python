#program 1
#names = ["krupa","sarika","poorva","om"]
#print(names)
# program 2
#info = {
 #   "firstName":"om",
 #   "lastName":"kotkar",
  #  "rollNo":"12",
  #  "age":"12"
#}

# program 3
#numbers = (11,22,33,44)
#program 4
#h = "krupa"
# program 5
#listA = [11,22,33,44,33]
#print(listA)
#program 6
#info = {
 #   "firstName":"rupa",
 #   "lastName":"kotkar",
#    "age":24,
 #   "age":22
#}
#print(info)
#lastName="rupa"
#print(lastName)

#set
setA = {11,22,33,44}
print(type(setA))

# allow duplicate values
setB = {11,22,33,44,44,55,55}
print(setB)
print(len(setB))
# stores the value by index??
#print(setB[0])
for i in setB:
    print(i)
# program 2
setC = {11,22,33,44,55}
setC.add(66) 
print(setC)

setC.pop()
print(setC)
setC.remove(22)
print(setC)