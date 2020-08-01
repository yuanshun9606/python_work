def fun(num):
    result = 1
    for n in range(1,num+1):
        result *= n
    return result

m = int(input('m= '))
n = int(input("n= "))
print(fun(m))
print(fun(m)//fun(n)//fun(m-n))
