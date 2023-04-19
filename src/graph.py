import json
import random
from pandas import read_csv

class Graph:
    def __init__(self) -> None:
        self.adjacency_list = {}


    def add_vertex(self, vertex: str) -> None:
        if vertex not in self.adjacency_list:
            self.adjacency_list[vertex] = []
    
    def add_edge(self, vertex1: str, vertex2: str) -> None:
        if vertex1 in self.adjacency_list and vertex2 in self.adjacency_list:
            self.adjacency_list[vertex1].append(vertex2)
            self.adjacency_list[vertex2].append(vertex1)

    def remove_edge(self, vertex1: str, vertex2: str) -> None:
        if vertex1 in self.adjacency_list and vertex2 in self.adjacency_list:
            self.adjacency_list[vertex1].remove(vertex2)
            self.adjacency_list[vertex2].remove(vertex1)

    def remove_vertex(self, vertex: str) -> None:
        if vertex in self.adjacency_list:
            for i in self.adjacency_list[vertex]:
                self.adjacency_list[i].remove(vertex)
            del self.adjacency_list[vertex]
    
    def obtain_adjacency_list(self, vertex: str) -> list:
        if vertex in self.adjacency_list:
            return self.adjacency_list[vertex]
        return []
    

    """  FALTA FAZER O LOAD GRAPH """
    def load_graph(self, file_path: str) -> None:
        df = read_csv(file_path).values.tolist()
        for i in df:
            self.add_vertex(i[0])
            self.add_vertex(i[1])
            self.add_edge(i[0], i[1])

            

    
    def bfs(self, start_vertex: str) -> list:
        visited = []
        queue = [start_vertex]
        while queue:
            current_vertex = queue.pop(0)
            if current_vertex not in visited:
                visited.append(current_vertex)
                queue.extend(self.adjacency_list[current_vertex])
        return visited

    def bfs_distance(self, start_vertex: str, end_vertex: str) -> int:
        visited = []
        queue = [start_vertex]
        distance = 0
        while queue:
            current_vertex = queue.pop(0)
            if current_vertex not in visited:
                visited.append(current_vertex)
                queue.extend(self.adjacency_list[current_vertex])
                distance += 1
                if current_vertex == end_vertex:
                    return distance
        return -1
    
    def random_vertex(self) -> str:
        return random.choice(list(self.adjacency_list.keys()))
    
    

if __name__ == "__main__":
    graph = Graph()
    graph.add_vertex("A")
    graph.add_vertex("B")
    graph.add_vertex("C")
    graph.add_vertex("D")
    graph.add_vertex("E")
    graph.add_vertex("F")
    graph.add_edge("A", "B")
    graph.add_edge("A", "C")
    graph.add_edge("B", "D")
    graph.add_edge("C", "E")
    graph.add_edge("D", "E")
    graph.add_edge("D", "F")
    graph.add_edge("E", "F")
    print(graph.bfs_distance("A", "F"))
