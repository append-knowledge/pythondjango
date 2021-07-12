x=input("enter a word ")
y=x[::-1]
if y in x:
    print("you entered a palindrom ")
else:
    print("not a palindrom",y)
