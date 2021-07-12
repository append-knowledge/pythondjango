# def add(num1,num2):
#     print(num1+num2)
# add(55,88,55)
#if more number is used as arguments we use  *args method
def add(*args):
    sum=0
    for i in args:
        sum+=i
    print(sum)

add(4,5,6,78,23)                     #while using *args method it is saved as tuple for their sum iterate and add
