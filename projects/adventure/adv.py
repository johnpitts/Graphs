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

# Fill this out with directions to walk
# traversal_path = ['n', 'n']

graph = Graph()

# HERE'S WHERE WE NEED IT ALL TO LOOP:
# Get player's current room
start_room = player.current_room
# id = start_room.id

# # HERE BEGINS SMART CODE: COMMENT OUT WHEN TESTING SPAGHETTI
# # travel to the end of the map
# graph.depth_first_traverse_from(start_room)
# # note the room you're in when done dft
# end_room = player.current_room
# # search for next room, to begin again and travel to that room
# path = graph.bfsearch_for_untried_door(end_room)
# graph.bfs_travel_to_untried_door(path)

# rewrite smart code above to LOOP back to depth-Traverse again, after spaghetti code works



# HERE BEGINS SPAGHETTI CODE TO GAIN UNDERSTANDING AND TEST
# Get the exits to the starting room
exits = start_room.get_exits(); print(exits)

# Add starting room to graph
graph.add_room(id, None, None, exits)

# pick a direction to travel based on the available exits
random_direction = random(exits); print(random_direction)

# optimize the random by remembering which path/s already taken so you don't waste time
# is this necessary for "2" or "3"?

# travel to the room randomly selected, and update your traversal_path
traversal_path.append(random_direction)
player.travel(random_direction)
print(player.current_room)
print(traversal_path)



traversal_path = []





    

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
