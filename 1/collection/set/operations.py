s1={1,2,3,4,88,5,9,7}
s2={1,2,3,85,95,65,}
print("s1 is ",s1)
print("s2 is ",s2)
#union ie total
print("union is ",s1.union(s2))

#intersection ie common
print("intersection of set is ",s1.intersection(s2))

#difference
print("difference of s1 in s2 is ",s1.difference(s2))
print("difference of s2 in s1 is ",s2.difference(s1))