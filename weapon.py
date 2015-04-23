import json


class Weapon:

    def __init__(self, name, damage):
        self.name = name
        self.damage = damage

    def __str__(self):
        message = "{} with damage = {}"
        message = message.format(self.name, self.damage)

        return message

    def get_damage(self):
        return self.damage

    def get_name(self):
        return self.name

    def prepare_json(self):
        data = {
            "name": self.name,
            "damage": self.damage
        }

        return data

    def save(self):
        with open("weapon.json", "w") as file:
            file.write(json.dumps(self.prepare_json(), indent=True))

    @staticmethod
    def load(path):
        with open(path, "r") as file:
            file_content = file.read()

        data = json.loads(file_content)

        name = data["name"]
        damage = data["damage"]

        return Weapon(name, damage)
