
a = [0]*2001
c = [6, 2, 5, 5, 4, 5, 6, 3, 7, 6]
a[0]=6
n = int(input())
count = 0
for i in range(1,2001):
    j = i
    while j>=1:
        a[i] += c[j%10]
        j = j//10
for i in range(1000):
    for j in range(1000):
        if a[i]+a[j]+a[i+j]+4 == n:
            count += 1

print(count)
