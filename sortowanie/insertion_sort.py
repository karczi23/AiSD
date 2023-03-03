from time import time
from list_gen import gen
# sortowanie przez wstawianie
# porównanie algorytmów, opisać dlaczego jest jeden szybszy od drugiego
input_list = gen(1000)

# print(input_list)
begin = time()

for i in range(1, len(input_list)):
    key = input_list[i]
    j = i - 1
    while j >= 0 and input_list[j] > key:
        input_list[j+1] = input_list[j]
        j -= 1
    input_list[j+1] = key


print(time() - begin)

print(input_list)
