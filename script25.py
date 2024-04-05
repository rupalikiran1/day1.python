#class Calculator:
 #   def addition(self,x,y):
  #      print(x+y)
   # 
    #def addition(self,x,y,z):
     #   print(x+y+z)
#def addition(self,x,y,z,a):
     #   print(x+y+z+a)
# def addition(self,x = None , y = None , z= None , a = None):
#if(x != None and y != None and z != None and a != None):
#print(x+y+z+a)
#elif(x != None and y != None and z != None):
#print(x+y+z)
#elif(x != None and y != None):
#print(x+y)
#cal = calculator()
#cal.addition(23,4)
#cal.addition(23,4,5)
#cal.addition(23,4,5,5)
 #program 3

class Dog:
    def talk(self):
        print("Bhow bhow")

class Human:
    def talk(self):
        print("Hello hi")
    
class Duck:
    def sound(self):
     print("quack quack")
    
def call_talk(obj):
    if hasattr(obj,'talk'):
        obj.talk()
    else:
        obj.sound()
    a = Human()
    b = Dog()
    c = Duck()

# program 4

class WorkBank:
    def loan(self):
        print("i am loan from WB")
    def save(self):
        print("i am save from WB")
    
class SBI(WorkBank):
    def loan(self):
        print("i am loan from SBI")
        super().loan()
    def save(self):
        print("i am save from SBI")
        super().loan()

class PNB(WorkBank):
    def loan(self):
        print("i am loan from SBI")
        super().loan()
    def save(self):
        print("i am save from SBI")
        super().save()
a = SBI()
a.loan()
a.save()
