#if there is condition and if all input has corresponding output we can use map
#map(function,iterable)

# def square(num):
#     return num**2
#
# lst1=[1,2,3,4,5,6,7,8,9,10]
# x=list(map(square,lst1))
# print(x)



products=[
    {"item_name":"boost","mrp":290,"stock":50},
    {"item_name":"complan","mrp":240,"stock":10},
    {"item_name":"bournvita","mrp":320,"stock":20},
    {"item_name":"horlicks","mrp":280,"stock":13},
    {"item_name":"nutricharge","mrp":275,"stock":0},]


name=list(map(lambda product:product['item_name'],products))
print(name)

