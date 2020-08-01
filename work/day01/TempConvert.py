tempStr = input("输入带符号的温度值：")

if tempStr[-1] in ['F', 'f']:
    c = (eval(tempStr[0:-1]) - 32) / 1.8
    print("转换后的温度是{:.2f}C".format(c))
elif tempStr[-1] in ['C', 'c']:
    F = 1.8 * eval(tempStr[0:-1]) + 32
    print("转换后的温度是{:.2f}F".format(F))
else:
    print("输入格式错误")

    # 注释
    # 缩进
 