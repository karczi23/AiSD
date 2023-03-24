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
for k in range(1):
    for j in range(60):
        newdata.append(int(mean([data[i][j][k] for i in range(9)])))

tmp = []
to_print = []
for k in range(60):
    tmp.append(newdata[k])
    # tmp.append(newdata[k + 60])
    # tmp.append(newdata[k + 120])
    # tmp.append(newdata[k + 180])
    to_print.append(tmp)
    tmp = []
with open("results_qs_merged.txt", "w") as f:
    f.write("Len Pivot Time\n")
    for i,a  in enumerate(to_print):
        f.write(str(ceil((i + 1) / 3)*1000)+" ")
        match i%3:
            case 0:
                f.write("right ")
            case 1:
                f.write("middle ")
            case 2:
                f.write("random ")
            case 3:
                f.write("const ")
            case 4:
                f.write("v-shape ")
        f.write(" ".join(str(x) for x in a))
        f.write("\n")