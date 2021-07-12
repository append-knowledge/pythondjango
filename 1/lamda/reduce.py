from functools import reduce
lst=[1,2,3,5,55,2,88]

total=reduce(lambda num1,num2:num1+num2,lst)
print(total)


product=reduce(lambda num1,num2:num1*num2,lst)
print(product)


difference=reduce(lambda num1,num2:num1-num2,lst)
print(difference)

largest=reduce(lambda num1,num2:num1 if num1>num2 else num2,lst)
print(largest)


products=[
    {"item_name":"boost","mrp":290,"stock":50},
    {"item_name":"complan","mrp":240,"stock":10},
    {"item_name":"bournvita","mrp":320,"stock":20},
    {"item_name":"horlicks","mrp":280,"stock":13},
    {"item_name":"nutricharge","mrp":275,"stock":0},]
prices=list(map(lambda price:price['mrp'],products))
print(prices)
high_price=reduce(lambda p1,p2:p1 if p1>p2 else p2,prices)
print(high_price)