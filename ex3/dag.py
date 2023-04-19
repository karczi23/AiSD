from random import randint
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
    
    def create_neighbourhood_matrix(self) -> list:
        edges = int(self.__get_full_saturation_size() * self.saturation)
 
        self.matrix = [[0 for _ in range(self.vertices)] for _ in range(self.vertices)]

        i = 0
        while i < edges:
            lower = randint(0, self.vertices - 2) # vertices - 1 (because of list indexes being "-1" ) 
                                                  # - 1 (because the "lower index vertex" can't be the last one)
            higher = randint(lower + 1, self.vertices - 1)
            if self.matrix[lower][higher] == 0:
                self.matrix[lower][higher] = 1
                self.matrix[higher][lower] = -1
                i += 1

        print(*[f"{i + 1}," for i in range(self.vertices)])
        for i in range(self.vertices):
            print(self.matrix[i]) 

        return self.matrix


    def get_vertices(self):
        return self.vertices

    def get_saturation(self):
        return self.saturation
    
    def __get_full_saturation_size(self):
        return self.vertices * (self.vertices - 1) / 2
    
dag = DAG(vertices=10, saturation=0.35)
dag.create_neighbourhood_matrix()
