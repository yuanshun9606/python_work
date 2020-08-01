n =int(input())
f = [0]*1001
for i in range(1,n+1):
    for j in range(1,i//2+1):
        f[i] += f[j]
    f[i] += 1
print(f[n])