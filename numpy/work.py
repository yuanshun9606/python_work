import numpy as np
from  numpy import pi

# x= np.linspace(0,2*pi,100)
# print(np.sin(x))



# x= np.arange(1,19).reshape(3,2,3)
# # print(x)
# # # print(np.mean(x,2))
# # print(x.reshape((-1,3)))
# p= np.poly1d([1,2],True)
#
# print(p.r)
# url = "iris.data"
# iris = np.genfromtxt(url, delimiter=',', dtype='object')
# petal_len_setosa = iris[iris[:, 4] == b'Iris-setosa',[2]]
# print(petal_len_setosa)
np.random.seed(100)
arr = np.random.randint(1,11,size=(6, 10))
# print(arr)

def counts_of_all_values_rowwise(arr2d):
    # Unique values and its counts row wise
    num_counts_array = [np.unique(row, return_counts=True) for row in arr2d]
    x = [[int(b[a==i]) if i in a else 0 for i in np.unique(arr2d)] for a, b in num_counts_array]
    # Counts of all values row wise
    return(x)


counts_of_all_values_rowwise(arr)


