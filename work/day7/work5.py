"""深度优先搜索"""

a = [0] * 10
book = [0] * 10

def dfs(step):
    global a, book
    a1 = (a[1] * 100 + a[2] * 10 + a[3])
    if (step == 10):
        a2 = (a[4] * 100 + a[5] * 10 + a[6])
        a3 = (a[7] * 100 + a[8] * 10 + a[9])
        if ((a1 * 2 == a2) & (a1 * 3 == a3)):
            print("%d%d%d %d%d%d %d%d%d" % (a[1], a[2], a[3], a[4], a[5],
                                            a[6], a[7], a[8], a[9]))

    for i in range(1, 10):
        if (book[i] == 0):
            a[step] = i      # 将数字i放入第step个盒子中
            book[i] = 1      #表示数字i已经使用
            if( step<4 | a1<399):
                dfs(step + 1)    #递归调用自己
            book[i] = 0      #收回自己的数字


def main():
    dfs(1)


if __name__ == '__main__':
    main()
