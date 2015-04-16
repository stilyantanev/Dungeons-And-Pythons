class Dungeon():

    def __init__(self, file_name):
        self.file_name = file_name

    def print_map(self):
        with open(str(self.file_name), "r") as dungeon_map:
            for line in dungeon_map:
                splitted_line = line.rstrip("\n")
                print (splitted_line)
