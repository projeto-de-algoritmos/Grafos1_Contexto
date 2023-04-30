#codign= utf-8

import json
import random



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
    

    def load_graph(self, file_path: str) -> None:
        with open(file_path, "r") as file:
            data = json.load(file)
            for i in data:
                self.add_vertex(i)
                for j in data[i]:
                    self.add_vertex(j)
                    self.add_edge(i, j)           

    
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
    graph.load_graph("./src/data.json")

    print(graph.obtain_adjacency_list("sobremesa"))

    print(graph.bfs_distance("uva","banana"))
    
