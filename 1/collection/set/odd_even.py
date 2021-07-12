s1={0,1,2,3,4,5,77,55,88,66,54,75,89,12,45}
even=set()
odd=set()
for i in s1:
    if i==0:
        continue
    elif i%2==0:
        even.add(i)
    else:
        odd.add(i)
print(s1)
print("even set is ",even)
print("odd set is ",odd)