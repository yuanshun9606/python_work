input()
s = set(map(int, input().split(' ')))
print(len(set(a+b for a in s for b in s if a!=b).intersection(s)))

'''
set() 建立一个集合 不包含重复元素
{}.intersection() 表示交集
a+b 双层遍历构建一个新集合
'''