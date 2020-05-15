'''
GRAPHS:
vertices
edges
weight
directed graph, can only move in one direction along edges
undirected graph, allows movement in both directions along edges
cyclic graph, edges allows you to revisit at least one vert
acyclic graph, vertices can only be visited once
dense graphs
sparse graphs
completely connected graph
graph weights
    weighted vs unweighted
ways of representing graphs:
adjacency matrices/matrixes
adjacency lists

graph does not really have a head, so you can start traversing wherever
add starting node to a queue
while queueu is not empty:
    dequeue the first vert
    if the vert has not been visited
        mark as visited
        add all its neighbors to the queue
breadth first search
    layers
    elements in a layer are equal nodes away from 'head'

depth first traversal
find shortest path
add starting node to a stack
whil stack is not empty:
    pop the first vert
    if that vert is not visited:
        mark as visited
        push all its unvisited neighbors to the stack

anytime you use a stack, you can use recursion
'''
class Queue:
    def __init__(self):
        self.queue = []
    def enqueue(self, value):
        self.queue.append(value)
    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        else:
            return None
    def size(self):
        return len(self.queue)

class GraphNode:
    def __init__(self, value):
        self.value = value
        # adjacency lists
        self.edges = []

class Graph:
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        # set of edges
        self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        # add edge from v1 to v2
        # if undirected, need to add two edges, one from v1 to v2 and vice versa
        # if they are both in the graph
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            raise IndexError('Vertex does not exist in the graph')

    def get_neighbors(self, vertex_id):
        return self.vertices[vertex_id]

    def bft(self, starting_vertex_id):
        # breadth first traversal
        q = Queue()
        q.enqueue(starting_vertex_id)

        # keep track of visited nodes
        visited = set()

        # repeat until queue is empty, done when queue is empty
        while q.size() > 0:
            # dequeue first vert
            v = q.dequeue()

            # if it is not visited
            if v not in visited:
                # mark visited
                print(v)
                visited.add(v)

                for next_vert in self.get_neighbors(v):
                    q.enqueue(next_vert)

g = Graph()
g.add_vertex(99)
g.add_vertex(3)
g.add_vertex(3490)
g.add_edge(99, 3)
g.add_edge(99, 3490)
g.add_edge(3, 99)
# print(g.get_neighbors(99))
# print(g.get_neighbors(3))

g.bft(99)
g.bft(3490)