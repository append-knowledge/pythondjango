tup=(1,2.5,23,2.75,555)
a,b,c,d,e=tup
sum=a+b+c+d+e
print(sum)

print()
#indexing  sliceing  reversing
print(tup[0])
print(tup[4])
print(tup[1:4])
print(tup[::-1])


print()
#count and index
tup5=(1,2,3,5,'fjj','hii','hii','hii')
print(tup5.count('hii'))
print(tup5.index('hii'))