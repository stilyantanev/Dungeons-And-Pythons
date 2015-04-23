import unittest
from enemy import Enemy
from weapon import Weapon
from spell import Spell


class TestEnemy(unittest.TestCase):

    def setUp(self):
        self.enemy = Enemy(health=110, mana=110, damage=35)

    def test_create_new_instance(self):
        self.assertTrue(isinstance(self.enemy, Enemy))

    def test_valid_members(self):
        self.assertEqual(self.enemy.health, 110)
        self.assertEqual(self.enemy.mana, 110)
        self.assertEqual(self.enemy.damage, 35)

        self.assertEqual(self.enemy.max_health, 110)
        self.assertEqual(self.enemy.max_mana, 110)

    def test_is_alive(self):
        self.assertEqual(self.enemy.is_alive(), True)

        self.enemy.health = 0
        self.assertEqual(self.enemy.is_alive(), False)

    def test_can_cast(self):
        self.assertTrue(self.enemy.can_cast())

    def test_get_health(self):
        self.assertEqual(self.enemy.get_health(), 110)

    def test_get_mana(self):
        self.assertEqual(self.enemy.get_mana(), 110)

    def test_take_healing_dead_enemy(self):
        self.enemy.health = 0
        self.assertEqual(self.enemy.take_healing(200), False)

    def test_take_healing_with_more_points_than_max_health(self):
        self.enemy.health = 80
        self.assertEqual(self.enemy.take_healing(200), True)
        self.assertEqual(self.enemy.health, 110)

    def test_take_healing_with_less_points_than_max_health(self):
        self.enemy.health = 90
        self.assertEqual(self.enemy.take_healing(20), True)
        self.assertEqual(self.enemy.health, 110)

    def test_take_mana_with_more_points_than_max_mana(self):
        self.enemy.mana = 80
        self.enemy.take_mana(200)
        self.assertEqual(self.enemy.mana, 110)

    def test_take_mana_with_negative_mana(self):
        self.enemy.mana = 50
        self.enemy.take_mana(-60)
        self.assertEqual(self.enemy.mana, 0)

    def test_take_mana_with_less_points_than_max_mana(self):
        self.enemy.mana = 65
        self.enemy.take_mana(20)
        self.assertEqual(self.enemy.mana, 85)

    def test_equip(self):
        knife = Weapon("Knife", 10)
        self.enemy.equip(knife)
        self.assertEqual(self.enemy.weapon, knife)

    def test_learn(self):
        mind_blast = Spell("Mind Blast", 20, 55, 2)
        self.enemy.learn(mind_blast)
        self.assertEqual(self.enemy.spell, mind_blast)

    def test_attack_with_weapon(self):
        knife = Weapon("Sword", 50)
        self.enemy.equip(knife)
        self.assertEqual(self.enemy.attack(by="weapon"), 50)

    def test_attack_with_spell(self):
        fire_blast = Spell("Fire Blast", 40, 30, 1)
        self.enemy.learn(fire_blast)
        self.assertEqual(self.enemy.attack(by="spell"), 40)

if __name__ == '__main__':
    unittest.main()
