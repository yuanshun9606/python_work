# -*- coding: <kakui> -*-

# str1 = input("输入一个人的名字:")
#
# str2 = input("输入一个国家名字:")
#
# print("世界那么大，{}想去{}看看".format(str1, str2))

# n = input("输入整数N：")
# sum = 0
# for i in range(int(n)):
#     sum+= i + 1
# print("1到N求和结果：",sum)

# sum, tem = 0, 1
# for i in range(1, 15):
#     tem *= i
#     sum += tem
# print("远算结果是:", sum)
# print("远算结果是:{}".format(sum))
#
# n = 1
# for i in range(5,0,-1):
#     n = (n+1)<<1
# print(n)
diet = ['西红柿', '黄瓜', '牛排', '虾仁']
for x in range(0, 4):
    for y in range(0, 4):
        if not (x == y):
            print("{}{}".format(diet[x], diet[y]))
