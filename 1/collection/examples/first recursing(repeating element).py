x=input("enter a string ")
count=0
for i in x:
    count=x.count(i)
    if count > 1:
        break
print("first recursive element is",i)

            #OR


# d={}
# for i in x:
#     if i not in d:
#         d.update({i:1})
#     else:
#         print("first recursive element is",i)