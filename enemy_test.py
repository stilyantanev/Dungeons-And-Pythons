from enemy import Enemy
from weapons_and_spells import Weapon
from weapons_and_spells import Spell
import unittest


class TestEnemy(unittest.TestCase):

    def setUp(self):
        self.enemy = Enemy(health=100, mana=100, damage=20)

    def test_init(self):
        self.assertTrue(self.enemy.health == 100)
        self.assertTrue(self.enemy.mana == 100)
        self.assertTrue(self.enemy.damage == 20)

    def test_is_alive(self):
        self.assertTrue(self.enemy.is_alive())

    def test_can_cast(self):
        self.assertTrue(self.enemy.can_cast())

    def test_get_health(self):
        self.assertEqual(self.enemy.get_health(), 100)

    def test_get_mana(self):
        self.assertEqual(self.enemy.get_mana(), 100)

    def test_take_healing_dead_enemy(self):
        self.enemy.health = 0
        self.assertEqual(self.enemy.take_healing(200), False)

    def test_take_healing_with_more_points_than_max_health(self):
        self.enemy.health = 80
        self.assertEqual(self.enemy.take_healing(200), True)
        self.assertEqual(self.enemy.health, 100)

    def test_take_healing_with_less_points_than_max_health(self):
        self.enemy.health = 90
        self.assertEqual(self.enemy.take_healing(5), True)
        self.assertEqual(self.enemy.health, 95)

    def test_take_mana_with_more_points_than_max_mana(self):
        self.enemy.mana = 80
        self.enemy.take_mana(200)
        self.assertEqual(self.enemy.mana, 100)

    def test_take_mana_with_negative_mana(self):
        self.enemy.mana = 50
        self.enemy.take_mana(-60)
        self.assertEqual(self.enemy.mana, 0)

    def test_take_mana_in_ordinary_case(self):
        self.enemy.mana = 65
        self.enemy.take_mana(20)
        self.assertEqual(self.enemy.mana, 85)

    def test_equip(self):
        axe = Weapon()
        self.enemy.equip(axe)
        self.assertEqual(self.enemy.weapon, axe)

    def test_learn(self):
        fireball = Spell()
        self.enemy.learn(fireball)
        self.assertEqual(self.enemy.spell, fireball)

    def test_atack_without_nothing(self):
        self.assertEqual(self.enemy.attack(), 0)

    def test_attack_with_weapon(self):
        axe = Weapon()
        self.enemy.equip(axe)
        self.assertEqual(self.enemy.attack(by="weapon"), 40)

    def test_attack_with_spell(self):
        fireball = Spell()
        self.enemy.learn(fireball)
        self.assertEqual(self.enemy.attack(by="spell"), 50)

if __name__ == '__main__':
    unittest.main()
