import time


def decorate(fun):
    def warappeer(*args,**kwargs):
        print('正在启动校验----')
        time.sleep(2)
        print('校验完成')
        fun(*args,**kwargs)

    return warappeer


@decorate
def f1():
    print('------f1---------')


def f2():
    print('------f2---------')

f1()
f2()


'''
装饰器套外
第一层接收参数
第二层接收函数
第三层接收函数的参数
'''