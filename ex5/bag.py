from random import randint
from time import time_ns
# import matplotlib.pyplot


class Ship:
    def __init__(self, num_items=5, capacity=10, max_size=100, max_cost=100):
        self.num_items = num_items
        self.capacity = capacity
        self.max_size = max_size
        self.max_cost = max_cost
        self.size_cost_list = []
        self.dynamic_table = [[0 for _ in range(self.capacity + 1)] for _ in range(self.num_items + 1)]
        self.optimal_set = []
        self.test_list = [] # (item_size, item_cost)
        self.greedy_optimal_set = []

        self.generate_random_set()
        self.create_dynamic_table()

    def generate_random_set(self):
        for i in range(self.num_items):
            # self.size_cost_list.append((randint(1, self.max_size), randint(0, self.max_cost)))
            self.size_cost_list.append((time_ns()%1000+1, randint(0, self.max_cost)))
    def create_dynamic_table(self):
        for item in range(1, self.num_items + 1):
            for size in range(1, self.capacity + 1):
                item_size = self.size_cost_list[item-1][0]
                if item_size <= size:
                    self.dynamic_table[item][size] = max([self.dynamic_table[item-1][size], self.dynamic_table[item-1][size-item_size] + self.size_cost_list[item-1][1]])
                else:
                    self.dynamic_table[item][size] = self.dynamic_table[item-1][size]


    def optimal_set_dynamic_table(self):
        item_offset = self.num_items+1
        size_offset = self.capacity+1
        biggest_cost = max([max([x for x in self.dynamic_table[y][:size_offset]]) for y in range(len(self.dynamic_table[:item_offset]))])
        # print(biggest_cost)
        while biggest_cost > 0:
            item_offset, size_offset = self.get_biggest_cost(biggest_cost, item_offset, size_offset)

            # new_list = [[x for x in self.dynamic_table[y][:size_offset]] for y in
            #             range(len(self.dynamic_table[:item_offset]))]
            # print()
            # print(*new_list, sep="\n", end="\n")
            biggest_cost = max([max([x for x in self.dynamic_table[y][:size_offset]]) for y in range(len(self.dynamic_table[:item_offset]))])
            # print(biggest_cost)

    def get_biggest_cost(self, biggest_cost, item_offset, size_offset):
        # print(biggest_cost)
        for item in range(len(self.dynamic_table[:item_offset])):
            for size, cost in enumerate(self.dynamic_table[item][:size_offset]):
                if cost == biggest_cost:
                    self.optimal_set.append(item)
                    item_offset = item
                    size_offset = size - self.size_cost_list[item - 1][0] + 1
                    # print(self.size_cost_list[item - 1])
                    self.test_list.append(self.size_cost_list[item-1])
                    # print(item_offset, size_offset)
                    return item_offset, size_offset

    # def greedy(self):
    #     greedy_list = []
    #     capacity_left = self.capacity
    #     capacity_list = []
    #     for item in range(self.num_items):
    #         greedy_list.append(self.size_cost_list[item][1]/self.size_cost_list[item][0])
    #         capacity_list.append(self.size_cost_list[item][0])
    #
    #     while capacity_left >= min(capacity_list):
    #         greedy_index = greedy_list.index(max(greedy_list))
    #         # if the most valuable item has no value brake
    #         if greedy_list[greedy_index] == 0:
    #             break
    #         # if item is to big to fit in the ship change its value to 0
    #         if capacity_list[greedy_index] > capacity_left:
    #             capacity_list[greedy_index] = self.capacity+1
    #             greedy_list[greedy_index] = 0
    #             continue
    #         # add item to the ship
    #         self.greedy_optimal_set.append(greedy_index+1)
    #         capacity_left -= capacity_list[greedy_index]
    #         capacity_list[greedy_index] = self.capacity+1
    #         greedy_list[greedy_index] = 0

    def greedy(self):
        greedy_list = []
        capacity_left = self.capacity
        for item in range(self.num_items):
            greedy_list.append([item + 1, self.size_cost_list[item][1]/self.size_cost_list[item][0]])

        greedy_list.sort(key=lambda x: x[1], reverse=True)

        for item in greedy_list:
            if item[1] == 0:
                break
            if self.size_cost_list[item[0]-1][0] <= capacity_left:
                self.greedy_optimal_set.append(item[0])
                capacity_left -= self.size_cost_list[item[0]-1][0]
