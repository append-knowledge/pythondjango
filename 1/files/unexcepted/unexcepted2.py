a=[1,2,3,5,4,5,88,455]
index_val=int(input('enter the index '))
try:
 print(a[index_val])
except Exception as e:
    print('exception is',e)
finally:
    print('bye')