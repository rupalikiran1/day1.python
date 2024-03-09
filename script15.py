setA = {1,2,3}
setB = {11,22,33}
setC = setA.union(setB)
print(setC)

setE = {11,33,44}
setF = {44,55,66}
#setG = setE.intersection(setF)
#print(setG)

#setE.intersection_update(setF)
setF.intersection_update(setE)
print(setE)
print(setF)

# program 2

setQ = {11,22,33}
setE = {45,66,77,33}

setR = setQ.symmetric_difference(setE)
print(setR)
setQ.symmetric_difference_update(setE)
print(setQ)
print(setE)

# program 3
setX = {11,22,33}
setY = {45,66,77,33}
setZ = setX.difference(setY)
print(setZ)
setX.difference_update(setY)
print(setX)
setY.difference_update(setX)
print(setY)

# program 4
setM = {11,22,33}
setN = {11,22,33,44}
O = setM.issubset(setN)
O2 = setN.issuperset(setM)
print(O)
print(O2)

# program 5
setR = {11,22,33,44,88}
setK = {55,66,77,88}
P = setR.isdisjoint(setK)
print(P)

# program 6
setU = {11,22,33,44}
setU.add(55)
print(setU)

#setU.clear()
#print(setU)

setU.pop()
setU.remove(44)
print(setU)

setU.update({5,6,7,8,3})
print(setU)

r = setU.discard(56)
print(setU)
