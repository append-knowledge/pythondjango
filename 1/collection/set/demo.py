#to store elements
#does not store duplicates
#doesnot store in the order that we input
set1={1,1,2,5,89,73,854,55,5,73,89}
print(set1)
print(type(set1))

#to insert an empty set use set()
#set is hetrogenious type so can store different type of data
#set is mutable data collection ie updation can be made

s1=set()
s1.add("hello")
s1.add(2.3)
s1.add(20)
s1.add(True)
print(s1)

set1={1,2,3,4,5,6,7,8,9,0}
print

#in set nesting is not possible
s3={1,1,2,{2,5,6}}
print(s3)