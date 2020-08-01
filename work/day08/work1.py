n =int(input())
s = list(map(int,input().split()))
con = 1
a = []
for i in range(n-1):
    if s[i] < s[i+1]:
        con +=1
        a.append(con)
    else:
        a.append(con)
        con = 1
print(max(a))