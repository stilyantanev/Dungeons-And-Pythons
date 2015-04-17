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
                    return True
        return False

    def get_current_position(self):
        position = {}
        for row in range(0, len(self.map)):
            for col in range(0, len(self.map[row])):
                if self.map[row][col] == 'H':
                    position[0] = row
                    position[1] = col

        return position

    def move_hero(self, direction):
        current_position = self.get_current_position()
        row = current_position[0]
        col = current_position[1]

        if direction == "up":
            if row - 1 > 0:

                if self.map[row - 1][col] == '#':
                    return False

                elif self.map[row - 1][col] == '.':
                    self.map[row][col] = '.'
                    self.map[row - 1][col] = 'H'
                    return True

                elif self.map[row - 1][col] == 'T':
                    print ("Found treasure!")
                    self.map[row][col] = '.'
                    self.map[row - 1][col] = 'H'
                    return True

                elif self.map[row - 1][col] == 'E':
                    pass

            else:
                return False

        if direction == "down":
            if row + 1 < len(self.map):

                if self.map[row + 1][col] == '#':
                    return False

                elif self.map[row + 1][col] == '.':
                    self.map[row][col] = '.'
                    self.map[row + 1][col] = 'H'
                    return True

                elif self.map[row + 1][col] == 'T':
                    print ("Found treasure!")
                    self.map[row][col] = '.'
                    self.map[row + 1][col] = 'H'
                    return True

                elif self.map[row + 1][col] == 'E':
                    pass

            else:
                return False

        if direction == "left":
            if col - 1 > 0:

                if self.map[row][col - 1] == '#':
                    return False

                elif self.map[row][col - 1] == '.':
                    self.map[row][col] = '.'
                    self.map[row][col - 1] = 'H'
                    return True

                elif self.map[row][col - 1] == 'T':
                    print ("Found treasure!")
                    self.map[row][col] = '.'
                    self.map[row][col - 1] = 'H'
                    return True

                elif self.map[row][col - 1] == 'E':
                    pass

            else:
                return False

        if direction == "right":
            if col + 1 < len(self.map[row]):

                if self.map[row][col + 1] == '#':
                    return False

                elif self.map[row][col + 1] == '.':
                    self.map[row][col] = '.'
                    self.map[row][col + 1] = 'H'
                    return True

                elif self.map[row][col + 1] == 'T':
                    print ("Found treasure!")
                    self.map[row][col] = '.'
                    self.map[row][col + 1] = 'H'
                    return True

                elif self.map[row][col + 1] == 'E':
                    pass

            else:
                return False
