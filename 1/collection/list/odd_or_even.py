lst=[1,2,3,4,5,88,55,44,57,25,34,52]
odd=[]
even=[]
for i in lst:
    if i%2==0:
        even.append(i)
    else:
        odd.append(i)
print("The list is ",lst)
print("The even numbers in the list",even)
print("The odd numbers in the list",odd)