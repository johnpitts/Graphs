from util import Stack, Queue
from room import Room
from player import Player

class Graph:

    """Represent a graph as a dictionary of room numbers
    mapping nieghboring rooms to the 4 cardinal directions."""
    def __init__(self):
        self.rooms = {}

    def add_room(self, room):
        exits = self.room.get_exits()
        id = room.id
        self.rooms[id] = {}

        if room not in self.rooms:
            id = room.id

        for each_exit in exits:
            # eliminates adding '?' to the direction from which player just left!

            if each_exit is not oppo:
                self.rooms[room_id][each_exit] = '?'
            else:
                self.rooms[room_id][oppo] = previous_room_id

            # 0: {'n' }
                

        # else:
        #     print("Either you just started or Error: direction entered is not a valid direction"
        #     return None

    def get_neighboring_rooms_dict(self, room_id):
        """
        Get all neighboring rooms
        """
        if room_id in self.rooms:
            return self.rooms[room_id]
        else:
            print("ERROR: you're code didn't work bc there's no nieghoring rooms dict for this room_id")


        def dft(self, starting_room):
        # step 1: create a stack
        s = Stack()
        # step 2: push the starting vertex
        s.push(starting_room)
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
                 # push all of it's nieghbors
                 neighbors = self.get_neighbors(v)
                 print(neighbors)
                 for neighbor in neighbors:
                     s.push(neighbor)



    def depth_first_traverse_from(self, starting_room_id, graph):
        """
        move to a graph exit in depth-first order
        beginning from starting_room.
        """
        # step 1: create a stack
        s = Stack()
        # step 2: push the starting room
        s.push(starting_room_id)
        # our graph (player map) will store visited rooms and all info associated
        # while stack is not empty...
        while s.size() > 0:
             # 

             # pop the 1st vertex
             room = s.pop()
             #  check if it''s been visited
             if room not in self.rooms:
             #  if it hasn't been visitied...
                 # mark it as visited
                 print(room)
                 self.add_room(room)



                 # get the new exits
                 exits = self.room.get_exits()
                 print(exits)
                 # randomly pick a door
                 picked_door = random(exits)
                 s.push(picked_door)


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
             v = path[-1]

             #  check if it''s been visited
             if v not in visited:
             #  if it hasn't been visitied...
                 # mark it as visited
                 visited.add(v)
                 # check if it's the target
                 if v is destination_vertex:
                     # if so return the PATH
                     return path
                 #  enqueue a PATH to all of it's nieghbors
                 for neighbor in get_neighbors(v):
                     # make a copy of the path
                     new_path = path.append(neighbor)
                     # enque the copy
                     q.enqueue(new_path)


    # not sure will need this yet, so not messing with it until i do need it
    def breadth_traverse_to_untried_door_room(self, starting_room, path):
        """
        traverse to the room with a ? for a door which you found using breadth
        first traversal method, using the given path
        """

        # step 1: create a queue
        q = Queue()
        # step 2: enqueue the starting vertex
        q.enqueue(starting_room)
        # while queue is not empty...
        while q.size() > 0:
             # dequeue the 1st vertex
             v = q.dequeue()
             #  check if it''s been visited
             if v not in visited:
             #  if it hasn't been visitied...
                 # mark it as visited
                 print(v)
                 self.add_room(v)
                 #  enqueue all of it's nieghbors
                 for neighbor in self.add_doors(v):
                     q.enqueue(neighbor)


         