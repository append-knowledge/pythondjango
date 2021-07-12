min=int(input("enter the min value "))
max=int(input("enter the max value "))
sum=0
for i in range(min,max):
   if i>1:
      for a in range(2,i):
         if (i%a)==0:
            break
      else:
         print(i)
         sum+=i
print(sum)

