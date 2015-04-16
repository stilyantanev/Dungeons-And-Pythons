class Dungeon():

    def __init__(self, file_name):
        self.file_name = file_name
        self.map = []

        with open(file_name, "r") as opened:
            lines_list = opened.read().splitlines()

            for line in lines_list:
                self.map.append(list(line))

    def print_map(self):
        for line in self.map:
            print (line)

    def spawn(self, hero):
        for row in range(0, len(self.map)):
            for col in range(0, len(self.map[row])):
                if self.map[row][col] == 'S':
                    self.map[row][col] = 'H'


