def check(func):            #check is decorator name
    def wrapper(name,age):
        if age<18:
            print(name,'not eligible for vaccination ')
        else:
            return func(name,age)
    return wrapper
@check

def vaccine(name,age):
    print(name,'eligible for vaccination ')
vaccine('lijo',27)   #when we call the function it first goes to decorator

@check
def eligibility_check(name,age):
    print(name,'eligible for vaccination ')
eligibility_check('lija',10)