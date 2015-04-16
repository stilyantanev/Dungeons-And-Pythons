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
        # Add functionality for given magic!!!
        return self.mana != 0

    def get_health(self):
        return self.health

    def get_mana(self):
        return self.mana

    def take_healing(self, healing_points):
        if self.health == 0:
            return False
        elif self.health + healing_points >= self.max_health:
            self.health = self.max_health
            return True
        elif self.health + healing_points < self.max_health:
            self.health += healing_points
            return True

    def take_mana(self, mana_points):
        if self.mana + mana_points >= self.max_mana:
            self.mana = self.max_mana
        elif self.mana + mana_points <= 0:
            self.mana = 0
        else:
            self.mana += mana_points

    def equip(self, weapon):
        self.weapon = weapon

    def learn(self, spell):
        self.spell = spell

    def attack(self, by=""):
        if hasattr(self, 'weapon') and by == "weapon":
            return self.weapon.damage + self.damage
        elif hasattr(self, 'spell') and by == "spell":
            return self.spell.damage + self.damage
        else:
            return 0
