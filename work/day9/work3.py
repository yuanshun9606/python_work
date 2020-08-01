from math import sqrt
from itertools import combinations


def main():
    a = input().split()
    b = list(map(int, input().split()))
    cont = 0
    for i in list(combinations(b, int(a[1]))):
        if is_prime(sum(i)):
            cont += 1
    print(cont)


def is_prime(n):
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


if __name__ == '__main__':
    main()
