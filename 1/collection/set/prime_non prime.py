s1={1,2,3,4,5,7,8,9,14,13,11,21,17,19}
prime=set()
nonprime=set()
for i in s1:
    for j in range(2,i):
        if (i%j)==0:
            nonprime.add(i)
            break
    else:
        prime.add(i)
print("prime number is ",prime)
print("non prime numbers are",nonprime)