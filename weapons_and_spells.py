class Weapon:

    def __init__(self, name="The Axe of Destiny", damage=20):
        self.name = name
        self.damage = damage

    def __str__(self):
        return "{} with damage={}".format(self.name, self.damage)


class Spell:

    def __init__(self, name="Fireball", damage=30, mana_cost=50, cast_range=2):
        self.name = name
        self.damage = damage
        self.mana_cost = mana_cost
        self.cast_range = cast_range
