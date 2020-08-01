def decorator(fun):
    a = 100
    print('wrapper外层')
    def wrapper():
        fun()
        print("装修1")
        print("装修2")
        print("装修3")
    print('加载完成')
    return wrapper


@decorator
def house():
    print("我是毛坯房······")


# house()

'''
未调用时也会装饰器加载函数
将装饰函数作为参数传递给装饰器
执行decorator函数
将返回值又赋给house 
'''