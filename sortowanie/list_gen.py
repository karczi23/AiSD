from random import randint


def gen(length: int, lowest: int = 0, highest: int = 100):
    return [randint(lowest, highest) for i in range(length)]

