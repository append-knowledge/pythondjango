def admin_require(func):
    def wrapper(user,pin):
        if user!='admin':
            raise Exception ('only admin is allowed')
        else:
            return func(user,pin)
    return wrapper
@admin_require
def change_pin(user,pin):
    mypin=pin
    return mypin
@admin_require
def del_acno(user,acno):
    return str(acno)+ 'deleted'

print(change_pin('admin',65485))
print(del_acno('admin',55555555555))