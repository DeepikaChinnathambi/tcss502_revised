from Dungeon import Dungeon
from Adventurer import Adventurer
from Items import *


class DungeonAdventure:
    def __init__(self):
        print("Welcome to the Dungeon Adventure!")
        self.dungeon = Dungeon(10, 20)
        self.adventurer = self.create_adventurer()
        self.game_over = False
        self.current_room = self.dungeon.entrance

        # Display the dungeon (for debugging purposes)
        print("Full Map generated for debugging purposes, no use for game!")
        self.dungeon.__place_items__()

    def create_adventurer(self):
        name = input("Enter your adventurer's name: ").strip()

        return Adventurer(name)

    def play(self):
        print(f"\nHello, {self.adventurer.name}, You are starting with {self.adventurer.health} health.\nGood luck in the Dungeons... you're gonna need it")
        self.current_room.__repr__()
        while not self.game_over:
            self.handle_player_turn()

    def handle_player_turn(self):
        dir = input(f"Health: {self.adventurer.health}\nPillars: {self.adventurer.pillars}\nHealing Potions: {self.adventurer.healing_potions}, Vision Potions: {self.adventurer.vision_potions}"
                    f"\nEnter your next move (N, S, E, W... North is always up)"
                    f"\nor use your potions, H (healing potion), V (vision potion)"
                    f"\nInput:  ")
        if dir.lower().strip() == "n" and self.current_room.north:
            self.current_room = self.current_room.north
        elif dir.lower().strip() == "e" and self.current_room.east:
            self.current_room = self.current_room.east
        elif dir.lower().strip() == "w" and self.current_room.west:
            self.current_room = self.current_room.west
        elif dir.lower().strip() == "s" and self.current_room.south:
            self.current_room = self.current_room.south
        elif dir.lower().strip() == "v" and self.adventurer.vision_potions > 0:
            self.dungeon.__display_map__(self.current_room.xcoord, self.current_room.ycoord, full_map=False, filename='Vision_Potion_Map.txt')
            print('Vision_Potion_Map.txt has been dropped to you in the room! (open that file and see what awaits)')
        elif dir.lower().strip() == "h" and self.adventurer.healing_potions > 0:
            self.adventurer.take_healing_potions()
        else:
            print("Invalid direction or command!")

        self.current_room.__repr__()

        # print(f"You are in room: {self.current_room.number}")
        for item in self.current_room.items:
            if isinstance(item, HealingPotion):
                self.adventurer.healing_potions = self.current_room.pick_up_item(item)
                print(f"You picked up a Healing potion!")

            if isinstance(item, VisionPotion):
                self.adventurer.vision_potions = self.current_room.pick_up_item(item)
                print(f"You picked up a Vision potion!")

            if isinstance(item, Pit):
                self.adventurer.hit_points(item.hit_points)
                print(f"You fell in a pit! You lost {item.hit_points} health!\nYou now have {self.adventurer.health} health!")

            if isinstance(item, Pillar):
                self.adventurer.pillars = self.current_room.pick_up_item(item)
                print(f"You found a Pillar of OO: ~{item.__str__()}~")

        self.check_game_over()

    def check_game_over(self):
        if self.adventurer.health <= 0:
            print("You have died! Game over.")
            self.game_over = True
        elif self.adventurer.pillars_found == 4:
            print("You have collected all Pillars of OO! You win!")
            self.game_over = True

    def display_dungeon(self):
        print(self.dungeon)


if __name__ == "__main__":
    DungeonAdventure().play()