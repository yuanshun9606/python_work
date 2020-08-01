def fun(s):
    result = 1
    for i in s:
        result *= ord(i) - 64
    return result


def main():
    a = input()
    b = input()
    if fun(a) % 47 == fun(b) % 47:
        print("GO")
    else:
        print("STAY")


if __name__ == '__main__':
    main()
