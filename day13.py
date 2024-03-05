# program 1
# upper()
first_name = "krupa"
print(len(first_name))
e = first_name.upper()
print(e)

# lower()
last_name = "KOTKAR"
e2 = last_name.lower()
print(e2)

# isupper()
middle_name = "RAYBHAN"
e3 = middle_name.isupper()
print(e3)

e4 = e2.islower()
print(e4)
#lower(),upper(),islower(),isupper()
# program 2
city = "pune"
e5 = city.startswith("pu")
e6 = city.startswith("p")
print(e5)
print(e6)

e7 = city.endswith('e')
e8 = city.endswith('une')
print(e7)
print(e8)

city2 = "chandrapur"
e9 = city2.count('a')
print(e9)

# program 3
city3 = "wardha"
print(len(city3))
e10 = city3.lstrip()
print(e10)
print(len(e10))

city4 = "wardha"
print(len(city4))
e11 = city4.rstrip()
print(len(e11))

# program 4
info = "I am learing javascript"
e13 = info.replace("javascript","python")
print(e13)
print(info)

# program 5
e14 = "123".isdigit()#  0  -9
print(e14)

e15 = "1233#"
e16 = e15.isalpha()
print(e16)

e17 = e15.isalnum()
print(e17)

e18 = "hello"
e19 = "1234"
e20 = "h123"
e21 = "h12#"
print(e19.isalnum())
print(e20.isalnum())
print(e21.isalnum())

# revision
first_name = "krupa"
print(len(first_name))
#print(len(first_name.rstrip()))
#print(len(first_name.lsstrip()))
#print(len(first_name.strip()))

# program 3
last_name = "kotkar"
print(last_name.startswith("k"))
print(last_name.startswith("ko"))
print(last_name.startswith("Ko"))

print(last_name.endswith("r"))
print(last_name.endswith("ar"))
print(last_name.endswith("Kar"))

# program 4
marks = "123"
print(marks.isdigit())# 0-9
print(marks.isalpha())#A-Z a-Z
print(marks.isalnum())
print(type(marks))

# program 5
full_name = "a"
e3 = full_name.isspace()
print(e3)
# program 6
firstN  = "krupa"
e4 = firstN.capitalize()
print(e4)

e4 = "I AM LEARNING JAVASCRIPT"
print(e4.istitle())

# program 7
info = ["krupa","kotkar","7744087820"]
e5 = "@".join(info)
print(e5)

# program 8
email = "krupa@gmail.com"
e6 = email.split('@')#["krupa","gmail.com"]
print(e6)
