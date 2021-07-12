x=int(input("ENTER THE NUMBER "))
if x>0:
    fact = 1
    for i in range(1, x + 1):
        fact = fact * i
    print(fact)
elif x==0:
    print("factorial is zero")
else:
    print("factorial only for positive integer.Please enter a positive integer ")