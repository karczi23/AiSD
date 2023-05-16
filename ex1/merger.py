from statistics import mean
from math import ceil

data = []

for i in range(1, 10):
    arr = []
    with open(f"results{i}.txt") as f:
        file = f.read().splitlines()
        file.pop(0)
        for line in file:
            tmp = line.split()
            tmp.pop(0)
            tmp.pop(0)
            arr.append([int(x) for x in tmp])
        data.append(arr)
newdata = []
for k in range(4):
    for j in range(100):
        newdata.append(int(mean([data[i][j][k] for i in range(9)])))

tmp = []
to_print = []
for k in range(100):
    tmp.append(newdata[k])
    tmp.append(newdata[k + 100])
    tmp.append(newdata[k + 200])
    tmp.append(newdata[k + 300])
    to_print.append(tmp)
    tmp = []
with open("results_merged.txt", "w") as f:
    f.write("Len Type IS SS HS MS\n")
    for i,a  in enumerate(to_print):
        f.write(str(ceil((i + 1) / 5)*1000)+" ")
        match i%5:
            case 0:
                f.write("rand ")
            case 1:
                f.write("inc ")
            case 2:
                f.write("dec ")
            case 3:
                f.write("const ")
            case 4:
                f.write("v-shape ")
        f.write(" ".join(str(x) for x in a))
        f.write("\n")