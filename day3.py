
# logical operator
# and

# true and true ===> true
# false and true ===>false
# true and false ===> false
# false and false ===>false

print(5 == 5 and 7 == 7)
print(5 == 4 and 2 == 2)
print(4 == 4 and 6 == 7)
print(8 == 9 and 6 == 2)

# or
# true or true ===>true
# false or true ===>true
# true or false ===>true
# false or false ===>false

print(6 == 6 or 8 == 8)
print(5 == 2 or 1 == 1)
print(7 == 7 or 9 == 8)
print(9 == 7 or 9 == 6)


# not operator

# not true ---->False
# not false --->True
print(not 7 == 7)
print(not 8 == 8)
print(not 7 == 6)


# conditional statements

# one input and multiple outcomes
# numT > 0 and numT <= 5 ---- 10 % discount
# numT > 5 and numT <= 10 ---- 20 % discount
# numT > 10             ----- 30 % discount


# if condition:
#     statements

numT = 5

if numT > 0 and numT <= 5:
    print("10 % discount")
if numT > 5 and numT <= 10:
    print("20 % discount")
if numT > 10:
    print("30 % discount")


  # program 2
    
numT1 = -17
if numT1 >= 0 and numT1 <= 5:
    print("5 % discount")
elif numT1 > 5 and numT1 <= 10:
    print("10 % discount")
elif numT1 > 10:
    print("20 % discount")
else:
    print("incorrect input")

    # program 3
        
    # marks = 55

     #if marks > 90:
     #    print("Grade A")
     #if marks >= 75:
     #   print("Grade B")
     #if marks >= 65:
     #    print("Grade c")


    # program 4
        
    marks = 55

if marks > 90:
    print("Grade A")
elif marks >= 75:
     print("Grade B")
elif marks >= 65:
     print("Grade c")
else:
    print("try again ....!")

    
    # program 5
            
a = 10
b = 50

if a > b:
    print("a is greater")
else:
    print("b is greater")

# program 6
    
x1 = 1000
x2 = 5000
x3 = 15000

if x1 > x2 and x1 > x3:
    print("x1 is greater")
elif x2 > x1 and x2 > x3:
    print("x2 is greater")
else:
    print("x3 is greater")
    

  
