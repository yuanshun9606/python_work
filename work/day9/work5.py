from math import sqrt


def is_prime(n):
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


def is_huiwen(n):
    n = str(n)
    if n == n[::-1]:
        return True
    else:
        return False


s = input().split()
r = min(9989900, int(s[1]))
for i in range(int(s[0]), r):
    if is_huiwen(i):
        if is_prime(i):
            print(i)
