class Atm(object):
    def __init__(self,CashWithdrawl, BalanceEnquiry):
       
        self.CashWithdrawl = CashWithdrawl 
        self.BalanceEnquiry = BalanceEnquiry

    def withdrawl(self):
        print("money is out") 
    def balance(self): 
        print("money is still in there")
   
money = Atm(20000,9000000)

print(money.withdrawl())
print(money.balance()) 