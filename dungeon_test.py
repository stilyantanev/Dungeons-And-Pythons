from dungeon import Dungeon
from hero import Hero
import unittest


class TestDungeon(unittest.TestCase):

    def setUp(self):
        self.map_level1 = Dungeon('level1.txt')
        self.hunter = Hero("Hunta", "Arrow", 120, 120, 2)

    def test_init(self):
        self.assertTrue(isinstance(self.map_level1, Dungeon))

    def test_spawn(self):
        expected_map_after_spawning = [
            ['H', '.', '#', '#', '.', '.', '.', '.', '.', 'T'],
            ['#', 'T', '#', '#', '.', '.', '#', '#', '#', '.'],
            ['#', '.', '#', '#', '#', 'E', '#', '#', '#', 'E'],
            ['#', '.', 'E', '.', '.', '.', '#', '#', '#', '.'],
            ['#', '#', '#', 'T', '#', '#', '#', '#', '#', 'G']
        ]
        self.map_level1.spawn(self.hunter)
        self.assertEqual(self.map_level1.map, expected_map_after_spawning)


if __name__ == '__main__':
    unittest.main()
