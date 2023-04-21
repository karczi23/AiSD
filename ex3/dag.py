from random import randint, choices
from time import sleep

class DAG:

    def __init__(self, vertices: int = 100, saturation: float = 1) -> None:
        if vertices < 1:
            vertices = 1
        if saturation <= 0 or saturation > 1:
            saturation = 1
        self.vertices = int(vertices)
        self.saturation = saturation
        self.matrix = []
        self.possible_edges = []
    
    def create_neighbourhood_matrix(self) -> list:
        edges = int(self.__get_full_saturation_size() * self.saturation)

        self.possible_edges = [(i, j) for i in range(0, self.vertices - 1) for j in range(i + 1, self.vertices)]

        self.matrix = [[0 for _ in range(self.vertices)] for _ in range(self.vertices)]

        ch = choices(population = self.possible_edges, k = edges)

        for item in ch:
            self.matrix[item[0]][item[1]] = 1
            self.matrix[item[1]][item[0]] = -1

        print(*[f"{i + 1}," for i in range(self.vertices)])
        for i in range(self.vertices):
            print(self.matrix[i]) 

        return self.matrix
    
    def top_sort(self, elem: tuple):
        
        pass


    def get_vertices(self):
        return self.vertices

    def get_saturation(self):
        return self.saturation
    
    def __get_full_saturation_size(self):
        return self.vertices * (self.vertices - 1) / 2
    
dag = DAG(vertices=10, saturation=0.35)
dag.create_neighbourhood_matrix()
