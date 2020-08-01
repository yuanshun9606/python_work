import numpy as np
#

url = "iris.data"
# species = np.genfromtxt(url, delimiter=',', dtype='str', usecols=[4])
# np.random.seed(100)
# species_small = np.sort(np.random.choice(species, size=20))
# for val in np.unique(species_small):
#     print(species_small[species_small == val])
#     ## 分组

# np.random.seed(10)
# a = np.random.randint(20, size=10)
# print('a',a)
# print('a.srgsort()',a.argsort())
# print('a.argsort().argsort()',a.argsort().argsort())
# print('a[a.argsort()]', a[a.argsort()])
# np.random.seed(100)
# species_small = np.sort(np.random.choice(species,size=20))
# output = []
# uniqs = np.unique(species_small)
#
# for val in uniqs:
#     for s in species_small[species_small==val]:
#         # print(s)
#         # print(s==uniqs) # 20*3的二维数组
#         # argwhere 查找非0值得索引
#         groupid = np.argwhere(uniqs == s)[0][0]
#         output.append(groupid)
#
# # x = np.array([ True,False,False])
# # print(x)
# # print(np.argwhere(x))  --->  [[0]]
# print(output)
# print([np.argwhere(np.unique(species_small) == s)[0][0] for val in np.unique(species_small) for s in species_small[species_small==val]])

# np.random.seed(100)
# a = np.random.randint(0, 5, 10)
# unique_positions = np.unique(a, return_index=True)


# iris = np.genfromtxt(url,delimiter=',',dtype="object")
# numeric_column = iris[:,1].astype('float')
# grouping_column = iris[:,4]
#
# # print([[group_val,numeric_column[grouping_column==group_val].mean()]for group_val in np.unique(grouping_column)])
# output = []
# for group_val in np.unique(grouping_column):
#     output.append([group_val,numeric_column[grouping_column==group_val].mean()])

# a = np.array([1,2,3,4,5])
# b = np.array([4,5,6,7,8])
# print(a-b)
x = np.array([1, 2, 1, 1, 3, 4, 3, 1, 1, 2, 1, 1, 2])
n = 5
t = np.where(x==1)

b= np.datetime64('2020-06-08')
print(b)

print(np.busday_offset('2020-06-06',1,roll='forward'))