# # parameters
# ship_capacity = 1000
# num_containers = 1000
# max_container_size = 100
# max_container_cost = 100
#
# start_size = 10
# repeats = 1
# step = 100
# num_steps = 15
#
# output = []
# # time of execution
# for i in range(num_steps):
#     tested_size = start_size + i * step
#     dynamic_time = 0
#     greedy_time = 0
#     for j in range(repeats):
#         ship = Ship(tested_size, ship_capacity, max_container_size, max_container_cost)
#         ship.create_dynamic_table()
#
#         start = time_ns()
#         ship.create_dynamic_table()
#         ship.optimal_set_dynamic_table()
#         end = time_ns()
#         dynamic_time += end - start
#
#         start = time_ns()
#         ship.greedy()
#         end = time_ns()
#
#         greedy_time += end - start
#
#     print(f"Dynamic time: {dynamic_time/repeats}")
#     print(f"Greedy time: {greedy_time/repeats}")
#     output.append([tested_size, dynamic_time/repeats, greedy_time/repeats])
#
# print(*output, sep="\n", end="\n")
#

# diffrent item size test

# parameters
ship_capacity = 1000
max_container_size = 1000
max_container_cost = 1000

start_size = 100
repeats = 3
step = 100
num_steps = 20

output = []
# time of execution
for i in range(num_steps):
    tested_size = start_size + i * step
    dynamic_time = 0
    greedy_time = 0
    # shi = Ship(tested_size, ship_capacity, max_container_size, max_container_cost)
    # del ship
    for j in range(repeats):
        ship = Ship(tested_size, ship_capacity, max_container_size, max_container_cost)
        print(ship.num_items, ship.capacity)
        # ship.capacity = 10
        # ship.num_items = 5
        # ship.size_cost_list = [(5, 6), (4, 3), (3, 2), (2, 5), (5, 4)]
        start = time_ns()
        ship.greedy()
        end = time_ns()
        # ship.create_dynamic_table()
        greedy_time += end - start
        # print(ship.greedy_optimal_set)
    # print(f"Dynamic time: {dynamic_time/repeats}")
    print(f"Greedy time: {greedy_time/repeats}")
    # output.append([tested_size + i, dynamic_time/repeats, greedy_time/repeats])
    output.append([tested_size, greedy_time/repeats])

print(*output, sep="\n", end="\n")
with open("results.txt", "w") as f:
    for line in output:
        f.writelines(f"{line[0]} {line[1]}\n")
# plt.plot([x[0] for x in output], [x[1:] for x in output], label="Dynamic")
# plt.xlabel("Size of the problem")
# plt.ylabel("Time of execution")
# plt.title("Dynamic vs Greedy")
# plt.legend(["Dynamic", "Greedy"])
# # plt.yscale("log")
# plt.show()


# for i in range(1):
#
#     bag = Ship(randint(1, 1000), randint(1, 1000), randint(1, 1000), randint(1, 1000))
#     # bag = Ship(5, 10, 10, 10)
#     # print(bag.size_cost_list)
#     start = time_ns()
#     bag.create_dynamic_table()
#     bag.get_biggest_cost()
#     end = time_ns()
#     bag.greedy()
#
#     print(bag.greedy_optimal_set)
#     # print(bag.size_cost_list)
#     # bag.create_dynamic_table()
#     # print(*bag.dynamic_table, sep="\n", end="\n\n")
#     # bag.optimal_set_dynamic_table()
#     # print(bag.optimal_set)
#     # if sum(x[0] for x in bag.test_list) <= bag.capacity and sum(x[1] for x in bag.test_list) == bag.dynamic_table[bag.num_items][bag.capacity]:
#     #     print("correct")
#     # else:
#     #     print("wrong")
#     #     input("Press ENTER to continue")

# x_values = [x[0] for x in output]
# y_values = [x[1:] for x in output]
#
# for y_set in y_values:
#     plt.plot(x_values, y_set)
# plt.plot([x[0] for x in output], [x[1:] for x in output], label="Dynamic")
# plt.xlabel("Size of the problem")
# plt.ylabel("Time of execution")
# plt.title("Dynamic vs Greedy")
# plt.legend(["Dynamic", "Greedy"])
# # plt.yscale("log")
# plt.show()
