# generate digraph with random weights from 1 to 1000
from random import randint, sample
from copy import deepcopy
from time import time_ns

class Graph:
    # constructor
    def __init__(self, vertices: int = 100, saturation: float = 1) -> None:
        if vertices < 1:
            raise Exception("The number of vertices must be greater than 0")
        if saturation <= 0 or saturation > 1:
            raise Exception("Saturation must be greater than 0 and less than or equal to 1")
        self.vertices = int(vertices)
        self.saturation = saturation
        self.matrix = []
        self.adjacency_list = [[] for _ in range(self.vertices)]

    def create_neighbourhood_matrix_with_weights(self) -> list:
        edges = int(self.__get_full_saturation_size() * self.saturation)
        # generate all possible edges
        self.possible_edges = [(i, j) for i in range(0, self.vertices - 1) for j in range(i + 1, self.vertices)]

        # generate empty matrix
        self.matrix = [[0 for _ in range(self.vertices)] for _ in range(self.vertices)]

        # get random edges in number of edges
        ch = sample(self.possible_edges, edges)

        # check if all vertices are connected,
        # by checking if the number of unique vertices is equal to the number of vertices
        while len(set([item[0] for item in ch] + [item[1] for item in ch])) != self.vertices:
            ch = sample(self.possible_edges, edges)

        # generate random weights for edges
        for item in ch:
            weight = randint(1, 1000)
            self.matrix[item[0]][item[1]] = weight
            self.matrix[item[1]][item[0]] = weight

        #
        # print(*[f"{i + 1}," for i in range(self.vertices)])
        # for i in range(self.vertices):
        #     print(self.matrix[i])
        return self.matrix

    def convert_neighbourhood_matrix_to_adjacency_list(self) -> list:
        # convert matrix to list
        for i in range(self.vertices):
            for j in range(self.vertices):
                if self.matrix[i][j] != 0:
                    self.adjacency_list[i].append((j, self.matrix[i][j]))

        # print(*[f"{i + 1}," for i in range(self.vertices)])
        # for i in range(self.vertices):
        #     print(self.adjacency_list[i])
        return self.adjacency_list

    # Bourvka's algorithm
    def minimum_spanning_tree_neighbourhood_matrix(self):
        # generate empty matrix
        spanning_tree = [[0 for _ in range(self.vertices)] for _ in range(self.vertices)]
        # copy matrix
        temp_matrix = deepcopy(self.matrix)
        # list of subgraphs in spanning tree
        sub_graphs = []
        start = time_ns()
        # find lowest weight for each vertex
        for index, vertex in enumerate(temp_matrix):
            vertex_connections = [i for i in vertex if i != 0]
            if len(vertex_connections) == 0:
                continue
            lowest_weight = min([weight for weight in vertex if weight != 0])
            # print([weight for weight in vertex if weight != 0])
            lowest_weight_index = vertex.index(lowest_weight)
            # print(f"{index + 1} -> {lowest_weight_index + 1} ({lowest_weight})")
            spanning_tree[index][lowest_weight_index] = lowest_weight
            spanning_tree[lowest_weight_index][index] = lowest_weight
            # generate subgraphs list
            for graph in sub_graphs:
                if index in graph and lowest_weight_index in graph:
                    break
                elif index in graph:
                    graph.append(lowest_weight_index)
                    break
                elif lowest_weight_index in graph:
                    graph.append(index)
                    break
            else:
                sub_graphs.append([index, lowest_weight_index])

            # temp_matrix[index][lowest_weight_index] = 0
            # temp_matrix[lowest_weight_index][index] = 0

        # print(sub_graphs)
        # join all intersecting graphs in sub_graphs
        i = 0
        while i < len(sub_graphs):
            for j in range(i + 1, len(sub_graphs)):
                if len(set(sub_graphs[i]) & set(sub_graphs[j])) > 0:
                    sub_graphs[i] = list(set(sub_graphs[i] + sub_graphs[j]))
                    sub_graphs.pop(j)
                    break
            else:
                i += 1

        # print(sub_graphs)
        # for i in range(self.vertices):
        #     print(temp_matrix[i])
        # print()
        # for i in range(self.vertices):
        #     print(spanning_tree[i])
        # check if there is only one subgraph containing all vertices
        while len(sub_graphs[0]) < self.vertices:
            # delete edges from temp_matrix that are in the same subgraph
            for graph in sub_graphs:
                for i in range(len(graph)-1):
                    for j in range(i+1, len(graph)):
                        temp_matrix[graph[i]][graph[j]] = 0
                        temp_matrix[graph[j]][graph[i]] = 0

                # for i in range(self.vertices):
                #     print(temp_matrix[i])
            # get all connections between subgraphs
            for graph in sub_graphs:
                graph_connections = []
                for i in graph:
                    for j in range(self.vertices):
                        if temp_matrix[i][j] != 0:
                            graph_connections.append((i, j, temp_matrix[i][j]))
                # sort connections by weight
                graph_connections.sort(key=lambda x: x[2])
                # print(graph_connections)
                from_graph = graph_connections[0][0]
                to_graph = graph_connections[0][1]
                weight = graph_connections[0][2]
                # add new edge to subgraph
                graph.append(to_graph)
                spanning_tree[from_graph][to_graph] = weight
                spanning_tree[to_graph][from_graph] = weight

                # join all intersecting graphs in sub_graphs
                i = 0
                while i < len(sub_graphs):
                    for j in range(i + 1, len(sub_graphs)):
                        if len(set(sub_graphs[i]) & set(sub_graphs[j])) > 0:
                            sub_graphs[i] = list(set(sub_graphs[i] + sub_graphs[j]))
                            sub_graphs.pop(j)
                            break
                    else:
                        i += 1

        # print()
        # print(*spanning_tree, sep="\n")
        end = time_ns()
        return spanning_tree, end - start

    def minimum_spanning_tree_adjacency_list(self):
        # generate empty matrix
        spanning_tree = [[] for _ in range(self.vertices)]
        # copy matrix
        temp_matrix = deepcopy(self.adjacency_list)
        # list of subgraphs in spanning tree
        sub_graphs = []

        start = time_ns()
        for index, vertex in enumerate(temp_matrix):
            vertex.sort(key=lambda x: x[1])
            if vertex[0][0] in [i[0] for i in spanning_tree[index]]:
                continue
            spanning_tree[index].append(vertex[0])
            spanning_tree[vertex[0][0]].append((index, vertex[0][1]))
            # print(f"{index + 1} -> {vertex[0][0] + 1} ({vertex[0][1]})")
            # generate subgraphs list
            for graph in sub_graphs:
                if vertex[0][0] in graph and index in graph:
                    break
                elif vertex[0][0] in graph:
                    graph.append(index)
                    break
                elif index in graph:
                    graph.append(vertex[0][0])
                    break
            else:
                sub_graphs.append([index, vertex[0][0]])

        # print()
        # print(sub_graphs)
        # print(*spanning_tree, sep="\n")
        # print()

        # join all intersecting graphs in sub_graphs
        i = 0
        while i < len(sub_graphs):
            for j in range(i + 1, len(sub_graphs)):
                if len(set(sub_graphs[i]) & set(sub_graphs[j])) > 0:
                    sub_graphs[i] = list(set(sub_graphs[i] + sub_graphs[j]))
                    sub_graphs.pop(j)
                    break
            else:
                i += 1

        # print(sub_graphs)

        while len(sub_graphs[0]) < self.vertices:
            for graph in sub_graphs:
                for vertex in graph:
                    for connection in temp_matrix[vertex].copy():
                        if connection[0] in graph:
                            temp_matrix[vertex].remove(connection)

            # print(*temp_matrix, sep="\n", end="\n\n")
            for graph in sub_graphs:
                graph_connections = []
                for vertex in graph:
                    for connection in temp_matrix[vertex]:
                        graph_connections.append((vertex, connection[0], connection[1]))

                graph_connections.sort(key=lambda x: x[2])
                # print(graph_connections)
                from_graph = graph_connections[0][0]
                to_graph = graph_connections[0][1]
                weight = graph_connections[0][2]
                if to_graph not in [x[0] for x in spanning_tree[from_graph]]:
                    spanning_tree[from_graph].append((to_graph, weight))
                    spanning_tree[to_graph].append((from_graph, weight))

                graph.append(to_graph)

            i = 0
            while i < len(sub_graphs):
                for j in range(i + 1, len(sub_graphs)):
                    if len(set(sub_graphs[i]) & set(sub_graphs[j])) > 0:
                        sub_graphs[i] = list(set(sub_graphs[i] + sub_graphs[j]))
                        sub_graphs.pop(j)
                        break
                else:
                    i += 1

        end = time_ns()
        return spanning_tree, end - start



    def get_vertices(self):
        return self.vertices

    def get_saturation(self):
        return self.saturation

    def __get_full_saturation_size(self):
        return self.vertices * (self.vertices - 1) / 2

# dag = Graph(vertices=5, saturation=0.5)
# print(*dag.create_neighbourhood_matrix_with_weights(), sep="\n", end="\n\n")
# print(*dag.minimum_spanning_tree_neighbourhood_matrix(), sep="\n", end="\n\n")
# print(*dag.convert_neighbourhood_matrix_to_adjacency_list(), sep="\n", end="\n\n")
# print(*dag.minimum_spanning_tree_adjacency_list(), sep="\n")

sat = [0.3, 0.7]
for s in sat:
    outcome = []
    for i in range(200, 1001, 200):
        print(i)

        graph = Graph(i, s)
        graph.create_neighbourhood_matrix_with_weights()

        _, time_nm = graph.minimum_spanning_tree_neighbourhood_matrix()
        print(time_nm)

        graph.convert_neighbourhood_matrix_to_adjacency_list()
        _, time_al = graph.minimum_spanning_tree_adjacency_list()
        print(time_al)

        outcome.append(f"{i} {time_nm} {time_al}")

    with open(f"wyniki3_2_{s}.txt", "w") as f:
        f.write("count neighbourhood matrix adjacency\n")
        for record in outcome:
            f.write(str(record) + "\n")

