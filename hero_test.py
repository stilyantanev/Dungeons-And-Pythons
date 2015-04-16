import unittest
from hero import Hero
from weapons_and_spells import Weapon
from weapons_and_spells import Spell


class HeroTest(unittest.TestCase):

    def setUp(self):
        self.hunter = Hero("Hunta", "Arrow", 120, 120, 2)

    def test_create_new_instance(self):
        self.assertTrue(isinstance(self.hunter, Hero))

    def test_valid_members(self):
        self.assertEqual(self.hunter.max_health, 120)
        self.assertEqual(self.hunter.max_mana, 120)

        self.assertEqual(self.hunter.name, "Hunta")
        self.assertEqual(self.hunter.title, "Arrow")
        self.assertEqual(self.hunter.health, 120)
        self.assertEqual(self.hunter.mana, 120)
        self.assertEqual(self.hunter.mana_regeneration_rate, 2)

    def test_known_as(self):
        self.assertEqual(self.hunter.known_as(), "Hunta the Arrow")

    def test_get_health(self):
        self.assertEqual(self.hunter.get_health(), 120)

    def test_get_mana(self):
        self.assertEqual(self.hunter.get_mana(), 120)

    def test_is_alive(self):
        self.assertEqual(self.hunter.is_alive(), True)

    def test_can_cast(self):
        self.assertEqual(self.hunter.can_cast(), True)

    def test_take_damage_more_than_health(self):
        self.hunter.take_damage(150)
        self.assertEqual(self.hunter.health, 0)

    def test_take_damage_less_than_health(self):
        self.hunter.take_damage(100)
        self.assertEqual(self.hunter.health, 20)

    def test_take_healing_dead_hero(self):
        self.hunter.health = 0
        self.assertEqual(self.hunter.take_healing(200), False)

    def test_take_healing_with_more_points_than_max_health(self):
        self.hunter.health = 80
        self.assertEqual(self.hunter.take_healing(200), True)
        self.assertEqual(self.hunter.health, 120)

    def test_take_healing_with_less_points_than_max_health(self):
        self.hunter.health = 90
        self.assertEqual(self.hunter.take_healing(20), True)
        self.assertEqual(self.hunter.health, 110)

    def test_take_mana_with_more_points_than_max_mana(self):
        self.hunter.mana = 80
        self.hunter.take_mana(200)
        self.assertEqual(self.hunter.mana, 120)

    def test_take_mana_with_negative_mana(self):
        self.hunter.mana = 50
        self.hunter.take_mana(-60)
        self.assertEqual(self.hunter.mana, 0)

    def test_take_mana_in_ordinary_case(self):
        self.hunter.mana = 65
        self.hunter.take_mana(20)
        self.assertEqual(self.hunter.mana, 85)

    def test_equip(self):
        axe = Weapon()
        self.hunter.equip(axe)
        self.assertEqual(self.hunter.weapon, axe)

    def test_learn(self):
        fireball = Spell()
        self.hunter.learn(fireball)
        self.assertEqual(self.hunter.spell, fireball)

    def test_atack_without_nothing(self):
        self.assertEqual(self.hunter.attack(), 0)

    def test_attack_with_weapon(self):
        axe = Weapon()
        self.hunter.equip(axe)
        self.assertEqual(self.hunter.attack(by="weapon"), 20)

    def test_attack_with_spell(self):
        fireball = Spell()
        self.hunter.learn(fireball)
        self.assertEqual(self.hunter.attack(by="spell"), 30)

if __name__ == '__main__':
    unittest.main()
