'''
数组类 ndarry
ndarry.nidm 数组的轴的个数 rank
ndarray.shape 维数
ndarray.size 元素总数 shape的元素乘积

'''

import numpy as np

# a = np.arange(15).reshape(3, 5)
# print(type(a))
# b = np.array([6, 7, 8])
# print(type(b))
# print(b.dtype)
# b = np.array([(1, 2, 3), (4, 5, 6)])
# print(b.shape)

# a = np.zeros((3,4),dtype=np.int32)
# print(a)
# print(a.dtype)

# a = np.arange(10, 30, 5) # 这里5是步长
# print(type(a))
# b = np.linspace(0, 2, 9) #这里9是新数组元素个数
# print(b)

# 协方差https://www.cnblogs.com/weiyinfu/p/10693445.html


# x = [-2.1, -1,  4.3]
# y = [3,  1.1,  0.12]
# X = np.stack((x, y))
# print(X)
#
# x = [1, 2, 3]
# y = [4, 5, 6]
# print(np.cross(y,x))

import  numpy as np
arr1 = np.arange(3)
arr2 = np.arange(3,7)
arr3 = np.arange(7,10)
array_of_arrays = np.array([arr1, arr2, arr3])
print(np.array([a for arr in array_of_arrays for a in arr]))