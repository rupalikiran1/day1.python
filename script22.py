
class Person:
    #constructor
    def _init_(self,fn,ln):
        #instance variables
        self.firstName = fn
        self.lastName = ln

    #instance method
    def displayName(self):
        print(self.firstName + self.lastName)
    # lastNameUpdate
    def updateName(self,ln):
        self.lastName = ln

    chinmay = Person("chinmay","deshpande")
    print(chinmay.firstName)
    print(chinmay.lastName)
    chinmay.displayName()
    chinmay.updateName("dani")
#class instance , class method


class personB:
    country = "India"

    #constructor
    def _init_(self,fn,ln):
        #instance variables
        self.firstName = fn
        self.lastName = ln
    
    # instance method
    def updateName(self,fn,ln):
        self.firstName = fn
        self.lastName = ln

    # class method
    @classmethod
    def updateCountry(cls,cnty):
        cls.country = cnty
    h = personB("Hrushali","patil")
    print(h.firstName)
    print(h.lastName)
    print(h.country)
    h.country = "bharat"
    h2 = personB("Hrushali2","patil2")
    print(h2.country)
    personB.updateCountry('india B')
    print(h.country)
    print(h2.country)
    #static mathod
    #count number of objects

class personC:
    count = 0
    country = "Bharat"
    def __init__(self,fn,ln):
      self.firstName = fn
      self.lastName = ln
      personC.count = personC.count + 1

    def displayName(self):
        print(self.firstName+self.lastName)

    @classmethod
    def updateCountry(cls,cnty):
        cls.country = cnty
    @staticmethod
    def countObj():
        return personC.count
amol = personC("amol","rao")
raj = personC("raj","kumar")

a = personC.countObj()
print(a)
#bank class
