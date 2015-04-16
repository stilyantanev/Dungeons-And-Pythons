class Enemy:

    def __init__(self, health=100, mana=100, damage=20):
        self.health = health
        self.mana = mana
        self.damage = damage

        self.max_mana = mana
        self.max_health = health

    def is_alive(self):
        if self.health > 0:
            return True
        return False

    def can_cast(self):
        return self.mana != 0

    def get_health(self):
        return self.health

    def get_mana(self):
        # Add functionality for given magic
        return self.mana

    def take_healing(self, healing_points):
        if not self.is_alive():
            return False

        if healing_points + self.health < self.max_health:
            self.health += healing_points
        else:
            self.health = self.max_health

    def take_mana(self, mana_points):
        if self.mana + mana_points < 0:
            self.mana = 0
        elif self.mana + mana_points > self.max_mana:
            self.mana = self.max_mana
        else:
            self.mana += mana_points

    def attack(self):
        pass
