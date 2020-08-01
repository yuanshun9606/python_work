s= input().split()

cont = 0
for i in range(1,int(s[0])+1):
    if(s[1] in str(i)):
        cont += str(i).count(s[1])
print(cont)