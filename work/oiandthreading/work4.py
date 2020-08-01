s = input().split()

a = int(s[0])*60 + int(s[1])
b = int(s[2])*60 + int(s[3])

c =int((b-a)//60)
d = int((b-a)%60)
print('%d %d' % (c,d))