from datetime import datetime
class Bank:
    bank_na="HDFC"   #static or class variable
    def __init__(self,name,id,amt,min_bal):
        self.name=name
        self.acnt_id=id
        self.amt=amt
        self.min_balance=min_bal

    def info(self):
        print(datetime.today(),self.name,self.acnt_id,self.amt,self.min_balance,Bank.bank_na)
    def deposit(self,amt):
        self.amt+=amt
    def withdraw(self,amt):
        tot=self.amt-amt
        if tot>self.min_balance:
            self.amt-=amt
        else:
            print("cant withdraw")
    def balance_enq(self):
        print(self.amt)
ob=Bank('Abhi',4874984,50000,1500)
ob.info()
ob.deposit(2000)
ob.info()
ob.withdraw(51000)
ob.balance_enq()
