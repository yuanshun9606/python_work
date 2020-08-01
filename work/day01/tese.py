numbers_strings = ("1", "2", "3", "4", "5")


def print_str(first, *second):
    print(first)
    print(second)


if __name__ == "__main__":
    print_str(*numbers_strings)  # 注意这里的*numbers_strings
