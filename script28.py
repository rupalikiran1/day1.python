# program 1
#compile time error

print("hello")
try:
    e = int(input("enter the number A"))
    f = int(input("enter the number B"))
    print(e/f)
except ArithmeticError:
    print("please enter correct input")
else:
    print("hello i will run")
finally:
    print("i will always execute")
    print("bye")
    