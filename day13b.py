strA = "amol"
print(strA)
print(type(strA))

names = ["krupa","sona","mona"]
print(names)
print(type(names))

info = {
    "firstname":"krupa",
    "lastname":"kotkar"
}
print(info)
print(type(info))

# program B
flowers = ["lily","lotus","jasmine"]
flowerB = ("lily","lotus","rose")
flowers[0]="rose"
print(flowers)
#flowerB[1]="sunflower"

# program c
# does tuple stores the value by index?
# how to define tuple

tupleA = ("A","B","C")
print(tupleA)
print(type(tupleA))
print(tupleA[0])

# for with range
for item in tupleA:
    print(item)

# for without range
for item in tupleA:
    print(item)

#program d
tupleB=12,23
print(type(tupleB))
#tupleB[0]=88

tupleC = (11,22,33)
a,b,c=tupleC
print(a)
print(b)
print(c)

# program E
d = (11,22,33,44,44)
print(d)
e2 = d.count(44)
print(e2)

e3 = d.index(22)
print(e3)
print(33 in d)

# program f
tupleF = (11,22,33)
len(tupleF)
e = list(tupleF)
print(e)
e.append(44)
e = tuple(e)
print(e)

# how to create tuple with constructor
e4=([11,22,33],[33,44,55],[55,66,77])
