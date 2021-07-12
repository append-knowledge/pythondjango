s1={1,2,3,4,5,77,88,99,100,55,44,6,200}
s2={1,2,3,4,5,35,100,200}
s3=set()
for i in s1:
    if i in s2:
        s3.add(i)
print("common elements are ",s3)