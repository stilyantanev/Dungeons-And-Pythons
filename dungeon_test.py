from dungeon import Dungeon
from hero import Hero
from dungeon import NotAHero
from dungeon import NotValidDirection
import unittest


class TestDungeon(unittest.TestCase):

    def setUp(self):
        self.map_level1 = Dungeon('level1.txt')
        self.hunter = Hero("Hunta", "Arrow", 120, 120, 2)

    def test_init(self):
        self.assertTrue(isinstance(self.map_level1, Dungeon))

    def test_map_loading(self):
        expected = [['S', '.', '#', '#', '.', '.', '.', '.', '.', 'T'],
                    ['#', 'T', '#', '#', '.', '.', '#', '#', '#', '.'],
                    ['#', '.', '#', '#', '#', 'E', '#', '#', '#', 'E'],
                    ['#', '.', 'E', '.', '.', '.', '#', '#', '#', '.'],
                    ['#', '#', '#', 'T', '#', '#', '#', '#', '#', 'G']]
        self.assertEqual(self.map_level1.map, expected)

    def test_spawn(self):
        with self.assertRaises(NotAHero):
            self.map_level1.spawn(1234)

        expected_map_after_spawning = [
            ['H', '.', '#', '#', '.', '.', '.', '.', '.', 'T'],
            ['#', 'T', '#', '#', '.', '.', '#', '#', '#', '.'],
            ['#', '.', '#', '#', '#', 'E', '#', '#', '#', 'E'],
            ['#', '.', 'E', '.', '.', '.', '#', '#', '#', '.'],
            ['#', '#', '#', 'T', '#', '#', '#', '#', '#', 'G']
        ]

        self.assertTrue(self.map_level1.spawn(self.hunter))
        self.assertEqual(self.map_level1.map, expected_map_after_spawning)
        self.assertEqual(self.map_level1.map[0][0], "H")

    def test_move_hero(self):
        self.map_level1.spawn(self.hunter)
        self.assertEqual(self.map_level1.get_current_position(), {0: 0, 1: 0})
        self.assertTrue(self.map_level1.move_hero("right"))
        self.assertEqual(self.map_level1.get_current_position(), {0: 0, 1: 1})
        self.assertEqual(self.map_level1.map[0][0], ".")

        self.assertFalse(self.map_level1.move_hero("up"))

        self.assertEqual(self.map_level1.map[1][1], "T")
        self.assertTrue(self.map_level1.move_hero("down"))
        self.assertEqual(self.map_level1.get_current_position(), {0: 1, 1: 1})
        self.assertEqual(self.map_level1.map[0][1], '.')
        self.assertEqual(self.map_level1.map[1][1], "H")

        self.assertFalse(self.map_level1.move_hero("left"))
        self.assertEqual(self.map_level1.map[1][0], "#")

        self.assertFalse(self.map_level1.move_hero("right"))
        self.assertEqual(self.map_level1.map[1][2], "#")

        with self.assertRaises(NotValidDirection):
            self.map_level1.move_hero("asd")

if __name__ == '__main__':
    unittest.main()
