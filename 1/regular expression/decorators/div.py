def decorator_div(func):
    def  wrapper(n1,n2):
        if n2>n1:
            n1,n2=n2,n1
        return n1/n2
    return wrapper

@decorator_div
def div(n1,n2):
    return(n1/n2)

print(div(10,200))