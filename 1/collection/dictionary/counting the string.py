# count={}
# data="hello hii hello"
# words=data.split(" ")
# for i in words:
#     if i not in count:
#         count.update({i:1})
#     else:
#         val=int(count[i])
#         val+=1
#         count.update({i:val})
#
# print(count)
#
# x=input("enter")
# dict={}
# words=x.split(" ")
# for i in words:
#     count=words.count(i)
#     dict.update({i:count})
# print(dict)

x={'1':2,'3':8}
y={'k':1,'l':5}
x.update(y)
print(x)