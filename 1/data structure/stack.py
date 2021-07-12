#Last in first out
stack=[]
top=0
n=0
size=int(input('Enter the size of stack '))
def push():
    global top,size
    if top>size:
        print('the stack is full ')
    else:
        a=int(input('enter the numberto be pushed '))
        stack.append(a)
        top+=1
def pop():
    global top,size
    if top<=0:
        print('stack is empty ')
    else:
        stack.pop()
        top-=1
def display():
    print(stack)

while n!=1:
    a=int(input('1)push  2)pop   3)display '))
    if a==1:
            push()
    elif a==2:
             pop()
    elif a==3:
            display()
    n=int(input('press 1 to exit'))
