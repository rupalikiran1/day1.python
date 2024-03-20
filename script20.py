# class person:
#fields or properties
# first_name = "krupa"
# last_name = "kotkar"

# instance
# def walk(self):
# print("I am Walking")

# def talk(self):
#print("I am talking")

# krupa = person()
#print(krupa.first_name)
#print(krupa.last_name)
#krupa.walk()
#krupa.talk()

# amol = person()
#print(amol.first_name)
#print(amol.last_name)
#amol.walk()
#amol.talk()

# amol.first_name = "amol"
# amol.last_name = "rao"

#print(amol.first_name)
#print(amol.last_name)

# program 2
class PersonB:
    #constructor
    def _init_(self,fn,In):
       self.first_name = fn
       self.last_name = ln
  
    def talk(self):
      print("I am talking")

    def walk(self):
       print("I am walking")
amol = PersonB("amol","rao")
krupa = PersonB("krupa","kotkar")

print(amol.first_name)
print(amol.last_name)


print(krupa.first_name)
print(krupa.last_name)
krupa.city = "pune"
print(krupa.city)
#print(amol.city)

