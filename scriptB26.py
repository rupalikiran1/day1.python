# program 1
#with open('info4.txt','w') as f:
 #   f.write("I am learning js")
  #  f.write("I am learning python")

# program 2
#user defined data type

import pickle
class Emp:
    def __init__(self,fn,ln,email,age):
          self.firstName = fn
          self.lastName = ln
          self.email = email
          self.age = age
    def displayDetails(self):
         print(self.firstName)
         print(self.lastName)
         print(self.email)
         print(self.age)
f = open('student.dat','wb')#file open
n = int(input('Enter the number of objects')) #2
for x in range(n):
     fn = input("enter firstName")
     ln = input("enter lastName")
     email = input("enter email")
     age = input("enter age")
     e = Emp(fn,ln,email,age)
     pickle.dump(e,f)
     f.close()
     