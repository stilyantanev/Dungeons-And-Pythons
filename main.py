from hero import Hero
from dungeon import Dungeon
from weapon import Weapon

if __name__ == '__main__':

    hero = Hero("Ragnar", "Lothbrok", 20, 100, 2)
    knife = Weapon("Knife", 50)
    hero.weapon = knife
    dungeon = Dungeon.load_map_from_file("level1.txt")

    print("Hello, You are in our game! Exit from dungeon, marry to princess!")
    print("Move by typing 'l,L(left)', 'r,R(right)', 'u,U(up)', 'd,D(down)'")
    print("Attack enemies with f(fight).")
    print("GO GO GO HERO!")
    print()

    dungeon.spawn(hero)

    while hero.is_alive() or dungeon.spawn(hero):

        dungeon.print_map()

        move = input("Choose your move: ")
        is_there_gate = False

        if move == "W" or move == "w":
            is_there_gate = dungeon.move_hero("u")

        elif move == "A" or move == "a":
            is_there_gate = dungeon.move_hero("l")

        elif move == "S" or move == "s":
            is_there_gate = dungeon.move_hero("d")

        elif move == "D" or move == "d":
            is_there_gate = dungeon.move_hero("r")

        elif move == "F" or move == "f":
            dungeon.hero_attack(hero)

        if is_there_gate:
                dungeon = Dungeon.load_map_from_file("level2.txt")
                dungeon.spawn(hero)

    print("You fall down! Try Again!")
