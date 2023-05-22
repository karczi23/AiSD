from random import randint

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
        # self.create_dynamic_table()

    def generate_random_set(self):
        for i in range(self.num_items):
            self.size_cost_list.append((randint(1, self.max_size), randint(0, self.max_cost)))

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
                    print(self.size_cost_list[item - 1])
                    self.test_list.append(self.size_cost_list[item-1])
                    # print(item_offset, size_offset)
                    return item_offset, size_offset

    def greedy(self):
        greedy_list = []
        capacity_left = self.capacity
        capacity_list = []
        for item in range(self.num_items):
            greedy_list.append(self.size_cost_list[item][1]/self.size_cost_list[item][0])
            capacity_list.append(self.size_cost_list[item][0])

        while capacity_left >= min(capacity_list):
            greedy_index = self.hit_the_greedy(greedy_list)
            if capacity_list[greedy_index] > capacity_left:
                capacity_list[greedy_index] = self.max_size
                greedy_list[greedy_index] = 0
                continue
            self.greedy_optimal_set.append(greedy_index+1)
            capacity_left -= capacity_list[greedy_index]
            capacity_list[greedy_index] = self.max_size
            greedy_list[greedy_index] = 0

    def hit_the_greedy(self, greedy_list):
        max_greedy = max(greedy_list)
        for i in range(len(greedy_list)):
            if greedy_list[i] == max_greedy:
                return i

for i in range(1):
    bag = Ship(randint(1, 1000), randint(1, 1000), randint(1, 1000), randint(1, 1000))
    # bag = Ship(5, 10, 10, 10)
    # bag.size_cost_list = [(5, 6), (4, 3), (3, 2), (2, 5), (5, 4)]
    print(bag.size_cost_list)
    bag.greedy()
    print(bag.greedy_optimal_set)
    # print(bag.size_cost_list)
    # bag.create_dynamic_table()
    # print(*bag.dynamic_table, sep="\n", end="\n\n")
    # bag.optimal_set_dynamic_table()
    # print(bag.optimal_set)
    # if sum(x[0] for x in bag.test_list) <= bag.capacity and sum(x[1] for x in bag.test_list) == bag.dynamic_table[bag.num_items][bag.capacity]:
    #     print("correct")
    # else:
    #     print("wrong")
    #     input("Press ENTER to continue")