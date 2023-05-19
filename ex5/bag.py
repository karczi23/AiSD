from random import randint

class Bag:
    def __init__(self, num_items=5, capacity=10, max_size=100, max_weight=100):
        self.num_items = num_items
        self.capacity = capacity
        self.max_size = max_size
        self.max_weight = max_weight
        self.size_list = []
        self.cost_list = []

    def generate_random_set(self):
        for i in range(self.num_items):
            self.size_list.append(randint(0, self.max_size))
            self.cost_list.append(randint(0, self.max_weight))

    def dynamic(self):
        pass


bag = Bag(5, 10)