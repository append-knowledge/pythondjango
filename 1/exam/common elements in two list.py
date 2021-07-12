a=[1,5,64,22,77,88,5,645]
b=[1,5,8,77]
common=[]
for i in a:
    if i in b:
        common.append(i)
print("common elements are ",common)