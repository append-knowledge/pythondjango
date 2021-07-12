x=""'`~!@#$%^&*()_-+=<>?/{}|\][":'''
y=input("enter a string ")
z=0
for i in y:
    if i in x:
        continue
    else:
        print(i,end="")