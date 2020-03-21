from room import Room
from player import Player
from world import World
# from projects import graph
# from graph import util
from util import Stack, Queue
from graph import Graph

import random
from ast import literal_eval

# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
map_file = "maps/test_line.txt"
# map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
# map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph=literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)

# graph = Graph()
graph = {}
traversal_path = []
unexplored_exits = {}

start_room = player.current_room
# initialize the starting room's exit dictionary with ?s


def get_opposite_direction_from(this_direction):
    if this_direction == 'n':
        return 's'
    if this_direction == 's':
        return 'n'
    if this_direction == 'w':
        return 'e'
    if this_direction == 'e':
        return 'w'


def graph_the_exits(room, previous_room=None, last_direction=None):
    exits = room.get_exits()
    if previous_room == None:
        for exit in exits:
            unexplored_exits[exit] = '?'
        graph[room.id] = unexplored_exits
    else:
        for exit in exits:
            if exit is not last_direction:
                unexplored_exits[exit] = '?'
            # else:
            #     unexplored_exits[exit] = previous_room.id
        graph[room.id] = unexplored_exits



def depth_first_traverse_from(starting_room):
    # step 1: create a stack
        s = Stack()
        # step 2: push the starting room
        s.push(starting_room)
        # step 3: create a path to track moves to send back via RETURN
        path = []
        room = starting_room
        # initialize the unexplored_exits of the starting room if first_time
        graph_the_exits(starting_room)
        # Now go thru with graph
        oppo = None
        while s.size() > 0:
             # enter all the exits into the graph with a '?'
             previous_room = room
             # pop the 1st room
             room = s.pop()
             graph_the_exits(room, previous_room.id, oppo)

             # find a door with a '?' if one exists, else return the path
             exits = room.get_exits()
             print(exits)
             if len(exits) > 1:
                 print("THREE")
                 for key, value in graph[room.id].items():
                     if '?' == value:
                         direction = key
             else:
                return path
             player.travel(direction)
             path.append(direction)
             print(path)
             oppo = get_opposite_direction_from(direction)
             # get newest room
             next_room = player.current_room()
             # set the newly-entered room as destination for door entered in the graph
             graph[next_room.id][oppo] = room.id
             # push it into the stack
             s.push(next_room)


def bfs(self, starting_room):
        # step 1: create a queue
        q = Queue()
        # step 2: enqueue a PATH TO the starting vertex
        q.enqueue( [starting_room] )
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



# Loop until the map we build is as long as the given groom graph
while len(graph) < len(room_graph):
    # travel til room has no unexplored exits
    traversal_path = depth_first_traverse_from(start_room)
    # do breadth-fs for nearest unexplored exit with graph already filled out only

    # Travel to unexplored exit room



    

# TRAVERSAL TEST
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)

for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room)

if len(visited_rooms) == len(room_graph):
    print("test")
    print(f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")



#######
# UNCOMMENT TO WALK AROUND
#######
# player.current_room.print_room_description(player)
# while True:
#     cmds = input("-> ").lower().split(" ")
#     if cmds[0] in ["n", "s", "e", "w"]:
#         player.travel(cmds[0], True)
#     elif cmds[0] == "q":
#         break
#     else:
#         print("I did not understand that command.")
