# #if conditions are there we use filter insted of map
# #filter(function,iterable)
#
# lst1=[1,2,3,44,55,88,6]
# even=list(filter(lambda num1:num1%2==0,lst1))
# print(even)
# odd=list(filter(lambda num1:num1%2!=0,lst1 ))
# print(odd)
#
#
# #print out of stock product
#
# products=[
#     {"item_name":"boost","mrp":290,"stock":50},
#     {"item_name":"complan","mrp":240,"stock":10},
#     {"item_name":"bournvita","mrp":320,"stock":20},
#     {"item_name":"horlicks","mrp":280,"stock":13},
#     {"item_name":"nutricharge","mrp":275,"stock":0},]
#
# out_stock=list(filter(lambda product:product['stock']==0,products))
# print(out_stock)
#
#
# #product mrp below 250
# item=list(filter(lambda product:product['mrp']<=250,products))
# print(item)

#
#
# lst=[2,3,4,8,10,7]
# #below 5==>num-1    else==>num+1
#
# lst2=list(map(lambda num:num+1 if num>5 else num-1,lst))
# print(lst2)




lst=[2,3,4,5,5,8,10,7]
#below 5==>num-1    greater than 5 ==>num+1  5 when it is 5
lst3=list(map(lambda num1:num1+1 if num1>5 else num1-1 if num1<5 else num1,lst))
print(lst3)