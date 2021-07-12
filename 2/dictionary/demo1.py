users={
    1000:{"acconu_num":1000,"password":"user1","balance":3000},
    1001: {"acconu_num": 1001, "password": "user2", "balance": 4000},
    1002: {"acconu_num": 1002, "password": "user2", "balance": 5000},
    1003: {"acconu_num": 1003, "password": "user3", "balance": 6000} }

 #to check password of accountnumber
def check(account_no,password):
     if account_no in users:
         if (password==users[account_no]['password']):
             print('success')
         else:
             print('wrong password ')


check(1000,'user1')


#to get the balance
def balance(account_no):
    if account_no in users:
        print(users[account_no]['balance'])
    else:
        print('invalid accountnumber')

balance(1000)