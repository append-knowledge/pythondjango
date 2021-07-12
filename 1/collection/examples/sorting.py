x=[25,45,89,77,55,33,22,-2,-5,-7,4258]

sorted=[]
for i in range(len(x)):
    min = x[0]
    for j in x:
        if j<min:
            min=j
    sorted.append(min)
    x.remove(min)
print(sorted)