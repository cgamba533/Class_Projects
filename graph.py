from dataclasses import dataclass
from typing import TypeAlias, Dict, Union, List
from stack_array import * # Needed for Depth First Search
from queue_array import * # Needed for Breadth First Search

MaybeVertex: TypeAlias = Union[None, 'Vertex']

@dataclass
class Vertex:
    id: Any

    def __post_init__(self) -> None:
        '''Add other attributes as necessary'''
        self.adjacent_to: List = []

class Graph:
    '''Add additional helper methods if necessary.'''
    def __init__(self, filename: str):
        '''reads in the specification of a graph and creates a graph using an adjacency list representation.  
           You may assume the graph is not empty and is a correct specification.  E.g. each edge is 
           represented by a pair of vertices.  Note that the graph is not directed so each edge specified 
           in the input file should appear on the adjacency list of each vertex of the two vertices associated 
           with the edge.'''
        self.vertices: Dict[Any, Vertex] = {}
        self.readFromFile(filename)

    def readFromFile(self, filename):
        with open(filename, 'r') as file:
            for line in file:
                v1, v2 = line.split()
                self.add_vertex(v1)
                self.add_vertex(v2)
                self.add_edge(v1, v2)

    def add_vertex(self, key: Any) -> None:
        '''Add vertex to graph, only if the vertex is not already in the graph.'''
        if key not in self.vertices:
            self.vertices[key] = Vertex(key)

    def get_vertex(self, key: Any):
        '''Return the Vertex object associated with the id. If id is not in the graph, return None'''
        return self.vertices.get(key)

    def add_edge(self, v1: Any, v2: Any) -> None:
        '''v1 and v2 are vertex id's. As this is an undirected graph, add an 
           edge from v1 to v2 and an edge from v2 to v1.  You can assume that
           v1 and v2 are already in the graph'''
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].adjacent_to.append(v2)
            self.vertices[v2].adjacent_to.append(v1)

    def get_vertices(self) -> List:
        '''Returns a list of id's representing the vertices in the graph, in ascending order'''
        return sorted(self.vertices.keys())

    def conn_components(self) -> List:
        '''Returns a list of lists.  For example, if there are three connected components 
           then you will return a list of three lists.  Each sub list should contain the
           vertices (in 'Python List Sort' order) in the connected component represented by that list.
           The overall list of lists should also be in order based on the first item of each sublist.
           This method MUST use Depth First Search logic!'''
        visited = set()
        components = []
        def depthFirstSearch(vertex, component):
            if vertex.id in visited:
                return
            visited.add(vertex.id)
            component.append(vertex.id)
            for i in vertex.adjacent_to:
                neighbor = self.get_vertex(i)
                depthFirstSearch(neighbor, component)

        for i in self.vertices.values():
            if i.id not in visited:
                component = []
                depthFirstSearch(i, component)
                components.append(sorted(component))
        return components

    def is_bipartite(self) -> bool:
        '''Returns True if the graph is bicolorable and False otherwise.
        This method MUST use Breadth First Search logic!'''
        color = {}
        queue = Queue(len(self.get_vertices()))
        start = self.get_vertex(self.get_vertices()[0])
        color[start.id] = 1
        queue.enqueue(start)
        while not queue.is_empty():
            current = queue.dequeue()
            for i in current.adjacent_to:
                neighbor = self.get_vertex(i)
                if neighbor.id not in color:
                    color[neighbor.id] = 3 - color[current.id]
                    queue.enqueue(neighbor)
                elif color[neighbor.id] == color[current.id]:
                    return False
        return True
