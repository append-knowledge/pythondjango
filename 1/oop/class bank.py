class Bank():
    def setval(self,name,account_no,bank_name,balance):
        self.name=name
        self.account_no=account_no
        self.bank_name=bank_name
        self.balance=balance

    def withdraw(self,amt):
        self.amt=amt

        if self.amt>self.balance:
            print('insufficent balance')
        else:
            self.balance -= self.amt
            print('your balance in bank is',self.balance)
    def depo(self,amt):
        self.amt=amt
        self.balance+=self.amt
        print(self.amt,'has been creadted to your account')
        print('your aval balance is',self.balance)
    # def print(self):
    #     print(self.name,self.account_no,self.bank_name,self.balance)
    #     # print(self.account_no)
    #     # print(self.bank_name)
    #     # print(self.balance)
obj1=Bank()
name=input('enter the name ')
account_no=int(input('enter the account number '))
bank_name=(input('enter the bank name '))
balance=int(input('enter the balance '))
obj1.setval(name,account_no,bank_name,balance)
obj1.withdraw(4000)
obj1.depo(1000)







