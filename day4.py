
# loops ? ?

# type of loops

# 1. while loops()
# 2 .for loops()

# for()
# range()


#for x in range(StartIndex,EndIndex(not included),StepSize)
   # Statements

# print(0 to 9)
for x in range(10): # if StartIndex not Mentioned by default zero is default
    print(x)

# print(2 to 9)
for x in range(2,10):
    print(x)

# print(1 to 5)
for x in range(1,6):
     print(x)


# table of two
#2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19   
for x in range(2,20,1):
    print(x)

# 2,4,6,8,10,12,14,16,18,20
for x in range(2,21,2):
    print(x)

# table of three
    
for x in range(3,31,3):
    print(x)

# table of five in reverse
    
for x in range(50,4,-5):
    print(x)


# table of 10 in reverse
    
for x in range(100,9,-10):
    print(x)


# break statement with for loop
    

for x in range(1,6):
    print(x)


for x in range(1,6):#2, #3
    if x == 3:
        break
    print(x) # 1, # 2

for x in range(1,6):#2,#3
    print(x)#1,#2,#3
    if x == 3:
        break

# program 9
# continue with for loop
    
for x in range(1,6): #2 #3 #4 #5
    if x == 3:
        continue
    print(x) #1 #2 #4 #5
    


# program 10
    
for x in range(6,1,-1):
    if x == 3:
        continue
    print(x)
    


    


      







