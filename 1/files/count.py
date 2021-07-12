x=open('counting', 'r')

dict={}

for i in x:
    print(i)
    z=i.split(' ')
    for j in z:
        count=z.count(j)
        dict.update({j:count})
print(dict)