def recur_fun(n):
    if n<=1:
        return n
    else:
        return recur_fun(n-1)+recur_fun(n-2)
n=10
print("fibonacci series ")
for i in range(n):
    print(recur_fun(i))

recur_fun(n)


