from matplotlib import pyplot as plt

file_data = []
with open("results.txt") as f:
    for line in f:
        file_data.append(list(map(float, line.split())))

print(file_data)

plt.plot([x[0] for x in file_data], [x[1:] for x in file_data], label="Dynamic")
plt.xlabel("Size of the problem")
plt.ylabel("Time of execution")
plt.title("Dynamic vs Greedy")
plt.legend(["Dynamic", "Greedy"])
# plt.yscale("log")
plt.show()
