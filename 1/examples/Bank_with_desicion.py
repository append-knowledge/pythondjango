ava=10000
print("BALANCE IS ",ava)
amt=int(input("ENTER THE AMOUNT REQUIRED "))
if amt<=ava:
    print("YOUR AVAILABLE BALANCE IS",ava-amt)
else:
    print("INSUFFICIENT BALANCE")