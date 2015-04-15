import unittest
from hero import Hero


class HeroTest(unittest.TestCase):

    def setUp(self):
        self.hunter = Hero(name="Hunta", title="Arrow", health=120, mana=120, mana_rate=2)

    def test_create_new_instance(self):
        self.assertTrue(isinstance(self.hunter, Hero))

    def test_valid_members(self):
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

    def test_take_healing_with_more_points_than_start_health(self):
        self.hunter.health = 80
        self.assertEqual(self.hunter.take_healing(200), True)
        self.assertEqual(self.hunter.health, 120)

    def test_take_healing_with_less_points_than_start_health(self):
        self.hunter.health = 90
        self.assertEqual(self.hunter.take_healing(20), True)
        self.assertEqual(self.hunter.health, 110)

    # def test_take_mana_with_more_points_than_start_mana(self):
    #     pass

    # def test_take_mana_with_negative_mana(self):
    #     pass

    # def test_take_mana_with_less_points_than_start_mana(self):
    #     pass

if __name__ == '__main__':
    unittest.main()
