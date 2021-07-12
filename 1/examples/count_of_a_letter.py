x=input("enter a word ")
y=input("enter the letter you want to count ")
k=0
for i in x:
    if i in y:
        k+=1
print("letter repeated for",k,"times")
