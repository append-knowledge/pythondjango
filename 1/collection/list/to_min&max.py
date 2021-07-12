x=[55,88,775,664,582,46,45,52]
max=x[0]
min = x[0]
for i in x:
    if i>max:
        max=i
for j in x:
     if j<min:
        min=j

print("minimum number is ",min)
print("maximum number is ",max)