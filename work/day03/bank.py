# 余额宝

yuebao_lixi = 0.6873 / 10000  # 余额宝每日利息

benjing =int(input("本金"))
yuebao_result = yuebao_result1 = benjing
year = 365
time = 98      # 周期
zhouqishu = 4  # 周期数

for i in range(1, year):
    yuebao_result += yuebao_result * yuebao_lixi

for i in range(1, time * zhouqishu):
    yuebao_result1 += yuebao_result1 * yuebao_lixi

str1 = "余额宝"
print(str1.center(50, "*"))
print(f"时间：{year}天")
print(f"总计：{int(yuebao_result)}元 \n总收益：{int(yuebao_result - benjing)}元")
print(f"时间：{time * zhouqishu}天")
print(f"总计：{int(yuebao_result1)}元 \n总收益：{int(yuebao_result1 - benjing)}元")

str2 = "平安"
print(str2.center(50, "*"))
pingan_lixi = 0.039/365
pingan_result = pingan_result1 = benjing

for i in range(1, zhouqishu):
    pingan_result += pingan_result * pingan_lixi * time

print(f"时间{time * zhouqishu}天")
print(f"总计：{int(pingan_result)}元 \n总收益：{int(pingan_result - benjing)}元")