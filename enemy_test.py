from enemy import Enemy
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

    def test_healing(self):
        dead_enemy = Enemy(health=0, mana=100, damage=20)
        some_enemy = Enemy(health=50, mana=100, damage=20)
        dead_enemy.take_healing(10)
        some_enemy.take_healing(10)

        self.assertEqual(some_enemy.health, 50)
        self.assertEqual(dead_enemy.health, 0)

        enemy1 = Enemy(health=10, mana=100, damage=20)
        enemy1.health = 5
        enemy1.take_healing(2)
        self.assertEqual(enemy1.health, 7)

    def test_take_mana(self):
        self.enemy.take_mana(-10)
        self.assertTrue(self.enemy.get_mana() == 90)

        self.enemy.take_mana(10)
        self.assertTrue(self.enemy.get_mana() == 100)

        some_enemy = Enemy(health=50, mana=50, damage=20)
        some_enemy.take_mana(100)
        self.assertTrue(some_enemy.get_mana() == 50)

        some_enemy.take_mana(-100)
        self.assertTrue(some_enemy.get_mana() == 0)

if __name__ == '__main__':
    unittest.main()
