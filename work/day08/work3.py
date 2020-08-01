ISBN = input()
strNum = ISBN[:12]
Sum = 0
j = 1
for i in strNum:
    if i != '-':
        n = int(i)
        Sum = Sum + n * j
        j += 1
if Sum % 11 == 10:
    ID = 'X'
else:
    ID = str(Sum % 11)
if ID == ISBN[12]:
    print("Right")
else:
    strNum = strNum + ID
    print(strNum)
