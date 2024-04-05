# inheritance
#single inheritance
class Father:
    def _init_(self,fn,ln):
        self.firstName = fn
        self.lastName = ln

    def displayName(self):
        print(self.firstName + self.lastName)

class Son(Father):
    def _init_(self,fn,ln,sn):
        super()._init_(fn,ln)
        self.sname = sn 
    def displaySName(self):
         print(self.sname + self.lastName)
        
amol = Son("dilip","rao","amol")

print(amol.firstName)
print(amol.lastName)
amol.displayName()
amol.displaySName
# multi-level inheritance
class GrandFather:
    def _init_(self,fn,ln):
        self.firstName = fn
        self.lastName = ln
    
    def displayGName(self):
        print(self.firstName + self.lastName)

class Father(GrandFather):
    def _init_(self,fn,ln,ffn):
        super()._init_(fn,ln)
        self.sname = ffn 
    
    def displayFName(self):
        print(self.fName + self.lastName)


class Son(Father):
    def _init_(self,fn,ln,ffn,ssn):
        super()._init_(fn,ln,ffn)        
        self.sname = ssn 
    
    def displaySName(self):
        print(self.sName + self.lastName)

chinmayA = Son("manohar","deshpande","shirish","chinmay")
print(chinmayA,firstName)
print(chinmayA.lastName)
print(chinmayA.fname)
print(chinmayA.lastName)

chinmayA.displayFName()
chinmayA.displayGName()
chinmayA.displaySName()
