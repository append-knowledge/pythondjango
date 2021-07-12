lst=[111,22,3,4,555,6]
lst.sort()
print(lst)

lst.sort(reverse=True)
print(lst)

#in args it is saved as tuple and in **kwargs it is stored as tuple

users={
    1000:{"acconu_num":1000,"password":"user1","balance":3000},
    1001: {"acconu_num": 1001, "password": "user2", "balance": 4000},
    1002: {"acconu_num": 1002, "password": "user2", "balance": 5000},
    1003: {"acconu_num": 1003, "password": "user3", "balance": 6000} }


def authentication(**kwargs):    #kwargs={'account_no':1000,'password':'test1}
    user=kwargs['account_no']
    password=kwargs['password']
    if user in users:
        if password==users[user]['password']:
            print('sucess')
        else:
            print('invalid')



authentication(account_no=1000,password='test1')
