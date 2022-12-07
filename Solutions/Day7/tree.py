class Tree:
    def __init__(self, name, parent):
        self.name = name
        self.children = []
        self.parent = parent
        self.size = 0

    def get_parent(self):
        return self.parent

    def add_file(self, file_line):
        self.size += int(file_line.split(" ")[0])

    def add_directory(self, dir_line):
        self.children.append(Tree(dir_line.split(" ")[1], self))

    def get_child_by_name(self, name):
        for child in self.children:
            if child.name == name:
                return child
