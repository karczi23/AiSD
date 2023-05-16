from time import time
from list_gen import gen
# ex1 przez wybieranie

input_list = gen(10)
print(input_list)

for j in range(len(input_list)-1):
    minimal = j
    for i in range(j+1, len(input_list)):
        if input_list[i] < input_list[minimal]:
            minimal = i

    input_list[j], input_list[minimal] = input_list[minimal], input_list[j]


print(input_list)
