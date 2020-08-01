from functools import lru_cache


@lru_cache(maxsize=128,typed=False)
def fun(n):
    if n == 1: return 1
    result = 0
    for i in range(1,(n//2)+1):
        result += fun(i)
    return result+1


def main():
    n = int(input())
    print(fun(n))


if __name__ == '__main__':
    main()
