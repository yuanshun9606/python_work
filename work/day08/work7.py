import string

str = (input() + input() + input() + input()).upper()
ddd = {i: str.count(i) for i in string.ascii_uppercase}  # 用字典统计每个字母的个数
for i in range(max(ddd.values()), 0, -1):
    print(" ".join("*" if ddd[alphabet] >= i else " " for alphabet in string.ascii_uppercase))
print(" ".join(list(string.ascii_uppercase)))








# dict = {chr(ii) : str.count(chr(ii)) for ii in range(65, 91)} #用字典统计每个字母的个数
