# bank
# class level variable - country
# constructor - fn,ln,accno transaction
# deposit() , withdrawl()
# static - total accounts
# class level for name change

class Bank:

    country = "India"
    count = 0
    def _init_(self,fn,ln,acc,bal):
        self.firstName = fn
        self.lastName = ln
        self.accNo = acc
        self.balance = bal
        self.transaction = []
        Bank.count = Bank.count + 1
    
    def deposit(self,amount):
        self.balance = self.balance + amount
        self.transaction.append(amount)

    def withdrawl(self,amount):
        if(self.balance > amount):
            self.balance = self.balance - amount
            self.transaction.append(-amount)
        else:
            print("insufficient balance")
    
    def lastFiveTransaction(self,x):
        return self.transaction[-x::]
    
    @classmethod
    def changeCountry(cls,cl):
        cls.country = cl
    
    @staticmethod
    def objCount():
        return Bank.count
  
  
amol = Bank("amol","rao",123,1000)
raj = Bank("raj","rao",123,1000)
sarika = Bank("sarika","pansare",123,1000)
chinmay = Bank("chinmay","deshpande",123,100000)
krupa = Bank("krupa","kotkar",123,100000000)

print(Bank.objCount())
amol.withdrawl(100000)
amol.deposit(3000000)
amol.deposit(30000)
amol.deposit(3000)
amol.deposit(30)
amol.deposit(3)
print(amol.lastFiveTransaction(2))
