x=open('counting2', 'r')
dict={}
for i in x:
    print(i)
    words=i.rstrip('\n').split(' ')
    print(words)
    for j in words:
        count=i.count(j)
        dict.update({j:count})
print(dict)