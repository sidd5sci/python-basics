import math
import time



class vertex:
    def __init__(self,_vertex):
        self.data = _vertex
        self.neighbour = list()
    def add_neighbour(self,_vertex):
        self.neighbour.append(_vertex)

    def remove_neighbour(self,_vertex):
        i = 0
        for v not in self.neighbour:
            i+=1
        self.neighbour[i].remove()
