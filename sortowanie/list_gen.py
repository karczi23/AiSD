from random import randint, random, uniform, choices
import string
import time

# unsigned int generator
def usintgen(length: int, lowest: int = 0, highest: int = 100):
    return [randint(lowest, highest) for _ in range(length)] if lowest >= 0 else None

#signed int generator
def intgen(length: int, lowest: int = -100, highest: int = 100):
    return [randint(lowest, highest) for _ in range(length)] if highest >= lowest else None

#unsigned float generator
def usfloatgen(length: int, lowest: int = 0, highest: int = 100):
    return [random() * highest for _ in range(length)] if lowest >= 0 else None

#signed float generator
def floatgen(length: int, lowest: int = -100, highest: int = 100):
    return [uniform(lowest, highest) for _ in range(length)] if highest >= lowest else None

#string generator (ASCII or UTF8)
def strgen(length: int, strlen = 20, isUTF = False):
    if not isUTF:
        return [''.join(choices(string.ascii_letters + string.digits, k=strlen)) for _ in range(length)]
    else:
        utf8_letters = [chr(i) for i in range(32, 0x110000) if chr(i).isprintable()]
        return [''.join(choices(utf8_letters, k=strlen)) for _ in range(length)]    
    

# unsigned int reversed? sorted generator
def usintgen(length: int, lowest: int = 0, highest: int = 100, reverse = False):
    unsorted = [randint(lowest, highest) for _ in range(length)] if lowest >= 0 else None
    return sorted(unsorted, reverse=reverse)

#signed int reversed? sorted generator
def intgen(length: int, lowest: int = -100, highest: int = 100, reverse = False):
    unsorted = [randint(lowest, highest) for _ in range(length)] if highest >= lowest else None
    return sorted(unsorted, reverse=reverse)

#unsigned float reversed? sorted generator
def usfloatgen(length: int, lowest: int = 0, highest: int = 100, reverse = False):
    unsorted = [random() * highest for _ in range(length)] if lowest >= 0 else None
    return sorted(unsorted, reverse=reverse)

#signed float reversed? sorted generator
def floatgen(length: int, lowest: int = -100, highest: int = 100, reverse = False):
    unsorted = [uniform(lowest, highest) for _ in range(length)] if highest >= lowest else None
    return sorted(unsorted, reverse=reverse)

#string generator reversed? sorted (ASCII or UTF8)
def strgen(length: int, strlen = 20, isUTF = False, reverse = False):
    if not isUTF:
        unsorted = [''.join(choices(string.ascii_letters + string.digits, k=strlen)) for _ in range(length)]
    else:
        utf8_letters = [chr(i) for i in range(32, 0x110000) if chr(i).isprintable()]
        unsorted = [''.join(choices(utf8_letters, k=strlen)) for _ in range(length)]       
    return sorted(unsorted, reverse=reverse)

start = time.perf_counter()
# print(strgen(1000000))
print(strgen(100, 20))
print((time.perf_counter() - start)*1000)
