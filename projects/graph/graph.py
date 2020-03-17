"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy

class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        pass  # TODO

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        pass  # TODO

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        pass  # TODO

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """

        # step 1: create a queue
        q = Queue()
        # step 2: enqueue the starting vertex
        q.enqueue(starting_vertex)


        # step 3: create a set to store visited vertices
        visited = set()

        # while queue is not empty...
        while q.size() > 0:
             # dequeue the 1st vertex
             v = q.dequeue()

             #  check if it''s been visited
             if v not in visited:
             #  if it hasn't been visitied...
                 # mark it as visited
                 visited.add(v)

                 #  enqueue all of it's nieghbords
                 



        pass

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        # step 1: create a stack
        s = Stack()
        # step 2: push the starting vertex
        s.push(starting_vertex)
        # step 3: create a set to store visited vertices
        visited = set()
        # while stack is not empty...
        while s.size() > 0:
             # pop the 1st vertex
             v = s.pop()
             #  check if it''s been visited
             if v not in visited:
             #  if it hasn't been visitied...
                 # mark it as visited
                 print(v)
                 visited.add(v)
                 # push all of it's nieghbords
                 for neighbor in self.get_neighbors(v):
                     s.push(neighbor)

    def dft_recursive(self, starting_vertex, visited=None): # "default arg = None"
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """
        if visited is None:
            visited() = set()
        # check if the node has been visited
        # if not...
        if starting_vertex not in visited:
            # Mark it as visited
            visited.add(starting_vertex)
        print(starting_vertex)
        # call dft_recursive on each nieghbor
        for neighbor in self.get_neighbors(starting_vertex):
            self.dft_recursive(neighbor, visited)

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        # step 1: create a queue
        q = Queue()
        # step 2: enqueue a PATH TO the starting vertex
       
        q.enqueue( [starting_vertex] )
        # step 3: create a set to store visited vertices
        visited = set()
        # while queue is not empty...
        while q.size() > 0:
             # dequeue the first PATH
             path = q.dequeue()
             # grab the vertex from the end of the path
             v - path[-1]

             #  check if it''s been visited
             if v not in visited:
             #  if it hasn't been visitied...
                 # mark it as visited
                 visited.add(v)
                 # check if it's the target
                 if v == destination_vertex
                     # if so return the PATH
                     return path
                 #  enqueue a PATH to all of it's nieghbors
                 v.append( neighbors(v[-1]) )
                     # make a copy of the path
                     # enque the copy
target = 6
q = [ [1,2,4,7], [another path]]


    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        pass  # TODO

    def dfs_recursive(self, starting_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        print(path)
        if visited is None:
            visited = None:
        if path is None:
            path = []
        if starting_vertex not in visited:
            visited.add(starting_vertex)
            path_copy = path.copy()
            path_copy.append(starting_vertex)
            

if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    print(graph.vertices)

    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    graph.bft(1)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    graph.dft(1)
    graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print(graph.dfs(1, 6))
    print(graph.dfs_recursive(1, 6))
