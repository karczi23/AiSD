import random
from random import shuffle, choice, randint
from time import time_ns
from copy import deepcopy
import networkx as nx
import matplotlib.pyplot as plt

# generate undirected graph
class Graph:
    def __init__(self, saturation, num_nodes):
        self.saturation = saturation
        self.num_nodes = num_nodes
        self.num_edges = int(self.num_nodes * (self.num_nodes - 1) / 2 * self.saturation)
        self.adjacency_matrix = [[0 for _ in range(self.num_nodes)] for _ in range(self.num_nodes)]
        self.odd_nodes = []
        self.hamilton_cycle = []
        self.euler_cycle = []
        self.num_edges_graph = self.num_edges
        self.generate_adjacency_matrix()
        self.adjacency_matrix_copy = deepcopy(self.adjacency_matrix)
        self.not_found = True

    # generate adjacency matrix for connected graph that is Eulerian and Hamiltonian
    def generate_adjacency_matrix(self):
        # generate ring graph with random node order
        nodes = [i for i in range(self.num_nodes)]
        shuffle(nodes)
        for i in range(self.num_nodes):
            self.adjacency_matrix[nodes[i]][nodes[(i + 1) % self.num_nodes]] = 1
            self.adjacency_matrix[nodes[(i + 1) % self.num_nodes]][nodes[i]] = 1

        # add random triangles
        while sum([sum(node) for node in self.adjacency_matrix]) / 2 < self.num_edges:
            # choose three random nodes
            three_nodes = random.sample(range(self.num_nodes), 3)

            # if there is no edge any of the two nodes, add edge between them
            if self.adjacency_matrix[three_nodes[0]][three_nodes[1]] == 0 and \
                self.adjacency_matrix[three_nodes[0]][three_nodes[2]] == 0 and \
                self.adjacency_matrix[three_nodes[1]][three_nodes[2]] == 0:
                self.adjacency_matrix[three_nodes[0]][three_nodes[1]] = 1
                self.adjacency_matrix[three_nodes[1]][three_nodes[0]] = 1
                self.adjacency_matrix[three_nodes[0]][three_nodes[2]] = 1
                self.adjacency_matrix[three_nodes[2]][three_nodes[0]] = 1
                self.adjacency_matrix[three_nodes[1]][three_nodes[2]] = 1
                self.adjacency_matrix[three_nodes[2]][three_nodes[1]] = 1

        # update number of edges
        self.num_edges = sum([sum(node) for node in self.adjacency_matrix]) // 2

    def find_hamilton_cycle(self, vertex=0):
        self.hamilton_cycle.append(vertex)
        # find all possible neighbours that are not in hamilton cycle
        possible_neighbours = list(set([i for i, x in enumerate(self.adjacency_matrix[vertex]) if x == 1]).difference(self.hamilton_cycle))
        for neighbour in possible_neighbours:
            # return multiple cycles
            self.find_hamilton_cycle(neighbour)

        # if all nodes are in hamilton cycle and last node has edge to first node
        if len(self.hamilton_cycle) == self.num_nodes \
                and self.hamilton_cycle[0] in \
                [x for x, i in enumerate(self.adjacency_matrix[self.hamilton_cycle[-1]]) if i == 1]:
            print("cykl znaleziony")
            self.hamilton_cycle.append(self.hamilton_cycle[0])
            for node in self.hamilton_cycle:
                print(f"{node}", end=" -> ")
            print(f"{self.hamilton_cycle}")
            self.hamilton_cycle.remove(self.hamilton_cycle[-1])

        # go back one node
        self.hamilton_cycle.remove(vertex)

    def find_eulerian_cycle(self):
        location = 0
        stack = [location]
        circuit = []
        while len(circuit) < self.num_edges + 1:
            for i, vertex in enumerate(self.adjacency_matrix_copy[location]):
                if vertex == 1:
                    self.adjacency_matrix_copy[location][i] = 0
                    self.adjacency_matrix_copy[i][location] = 0
                    stack.append(i)
                    location = i
                    break
            else:
                node = stack.pop()
                circuit.append(node)
                location = stack[-1] if stack else 0

    def print_adjacency_matrix(self):
        for row in self.adjacency_matrix:
            print(row)


# for i in range(10, 10000, 100):
#     graph = Graph(0.7, i)
#     # graph.print_adjacency_matrix()
#     start = time_ns()
#     graph.find_hamilton_cycle()
#     end = time_ns()
#     print(f"n: {i}, time: {(end - start) / 1000000000} s")
#
graph = Graph(0.7, 6)
graph.print_adjacency_matrix()
graph.find_hamilton_cycle()
adj_matrix = graph.adjacency_matrix
G = nx.Graph()
for i in range(len(adj_matrix)):
    for j in range(i + 1, len(adj_matrix[i])):
        if adj_matrix[i][j] == 1:
            G.add_edge(i, j)
# Draw the graph
nx.draw(G, with_labels=True, node_color='lightblue', node_size=500, font_weight='bold')
# Display the graph
plt.show()


# graph.find_eulerian_cycle()
# graph.find_hamilton_cycle()

# count = 0
# for i in range(1000):
#     i_count = 0
#     graph = Graph(0.7, 25)
#     print(graph.num_edges)
#     graph.find_eulerian_cycle()
#     # print(graph.find_eulerian_cycle_wrapper(deepcopy(graph.adjacency_matrix)))
#     # print(graph.find_eulerian_cycle())
#     for row in graph.adjacency_matrix:
#         if sum(row) % 2 == 1:
#             # print("nieeulerowski")
#             i_count += 1
#             count += 1
#
#         if i_count > 2:
#             print("totally nieeulerowski")
#     graph_to_print = deepcopy(graph.adjacency_matrix)
#
# print(count)