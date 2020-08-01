n = int(input())
li = list(map(int, input().split())).sort()
s = [0] * n   #标记
cont = 0
for i in range(n - 1):
    for j in range(i + 1, n - 1):
        if ((li[i] + li[j]) in li):
            a = li.index(li[i] + li[j])
            if s[a] == 0:
                cont += 1
                s[a] = 1
print(cont)
