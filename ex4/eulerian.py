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
        self.reps = 0
        self.generate_adjacency_matrix()
        self.adjacency_matrix_copy = deepcopy(self.adjacency_matrix)
        self.not_found = True
        self.sum_edges = 0

    # generate adjacency matrix for connected graph that is Eulerian and Hamiltonian
    def generate_adjacency_matrix(self):
        # generate ring graph with random node order
        nodes = [i for i in range(self.num_nodes)]
        shuffle(nodes)
        for i in range(self.num_nodes):
            self.adjacency_matrix[nodes[i]][nodes[(i + 1) % self.num_nodes]] = 1
            self.adjacency_matrix[nodes[(i + 1) % self.num_nodes]][nodes[i]] = 1

        self.sum_edges = self.num_nodes
        # add random triangles
        while self.sum_edges < self.num_edges:
            # choose three random nodes
            three_nodes = random.sample(range(self.num_nodes), 3)
            # if generator is stuck, break
            if self.reps > 1000000:
                break
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
                self.sum_edges += 3

            self.reps += 1

        # if generator was stuck, reset and try again
        if self.reps > 1000000:
            self.reps = 0
            self.adjacency_matrix = [[0 for _ in range(self.num_nodes)] for _ in range(self.num_nodes)]
            self.generate_adjacency_matrix()
            return
        self.num_edges = self.sum_edges

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

    def isSafe(self, v, graph, path, pos):

        # If the vertex is adjacent to
        # the vertex of the previously
        # added vertex
        if graph[path[pos - 1]][v] == 0:
            return False

        # If the vertex has already
        # been included in the path
        for i in range(pos):
            if path[i] == v:
                return False

        # Both the above conditions are
        # not true, return true
        return True

    # To check if there exists
    # at least 1 hamiltonian cycle
    hasCycle = False

    # Function to find all possible
    # hamiltonian cycles
    def hamCycle(self, graph):
        global hasCycle

        # Initially value of boolean
        # flag is false
        hasCycle = False

        # Store the resultant path
        path = []
        path.append(0)

        # Keeps the track of the
        # visited vertices
        visited = [False] * (len(graph))

        for i in range(len(visited)):
            visited[i] = False

        visited[0] = True

        # Function call to find all
        # hamiltonian cycles
        self.FindHamCycle(graph, 1, path, visited)

        if hasCycle:
            # If no Hamiltonian Cycle
            # is possible for the
            # given graph
            print("No Hamiltonian Cycle" + "possible ")
            return

    # Recursive function to find all
    # hamiltonian cycles
    def FindHamCycle(self, graph, pos, path, visited):

        # If all vertices are included
        # in Hamiltonian Cycle
        if pos == len(graph):

            # If there is an edge
            # from the last vertex to
            # the source vertex
            if graph[path[-1]][path[0]] != 0:

                # Include source vertex
                # into the path and
                # print the path
                path.append(0)
                # for i in range(len(path)):
                #     print(path[i], end=" ")
                # print()

                # Remove the source
                # vertex added
                path.pop()

                # Update the hasCycle
                # as true
                hasCycle = True
            return

        # Try different vertices
        # as the next vertex
        for v in range(len(graph)):

            # Check if this vertex can
            # be added to Cycle
            if self.isSafe(v, graph, path, pos) and not visited[v]:
                path.append(v)
                visited[v] = True

                # Recur to construct
                # rest of the path
                self.FindHamCycle(graph, pos + 1, path, visited)

                # Remove current vertex
                # from path and process
                # other vertices
                visited[v] = False
                path.pop()
    def print_adjacency_matrix(self):
        for row in self.adjacency_matrix:
            print(row)


step = 1
saturations = [0.5]
repeats = 10

for j in saturations:
    average_hamilton_times = []
    for rep in range(repeats):
        hamilton_times = []
        for i in range(5, 15):
            hamilton_graph = Graph(j, (i + 1) * step)

            start = time_ns()
            hamilton_graph.hamCycle(hamilton_graph.adjacency_matrix)
            end = time_ns()
            print(f"n: {i}, time: {(end - start) / 1000000000} s")
            hamilton_times.append([(i + 1) * step, end - start])

        average_hamilton_times.append(hamilton_times)

    for test in range(len(average_hamilton_times[0])):
        sum = 0
        for rep in range(repeats):
            sum += average_hamilton_times[rep][test][1]
        average_hamilton_times[0][test][1] = sum / repeats

    with open(f"euler-hamilton_{j}.txt", "w") as file:
        for line in average_hamilton_times[0]:
            file.write(f"{line[0]} {line[1]}\n")
#
# graph = Graph(0.5, 10)
# # graph.print_adjacency_matrix()
# # graph.find_hamilton_cycle()
# graph.hamCycle(graph.adjacency_matrix)
# adj_matrix = graph.adjacency_matrix
# G = nx.Graph()
# for i in range(len(adj_matrix)):
#     for j in range(i + 1, len(adj_matrix[i])):
#         if adj_matrix[i][j] == 1:
#             G.add_edge(i, j)
# # Draw the graph
# nx.draw(G, with_labels=True, node_color='lightblue', node_size=500, font_weight='bold')
# # Display the graph
# plt.show()


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