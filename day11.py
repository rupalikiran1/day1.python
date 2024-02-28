x = 10
print(x)

first_name = "krupali"
print(type(first_name))

last_name = "kotkar"
print(type(last_name))


middle_name = """
krupa
"""
info = '''
i am learning
python
'''
print(info)

# program 2

city = "pune"
# 0 1 2 3
# p u n e
print(city[0])
print(city[1])
#print(city[5])

# program 3
city4 = "sangamner"
#  0 1 2 3 4 5 6 7 8
 # s a n g a m n e r
# -10 -9 -8 -7 -6 -5 -4 -3 -2 -1

# strint[StartIndex,EndIndex(not included),StepSize]
e = city4[5 : :]
print(e)
e2 = city4[-7::]
print(e2)
e3 = city4[1:7:]
print(e3)
e4 = city4[1:-2:]
print(e4)
e5 = city4[-7:-2:]
print(e5)
e6 = city4[-7:9:]
print(e6)
e7 = city4[::-1]
print(e7)
e8 = city4[-1:-4]
print(e8)

# program 4
# upper()
city = "nagpur"
e9 = city.upper()
print(e9)

# lower()
city2 = "pune"
e10 = city2.lower()
print(e10)

# count()
city3 = "chandrapur"
e11 = city3.count('a')
print(e11)
