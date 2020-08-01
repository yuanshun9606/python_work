a = "[[1,2], [3,4], [5,6], [7,8], [9,0]]"
print(type(a))
b = eval(a)
print(type(b))
age = 18
print(eval("{'name':'linux','age':age}", {"age": 1822}, locals()))
