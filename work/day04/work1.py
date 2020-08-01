import os
import time


def main():
    content = '北京欢迎你为你开天辟地…………'

    # 清理屏幕上的输出
    os.system('cls')  # os.system('clear')
    print(content)
    print(content[1:])
    # 休眠200毫秒


if __name__ == '__main__':
    main()
