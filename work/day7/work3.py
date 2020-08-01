global Save
Save = 0  # 存款
Pack = 300  # 零花钱
global T
T = 0


def main():
    global Save
    global T
    flag = 0  #
    for i in range(12):
        a = int(input())
        Money = Pack - a  # 每月剩的钱= 300 - 花销
        T += Money  # 手里的钱 = 上个月剩的+ 这个月剩的
        while T >= 100:
            Save += 100
            T -= 100
        if ((T < 0) & (flag == 0)):
            flag = 1
            print('-%d' % (i + 1))

    if (flag == 0):
        print(int(Save + (Save * 0.2) + T))


if __name__ == '__main__':
    main()
