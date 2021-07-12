x=input("enter a word ")
y=input("enter the next word ")
for i in x:
    if i not in y:
        print(i)
for j in y:
    if j not in x:
        print(j)
