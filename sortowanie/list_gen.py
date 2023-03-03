from random import randint, random, uniform, choices
import string
import time

# unsigned int generator
def usintgen(length: int, lowest: int = 0, highest: int = 100):
    return [randint(lowest, highest) for _ in range(length)] if lowest >= 0 else None

def intgen(length: int, lowest: int = -100, highest: int = 100):
    return [randint(lowest, highest) for _ in range(length)] if highest >= lowest else None

def usfloatgen(length: int, lowest: int = 0, highest: int = 100):
    return [random() * highest for _ in range(length)] if lowest >= 0 else None

def floatgen(length: int, lowest: int = -100, highest: int = 100):
    return [uniform(lowest, highest) for _ in range(length)] if highest >= lowest else None

def strgen(length: int, strlen = 20, isUTF = False):
    if not isUTF:
        return [''.join(choices(string.ascii_letters + string.digits, k=strlen)) for _ in range(length)]
    else:
        return [''.join(choices([chr(i) for i in range(32, 0x110000) if chr(i).isprintable()], k=strlen)) for _ in range(length)]        
# print(usintgen(50))
# print(intgen(50))
# print(usfloatgen(50))
# print(floatgen(50))

start = time.perf_counter()
# print(strgen(1000000))
print(strgen(100, 20, True))
print((time.perf_counter() - start)*1000)
