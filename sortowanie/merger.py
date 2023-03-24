from statistics import mean
from math import ceil

data = []
nr_results = 10
len_results = 20



for i in range(1, nr_results):
    arr = []
    with open(f"results{i}.txt") as f:
        file = f.read().splitlines()
        file.pop(0)
        for line in file:
            tmp = line.split()
            tmp.pop(0)
            arr.append([int(x) for x in tmp])
        data.append(arr)

newdata = []
for k in range(3):
    for j in range(len_results):
        newdata.append(int(mean([data[i][j][k] for i in range(nr_results-1)])))


tmp = []
to_print = []
for k in range(len_results):
    tmp.append(newdata[k])
    tmp.append(newdata[k + 20])
    tmp.append(newdata[k + 40])
    # tmp.append(newdata[k + 180])
    to_print.append(tmp)
    tmp = []
with open("results_qs_merged.txt", "w") as f:
    f.write("Len right middle random\n")
    for i, a in enumerate(to_print):
        f.write(str(ceil((i + 1) / 3)*1000)+" ")
        match i%1:
            case 0:
                f.write("")
            case 1:
                f.write("")
            case 2:
                f.write("")
            case 3:
                f.write("const ")
            case 4:
                f.write("v-shape ")
        f.write(" ".join(str(x) for x in a))
        f.write("\n")