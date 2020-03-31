import sys
from room import Room
from player import Player
from world import World
# from projects import graph
# from graph import util
from util import Stack, Queue
# from graph import Graph

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


def opposite_direction_from(this_direction):
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
    for exit in exits:
        if exit is not last_direction and exit is not 'n' or 's' or 'e' or 'w':
            unexplored_exits[exit] = '?'
        else: # the exit is the door player used to enter room...
            unexplored_exits[exit] = previous_room
    graph[room.id] = unexplored_exits

# determines if the room is the final room with nowhere else to go
def the_last_room(room, last_direction=None):
    if last_direction is None: # you're in the starting room
        return False
    exits = room.get_exits()
    for exit in exits:
        # exclude the entry-door
        if exit is not opposite_direction_from(last_direction):
            # if any door = ? then you're NOT in the last room
            if exit is not '?':
                return False
    # if you avoid line 71, then you're in the last room
    return False

def depth_first_traverse_from(starting_room):
    # step 1: create a stack
        s = Stack()
        
        counter = 0

        # step 2: push the starting room
        s.push(starting_room)
        # step 3: create a path to track moves to send back via RETURN
        path = []
        room = starting_room
        # initialize the unexplored_exits of the starting room if first_time
        # graph_the_exits(starting_room)
        # Now go thru with graph
        direction = "dead end"
        doorway = None
        while s.size() > 0:
            # get the room the player was in previously so it's door can be properly attributed in the graph
             previous_room = room
             # pop the current room
             room = s.pop()
             print(f"room: {room}")

             # check if the current room is the end of the graph
             if not the_last_room(room, doorway):
                # Get the next direction to travel
                for key, value in graph[room.id].items():
                    if '?' == value:
                        direction = key
                if direction == "dead end":
                    return path
                print(f"A direction to move next is: {direction}")

                # Move the player to the next room, and record the path used, note the doorway just used
                player.travel(direction)
                path.append(direction)
                print(f"path: {path}")
                doorway = get_opposite_direction_from(direction) # tested, works

                # get newest room and graph the entryway door
                next_room = player.current_room
                graph[next_room.id][doorway] = room.id
                print(f"print your newly updated room graph: {graph} ")

                # push current room into the stack
                s.push(next_room)
             counter += 1
             if counter == 4:
                 sys.exit() 


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
# while len(graph) < len(room_graph):
    # travel til room has no unexplored exits
traversal_path = depth_first_traverse_from(start_room)
print(player.current_room)
print(traversal_path)
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
