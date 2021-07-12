#num1 should be greater than num2 if num2>num1 inter change
def inter(func):
    def wrapper(num1,num2):
        if num2>num1:
            temp=num1                  #(num1,num2)=(num2,num1)             #if num2>num1
            num1=num2                  #return func(num1,num2)              #return num2-num1
            num2=temp
            return num1-num2
        else:
            return func(num1,num2)
    return wrapper

@inter
def sub(num1,num2):
    return num1-num2
print(sub(15,50))