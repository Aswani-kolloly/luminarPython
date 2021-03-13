class Bank:

    def withdraw(self):
        print("inside withdraw")
    def __deposit(self):#private, can hide method
        print("inside deposit")
    def mcall(self):
        self.__deposit()
    def bal_enq(self):
        print("inside balance enq")
class Atm(Bank):
    pass
ob=Bank()
ob.mcall()
ob._Bank__deposit()

ob2=Atm()
ob2.mcall()
ob2._Atm__deposit()