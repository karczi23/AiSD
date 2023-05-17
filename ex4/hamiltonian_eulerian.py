from random import shuffle, choice


# generate undirected graph
class Graph:
    def __init__(self, saturation, num_nodes):
        self.saturation = saturation
        self.num_nodes = num_nodes
        self.num_edges = int(self.num_nodes * (self.num_nodes - 1) / 2 * self.saturation)
        self.adjacency_matrix = [[0 for _ in range(self.num_nodes)] for _ in range(self.num_nodes)]
        self.odd_nodes = []
        self.num_edges_graph = self.num_edges
        self.generate_adjacency_matrix()

    # generate adjacency matrix for connected graph that is Eulerian and Hamiltonian
    def generate_adjacency_matrix(self):
        # generate ring graph with random node order
        nodes = [i for i in range(self.num_nodes)]
        shuffle(nodes)
        for i in range(self.num_nodes):
            self.adjacency_matrix[nodes[i]][nodes[(i + 1) % self.num_nodes]] = 1
            self.adjacency_matrix[nodes[(i + 1) % self.num_nodes]][nodes[i]] = 1

        # add random edges
        beg_node = nodes[0]
        for _ in range(self.num_edges - self.num_nodes):
            connections = [i for i, x in enumerate(self.adjacency_matrix[beg_node]) if x == 0]
            connections.remove(beg_node)
            end_node = choice(connections)
            if sum(self.adjacency_matrix[end_node]) % 2 == 1:
                self.adjacency_matrix[beg_node][end_node] = 1
                self.adjacency_matrix[end_node][beg_node] = 1
                beg_node = choice([i for i, node in enumerate(self.adjacency_matrix) if sum(node) < self.num_nodes - 1])
            else:
                self.adjacency_matrix[beg_node][end_node] = 1
                self.adjacency_matrix[end_node][beg_node] = 1
                beg_node = end_node

    def print_adjacency_matrix(self):
        for row in self.adjacency_matrix:
            print(row)


graph = Graph(0.6, 7)
graph.print_adjacency_matrix()
