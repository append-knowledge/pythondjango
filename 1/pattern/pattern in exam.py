x=int(input('enter the starting range '))
y=int(input('enter the ending range '))
r=5
for i in range(x,y):
     if i%2==0:
         for j in range(r,0,-1):
             for e in range(0,r):
                 if e<=j:
                     print(i,end=" ")
             print()
     else:
         for l in range(0,r):
             for m in range(0,l+1):
                 if m<=l:
                     print(i,end=" ")
             print()