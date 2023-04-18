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
    print(graph.adjacency_list)
    graph.remove_edge("A", "B")
    print(graph.adjacency_list)
    graph.remove_vertex("A")
    print(graph.adjacency_list)
    print(graph.obtain_adjacency_list("B"))
    print(graph.obtain_adjacency_list("A"))
