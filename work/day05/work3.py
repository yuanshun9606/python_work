class Person(object):

    def __init__(self, name, age):
        self._name = name
        self._age = age

    @property
    def name(self):
        return self._name

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, age):
        self._age = age

    def play(self):
        if self._age <= 16:
            print("玩个锤子")
        else:
            print('玩鸡鸡')


def main():
    person = Person('王大锤', 12)
    person.play()
    person.age = 18
    person.play()


if __name__ == '__main__':
    main()