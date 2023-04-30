from random import randint, choices
from time import sleep
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

        return self.matrix
    
    #Kahn algorithm
    def top_sort_neighbourhood_matrix(self):
        # first element will always be "1" vertex
        top_sort_list = []
        lookup_matrix = deepcopy(self.matrix)
        # independent_vertex = lookup_matrix[0]
        # index = self.matrix.index(independent_vertex)
        # top_sort_list.append(index + 1) # we count from 1, not 0
        #     # for elem in vertex:
        for _ in lookup_matrix:
            for index, vertex in enumerate(lookup_matrix):
                candidate = True
                for elem in vertex:
                    if elem == -1:
                        candidate = False
                        break
                if candidate and (index + 1) not in top_sort_list:
                    top_sort_list.append(index + 1)
                    for vertex in lookup_matrix:
                        vertex[index] = 0
                    break
        print(top_sort_list)
            



    def get_vertices(self):
        return self.vertices

    def get_saturation(self):
        return self.saturation
    
    def __get_full_saturation_size(self):
        return self.vertices * (self.vertices - 1) / 2
    
dag = DAG(vertices=10, saturation=0.35)
dag.create_neighbourhood_matrix()
dag.top_sort_neighbourhood_matrix()
