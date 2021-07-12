x=[1,1,2,5,545,4555,33,22565,44,55,55,55,55]
y=[]
for i in x:
   if i not in y:
       y.append(i)
   else:
       print(i)

