#first in first out
# insertion........enqueue
# deletion.........dequeue



def enqueue():
    global top,size
    if top>size:
        print('the queue is full ',queue)
    else:
        a=int(input('enter the number to be enqueued '))
        queue.append(a)
        top+=1
def dequeue():
    global top,size
    if top<=0:
        print('queue is empty ',queue)

    else:
        a=queue[0]
        queue.remove(a)
        top-=1
def display():
    print(queue)


queue=[]
size=int(input('enter the length of queue '))
top=1
while size>=len(queue):
    opt=int(input('1) enqueue 2) dequeue 3)display '))
    if opt==1:
        enqueue()
    elif opt==2:
        dequeue()
    elif opt==3:
        display()
print(queue)

