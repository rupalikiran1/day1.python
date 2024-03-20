
#class Person:
 # def _init_(self,fn,ln):
  #      self.firstName = fn
   #     self.lastName = ln

    #def display_name(self):
     #   print(self.firstName + self.lastName)

#mona = Person("mona","kotkar")
#krupa = Person("rupali","gund")
#print(mona.firstName)
#print(krupa.firstName)
#print(krupa.lastName)
#print(mona.lastName)
#krupa.display_name()
#mona.display_name()

# program 2
class Person2():
    country = "bharat"
    def _init_(self,fn,ln):
        self.firstName = fn
        self.lastName = ln
    def displayName(self):
        print(self.firstName + self.lastName)

        @classmethod
        def changeCountry(cls,cnty):
            cls.country = cnty
amol = Person2('amol','rao')
chinmay = Person2("chinmay","deshpande")
ninad = Person2("ninad","dani")

print(amol.firstName)
print(amol.lastName)
print(amol.country)
amol.country = "india"
print(amol.country)
print(chinmay.country)
print(ninad.country)
Person2.changeCountry("Hindustan")
print(amol.country)
print(chinmay.country)
print(ninad.country)
