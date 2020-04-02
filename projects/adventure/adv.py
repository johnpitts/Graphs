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
# map_file = "maps/test_line.txt"
map_file = "maps/test_cross.txt"
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

# FUNCTIONS (go to line...  ... for continuation of main code)


def opposite_direction_from(this_direction):
    if this_direction == 'n':
        return 's'
    if this_direction == 's':
        return 'n'
    if this_direction == 'w':
        return 'e'
    if this_direction == 'e':
        return 'w'


def graph_the_exits(room, previous_room=None, entryway=None):
    # graph the entryway into the previous room
    if previous_room is not None:
        last_door = opposite_direction_from(entryway)
        graph[previous_room.id][last_door] = room.id
    exits = room.get_exits()
    unexplored_exits = {}
    for exit in exits:
        # the only time the graph is updated is when player has walked thru a door and can connect a past room to current room
        if exit is entryway:
            unexplored_exits[exit] = previous_room.id
        else:
            unexplored_exits[exit] = '?'

    graph[room.id] = unexplored_exits

# determines if the room is the final room with nowhere else to go
def the_last_room(room, entryway=None):
    if entryway is None: # you're in the starting room
        return False
    exits = room.get_exits()
    for exit in exits:
        # exclude the entry-door
        print(f"exit to review is: {exit}")
        if exit is not entryway:
            # if any door = ? then you're NOT in the last room
            print("exit is not entryway")
            if graph[room.id][exit] is '?':
                print("returned false")
                return False
    # if you avoid line 71, then you're in the last room
    print("last room")
    return True

def depth_first_traverse_from(starting_room):

    print(starting_room)

    # step 1: create a stack
    s = Stack()
    # you must graph the starting room, or else graph won't have anything in it when you look for '?' in for key, value... statement
    graph_the_exits(starting_room)
    print(f"brand new room graph: {graph} ")

    # step 2: push the starting room
    s.push(starting_room)
    # step 3: create a path to track moves to send back via RETURN
    path = []
    # initialize the unexplored_exits of the starting room if first_time
    # graph_the_exits(starting_room)
    # Now go thru with graph
    direction = "just one room"
    entryway = None
    while s.size() > 0:
        # pop the current room
        room = s.pop()
        # check if the current room is the end of the graph
        if not the_last_room(room, entryway):
            # Get the next direction to travel from any door which is unknown... '?'
            for key, value in graph[room.id].items():
                if '?' == value:
                    direction = key
            if direction == "just one room":
                return path
            print(f"A direction to move next is: {direction}")

            # Move the player to the next room, and record the path used, note the doorway just used
            player.travel(direction)
            path.append(direction)
            print(f"path: {path}")
            entryway = opposite_direction_from(direction) # tested, works
            # get newest room and graph the entryway door
            next_room = player.current_room
            print(next_room)
            graph_the_exits(next_room, room, entryway)

            print(f"newly updated room graph: {graph} ")

            # push current room into the stack
            s.push(next_room)
        else:
            print("do a breadth first search to find an empty room")
            print("travel to that empty room")
            print("do depth first search again")

    return path

def theres_an_unexplored_exit_in_this(room):
    exits = room.get_exits()
    for exit in exits:
        print(f"processing exit door... {exit}")
        if graph[room.id][exit] is '?':
            print("returned: FOUND THE ROOM!")
            return True
    # if you avoid line 139 then room has no unexplored exits
    print("keep moving")
    return False



def bfs(starting_room):
        # step 1: create a queue to store rooms
        q = Queue()
        # step 2: enqueue the starting room
        print(f"\n &&&&&&&&&&&&&&&&&&& bfs begins at room # {starting_room.id} &&&&&&&&&&&&&&&&&&&&")
        q.enqueue( [starting_room] )
        # step 3: create a set to store visited rooms, or we can just use our graph
        visited = set()
        # while queue is not empty...
        while q.size() > 0:
             # dequeue the first room into our path, note that q has lists
             path = q.dequeue()            
             # grab the most recent room
             room = path[-1]
             #  check if room has any '?' 
             if room not in visited:
             #  if it hasn't been visitied...
                 # mark it as visited
                 visited.add(room)
                 # check if it's the room with a '?'
                 if theres_an_unexplored_exit_in_this(room):
                     # if so return the PATH
                     print("Kicking Out of bfs")
                     return path
                 #  enqueue a PATH to all of it's nieghbors
                 for exit in room.get_exits():
                     # make a copy of the path
                     #  neighboring_roomID_associated_with_exit = graph[room.id][exit]
                     adjacent_room = room.get_room_in_direction(exit)
                     print(f"adjacent room is... {adjacent_room}")
                     new_path = path

                     new_path.append(adjacent_room)
                     print(f"newPath: {new_path}")
                     # enque the copy
                     q.enqueue(new_path)


def travel_back(back_path):

    # check for circularity?

    # check to make sure algo doesn't take you down the same path as last time, aka
          # check to make sure that upon calling depth-1st-tr it looks for a '?' room to head

    for each_door in range(len(back_path)):
        # door will be 3 then 0 for first pass back from cross's first dft
        player.travel(each_door)
        print(f"hello new room! {player.current_room.id}")

def reverse_path(path):
    reversed_path = []
    for i in range(len(path)):
        element = path.pop()
        oppo = opposite_direction_from(element)
        reversed_path.append(oppo)


# ... continuation of MAIN CODE
# Loop until the map we build is as long as the given groom graph
#while len(graph) < len(room_graph):
for i in range(6):
    print(f"$$$$$$$$$$$$$$$$$$$$$$$$$${i}$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")

    start_room = player.current_room

    # travel til room has no unexplored exits
    traversal_path = depth_first_traverse_from(start_room)
    print(f"your are here! {player.current_room.id}")
    print(traversal_path)
    # do breadth-fs for nearest unexplored exit with graph already filled out only
    from_starting_room = player.current_room
    # reversed_path = reverse_path(traversal_path)
    back_path = bfs(from_starting_room)
    # MIGHT need to take the initial path item out of back_path bc it will be the starting room
    # you'd do this by using "remove" from the 0th position
    print(f"@@@@@@@@@@@@@@@@backpath is: {back_path}@@@@@@@@@@@@@@@@@@@@@")
    traversal_path.append(back_path)
    print(f"@@@@@@@@@@@@@@@@TOTALpath is now: {traversal_path}@@@@@@@@@@@@@@@@@@@@@")
    travel_back(back_path)
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
