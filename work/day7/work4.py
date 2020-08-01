n = int(input())
a = []
for i in range(3):
    s = input().split()
    if ((n % int(s[0])) != 0):
        a.append(((n // int(s[0]) + 1) * int(s[1])))
    else:
        a.append((n // int(s[0])) * int(s[1]))

print(min(a))
