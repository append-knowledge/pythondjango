que=[]
size=int(input('enter the range:: '))
front=0
rear=0
n=0
def insert():
    global front,rear,size,que
    if rear>=size:
        print('queue is full ')
    else:
        a=int(input("enter the number "))
        que.insert(rear,a)
        rear+=1
    for i in range(front,rear):
        print(que[i])
def delete():
    global front,rear,size,que
    if rear==front:
        print("queue is empty ")
    else:
        front+=1
    for i in range(front,rear):
        print(que[i])
while n!=1:
    opt=int(input("1)insert \n2) delete  "))
    if opt==1:
        insert()
    elif opt==2:
        delete()
    else:
        print('check the number you have dialed ')


