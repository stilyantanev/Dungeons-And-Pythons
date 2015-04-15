class Enemy:

    def __init__(self, health=100, mana=100, damage=20):
        self.health = health
        self.mana = mana
        self.damage = damage

        self.start_mana = mana

    def is_alive(self):
        if self.health > 0:
            return True
        return False

    def can_cast(self):
        return self.mana != 0

    def get_health(self):
        return self.health

    def get_mana(self):
        return self.mana

    def take_healing(self, healing_points):
        if not self.is_alive():
            return False

        if healing_points + self.health < 100:
            self.health += healing_points
        else:
            self.health = 100

        return self.health

    def take_mana(self, mana_points):
        if self.mana + mana_points < 0:
            self.mana = 0
        elif self.mana + mana_points > self.start_mana:
            self.mana = self.start_mana
        else:
            self.mana += mana_points

        return self.mana

    def attack(self):
        pass
