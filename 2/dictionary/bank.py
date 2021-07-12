class Bank():
    users = {
        1000: {"acconu_num": 1000, "password": "user1", "balance": 3000},
        1001: {"acconu_num": 1001, "password": "user2", "balance": 4000},
        1002: {"acconu_num": 1002, "password": "user2", "balance": 5000},
        1003: {"acconu_num": 1003, "password": "user3", "balance": 6000}}
    session={}

    def authenticate(self,**kwargs):  #**kwargs forms a dictionry
        account_no=kwargs['account_no']
        password=kwargs['password']
        user=self.check(account_no)
        if user:
            if (password==self.users[account_no]['password']):
                self.session['user']=account_no
                return account_no
            else:
                return -1 #invalid password
        else:
            return 0  #invalid username

    def check(self, account_no):
        if account_no in Bank.users:
            return True
        else:
            return False

    def min_balance(self,account_no):
        if (account_no==self.session['user']):
            print(self.users[account_no]['balance'])
        else:
            print('you must login')
    def fund_transfer(self,user,to_account_no,amt):
        if self.check(to_account_no):
            balance=self.users[user]['balance']
            if balance < amt:
                print('insufficient balance')
            else:
                self.users[user]['balance']-=amt
                self.users[to_account_no]['balance']+=amt
    def log_out(self):
        self.session['user']=0
        print('successfully loggedout')

obj=Bank()
user=obj.authenticate(account_no=1000,password='user1')
if (user==-1)|(user==0):
    print('failed')
else:
    obj.min_balance(user)
obj.fund_transfer(user,1002,500)
obj.min_balance(user)
obj.log_out()