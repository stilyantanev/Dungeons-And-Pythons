import unittest
from weapons_and_spells import Weapon
from weapons_and_spells import Spell


class WeaponTest(unittest.TestCase):

    def setUp(self):
        self.weapon = Weapon()

    def test_is_instance(self):
        self.assertTrue(isinstance(self.weapon, Weapon))

    def test_valid_members(self):
        self.assertEqual(self.weapon.name, "The Axe of Destiny")
        self.assertEqual(self.weapon.damage, 20)

    def test_str(self):
        expected = "The Axe of Destiny with damage=20"
        self.assertEqual(str(self.weapon), expected)


class SpellTest(unittest.TestCase):

    def setUp(self):
        self.spell = Spell()

    def test_is_instance(self):
        self.assertTrue(isinstance(self.spell, Spell))

    def test_valid_members(self):
        self.assertEqual(self.spell.name, "Fireball")
        self.assertEqual(self.spell.damage, 30)
        self.assertEqual(self.spell.mana_cost, 50)
        self.assertEqual(self.spell.cast_range, 2)

if __name__ == '__main__':
    unittest.main()
