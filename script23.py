# program 1
# single inheritance
# parent - constructor , child no constructor

#class student:
#   def _init_(self,fn,ln,adharNo):
#       self.firstName = fn
#       self.lastName = ln
#        self.adharNo = adharNo

#   def displayName(self):
#   print(self.firstName + self.lastName)

# amol = student("amol","rao","123")
#print(amol.firstName)
#print(amol.lastName)
#print(amol.adharNo)
#amol.displayName()

#class Teacher(student):
#salary = 100000
#def displaySalary(self):
#   print(self.Salary)

#amolT = Teacher("amolT","raoT","123")
#print(amol.firstName)
#print(amol.lastName)
#print(amol.adharNo)
#print(amolT.salary)
#amol.displayName()
#amol.displaySalary()

# program 2
#single inheritance
#class students:
#def _init_(self,fn,ln,adharNo):
#       self.firstName = fn
#       self.lastName = ln
#        self.adharNo = adharNo

 # def displayName(self):
#   print(self.firstName + self.lastName)
#class Teacher(student):
#   def _init_(self,fn,ln,adharNo,salary):
#     super()._init_(fn,ln,adharNo)
#      self.salary = salary

#  def displaySalary(self):
#    print(self.salary)

#chinmayT = Teacher("chinmay","deshpande",123,7744087820)
#print(chinmayT.firstName)
#print(chinmayT.laststName)
#print(chinmayT.adharNo)
#print(chinmayT.Salary)

##amol.displayName()
#amol.displaySalary()

# program 3
# multi-level
class Student:
    def _init_(self,fn,ln,adharNo):
        self.firstName = fn
        self.lastName = ln
        self.adharNo = adharNo
    
    def displayName(self):
        print(self.firstName + self.lastName)
    
class Teacher(Student):
    def _init_(self,fn,ln,adharNo,salary):
        super()._init_(fn,ln,adharNo)
        self.salary = salary

    def displaySalary(self):
        print(self.salary)

class professor(Teacher):
    def _init_(self,fn,ln,adharNo,salary,spec):
        super()._init_(fn,ln,adharNo,salary)
        self.special = spec
    def displaySpecialization(self):
        print(self.special)
  
    bharat = professor("bharat","bhate",213,1454552,"hindi")
    print(bharat.firstName)
    print(bharat.lastName)
    print(bharat.adharNo)
    print(bharat.salary)
    print(bharat.special)
    
    bharat.displayName()
    bharat.displaySalary()
    bharat.displaySpecialization()