from abc import ABC, abstractmethod

class Payment(ABC):
    @abstractmethod
    def paymethod(self,money):
        return f"default payment , direct cash :{self.money}"



class UPI(Payment):
    
    def paymethod(self,money):
        self.money=money
        return f"payment done by UPI: {self.money}"
    
class DebitCard(Payment):
    def paymethod(self,money):
        self.money=money
        return f"payment done by CARD: {self.money}"
    
class Directcash(Payment):
    def paymethod(self, money):
        pass
    

p2=UPI()
print(p2.paymethod(500))
p3=DebitCard()
print(p3.paymethod(600))
# p4=Directcash()
# print(p4.paymethod(800))