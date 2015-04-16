from hero import Hero
from weapons_and_spells import Weapon


def main():

    h = Hero(name="Bron", title="Dragonslayer", health=100,
             mana=100, mana_regeneration_rate=2)
    print(h.known_as())
    # w = Weapon(name="The Axe of Destiny", damage=20)

    # h.equip(w)

    # print(h.attack(by="weapon") == 0)

if __name__ == '__main__':
    main()
