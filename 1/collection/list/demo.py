x=[1,2,3,1,2,3,"hello",True,22.3]
print(x)
# allows repetation of data
# heterogenous
# keeps order

#to add elements
x.append(8)
x.append(15)
print(x)

#to remove elements
x.remove(3)
print(x)

#to clear the lst
x.clear()
print(x)

#to delete the entire list
# del x
# print(x)


#in list nesting is posible
l1=[1,2,2,[5,6,4],[45,8,5]]
print(l1)

#for iteration
l2=[[1,2,3],[4,5,6]]
for i in l2:
    print(i)
    for j in i:
        print(j)



x=[1,2,3,5,4,5,4,88,544]
#to print the element in indexvalue
print(x[1])
print(x[6])

#to print the length
print(len(x))

#to change the element of given index value
x[2]=55
print(x)

#To slice the list
lst6=[1,2,3,4,55,45,22,55,44,5,87]
print(lst6[1])
print(lst6[0:5])
print(lst6[:8])
print(lst6[1:])
print(lst6[0:8:2])


#to remove last element
lst7=[1,2,5,44,77,88]
lst7.pop()
print(lst7)