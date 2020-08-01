a = []
b = []
flag = 0
for i in range(7):
    a.append(input().split())
    b.append(int(a[i][0]) + int(a[i][1]))
    if ((b[i] > 8) & (flag == 0)):
        flag += 1
        print(i + 1)

if (flag == 0):
    print(0)
