
# what's interesting about this class, is that it's generic
# so long as starting_room is passed in as a proper Room class, 
# then this Player class will have access to methods like .get_room_in_direction and print_room



class Player:
    def __init__(self, starting_room):
        self.current_room = starting_room
    def travel(self, direction, show_rooms = False):
        next_room = self.current_room.get_room_in_direction(direction)
        if next_room is not None:
            self.current_room = next_room
            if (show_rooms):
                next_room.print_room_description(self)
        else:
            print("You cannot move in that direction.")
