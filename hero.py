class Hero:

    def __init__(self, name="", title="", health=100, mana=100, mana_rate=2):
        self.max_health = health
        self.max_mana = mana

        self.name = name
        self.title = title
        self.health = health
        self.mana = mana
        self.mana_regeneration_rate = mana_rate

    def known_as(self):
        nickname = "{} the {}".format(self.name, self.title)
        return nickname

    def get_health(self):
        return self.health

    def get_mana(self):
        return self.mana

    def is_alive(self):
        return self.health != 0

    def can_cast(self):
        # Add functionality for given magic
        return self.mana != 0

    def take_damage(self, damage_points):
        if self.health <= damage_points:
            self.health = 0
        elif self.health > damage_points:
            self.health -= damage_points

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
        # Add move functionality
        if self.mana + mana_points >= self.max_mana:
            self.mana = self.max_mana
        elif self.mana + mana_points <= 0:
            self.mana = 0
        else:
            self.mana += mana_points

    def equip(weapon):
        pass

    def learn(spell):
        pass

    def attack(by=""):
        pass
