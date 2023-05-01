from random import randint, choices
from time import time_ns
from copy import deepcopy

class DAG:

    def __init__(self, vertices: int = 100, saturation: float = 1) -> None:
        if vertices < 1:
            vertices = 1
        if saturation <= 0 or saturation > 1:
            saturation = 1
        self.vertices = int(vertices)
        self.saturation = saturation
        self.matrix = []
        self.splist = []
        for i in range(self.vertices):
            self.splist.append([])
        # matrix used for top sort testing (correct top sort is 1, 10, 5, 2, 3, 7, 8, 4, 6, 9)
        # self.matrix = [
        #     [0,1,0,0,0,0,0,0,0,1],
        #     [-1,0,1,0,-1,0,1,0,0,0],
        #     [0,-1,0,1,0,0,0,0,0,0],
        #     [0,0,-1,0,0,1,0,-1,0,0],
        #     [0,1,0,0,0,0,1,0,0,-1],
        #     [0,0,0,-1,0,0,-1,-1,1,-1],
        #     [0,-1,0,0,-1,1,0,1,1,0],
        #     [0,0,0,1,0,1,-1,0,1,0],
        #     [0,0,0,0,0,-1,-1,-1,0,0],
        #     [-1,0,0,0,1,1,0,0,0,0]
        # ]
        self.possible_edges = []
        self.create_neighbourhood_matrix()
        self.convert_neighbourhood_matrix_into_predecessors_list()

    
    def create_neighbourhood_matrix(self) -> list:
        edges = int(self.__get_full_saturation_size() * self.saturation)

        self.possible_edges = [(i, j) for i in range(0, self.vertices - 1) for j in range(i + 1, self.vertices)]

        self.matrix = [[0 for _ in range(self.vertices)] for _ in range(self.vertices)]

        ch = choices(population = self.possible_edges, k = edges)

        for item in ch:
            self.matrix[item[0]][item[1]] = 1
            self.matrix[item[1]][item[0]] = -1

        # print(*[f"{i + 1}," for i in range(self.vertices)])
        # for i in range(self.vertices):
        #     print(self.matrix[i]) 
        while (len(self.top_sort_neighbourhood_matrix()[0]) != self.vertices):
            return self.create_neighbourhood_matrix()
        return self.matrix
    
    #Kahn algorithm
    def top_sort_neighbourhood_matrix(self) -> list:
        # first element will always be "1" vertex
        top_sort_list = []
        lookup_matrix = deepcopy(self.matrix)
        # independent_vertex = lookup_matrix[0]
        # index = self.matrix.index(independent_vertex)
        # top_sort_list.append(index + 1) # we count from 1, not 0
        #     # for elem in vertex:
        start = time_ns()
        while len(top_sort_list) != self.vertices:
        # for _ in lookup_matrix:
            for index, vertex in enumerate(lookup_matrix):
                if (index + 1) in top_sort_list:
                    continue
                candidate = True
                for elem in vertex:
                    if elem == -1:
                        candidate = False
                        break
                if candidate:
                    top_sort_list.append(index + 1)
                    for vertex in lookup_matrix:
                        vertex[index] = 0
                    break
        return top_sort_list, time_ns() - start
    
    def top_sort_predecessors_list(self):
        top_sort_list = []
        lookup_list = deepcopy(self.splist)
        start = time_ns()
        # for _ in lookup_list:
        while len(top_sort_list) != self.vertices:
            for index, vertex in enumerate(lookup_list):
                if len(vertex) == 0 and (index + 1) not in top_sort_list:
                    top_sort_list.append(index + 1)
                    for vertex in lookup_list:
                        try:
                            vertex.remove(index)
                        except ValueError:
                            pass
        return top_sort_list, time_ns() - start
            
    def convert_neighbourhood_matrix_into_predecessors_list(self):
        for i, vertex in enumerate(self.matrix):
            for j, elem in enumerate(vertex):
                if elem == -1:
                    self.splist[i].append(j)

    def get_vertices(self):
        return self.vertices

    def get_saturation(self):
        return self.saturation
    
    def __get_full_saturation_size(self):
        return self.vertices * (self.vertices - 1) / 2
    
# dag = DAG(vertices=10, saturation=0.4)
# for vertex in dag.matrix:
#     print(vertex)
# print(dag.top_sort_predecessors_list())
# dag.top_sort_neighbourhood_matrix()

# from matplotlib import pyplot as plt
# import networkx as nx

# graph = nx.DiGraph()
# for index,vertex in enumerate(dag.splist):
#     for edge in vertex:
#         graph.add_edge(edge + 1, index + 1)

# plt.tight_layout()
# nx.draw_networkx(graph, arrows=True)
# plt.savefig("g1.png", format="PNG")
# plt.clf()

# print(list(nx.topological_sort(graph)))
outcome = []
for i in range(200, 1001, 200):
    print(i)

    dag = DAG(i, 0.6)
    
    _, time_pl = dag.top_sort_predecessors_list()
    print(time_pl)

    _, time_nm = dag.top_sort_neighbourhood_matrix()
    print(time_nm)

    outcome.append((i, time_nm, time_pl))

with open("wyniki3.txt", "w") as f:
    f.write("count | neighbourhood matrix | predecessors list\n")
    for record in outcome:
        f.write(str(record) + "\n")