from dungeon import Dungeon
import unittest


class TestDungeon(unittest.TestCase):

    def setUp(self):
        self.map_level1 = Dungeon('level1.txt')

    def test_init(self):
        self.assertTrue(isinstance(self.map_level1, Dungeon))

    def test_print_correct_map(self):
        pass

if __name__ == '__main__':
    unittest.main()
