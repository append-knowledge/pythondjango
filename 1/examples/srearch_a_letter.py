x=input("enter the word ")
y=input("enter the letter you want to find ")
flag=0
for i in x:
    if i in y:
         flag=1
if flag==1:
    print("entered word found ")
else:
    print("not found")