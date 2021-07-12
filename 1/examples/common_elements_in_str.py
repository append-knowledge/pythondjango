x=input("enter the first word ")
y=input("enter the second word ")
for i in x:
    if i in y:
        print(i)
else:
     print("not found")