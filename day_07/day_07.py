class Directory():
    def __init__(self, name, parent=None):
        self.name = name
        self.files = []
        self.directories = []
        self.parent = parent

    def add_dir(self, name, parent):
        directory = Directory(name, parent)
        self.directories.append(directory)

    def add_file(self, file_name, file_size):
        file = File(file_name, int(file_size))
        self.files.append(file)

    def calculate_size(self):
        return sum([file.file_size for file in self.files]) \
               + sum([directory.calculate_size() for directory in self.directories])

    def change_directory(self, name):
        if name == "..":
            return self.parent
        for directory in self.directories:
            if directory.name == name:
                return directory
        return None

    def get_directories(self):
        directories = []
        for dir in self.directories:
            directories.append(dir)
            if dir.directories:
                directories += dir.get_directories()
        return directories


    def __repr__(self):
        return f"'Directory('name': '{self.name}, 'Size': {self.calculate_size()}, 'directories': {self.directories})"


class File():
    def __init__(self, name, file_size):
        self.name = name
        self.file_size = file_size

    def __repr__(self):
        return f"'File('name': '{self.name}, 'file_size': {self.file_size})"


def part1():
    root_dir = Directory("/")
    current_directory: Directory = root_dir
    with open("input", "r") as file:
        for line in file.readlines():
            line = line[:-1]
            if line.startswith("$ cd "):
                if not line == "$ cd /":
                    current_directory = current_directory.change_directory(line[5:])
            elif line.startswith("dir"):
                current_directory.add_dir(line[4:], current_directory)
            elif line != "$ ls":
                file_size, name = line.split()
                current_directory.add_file(name, file_size)

    return sum([dir.calculate_size() for dir in root_dir.get_directories() if dir.calculate_size() < 100000])


def part2():
    root_dir = Directory("/")
    current_directory: Directory = root_dir

    with open("input", "r") as file:
        for line in file.readlines():
            line = line[:-1]
            if line.startswith("$ cd "):
                if not line == "$ cd /":
                    current_directory = current_directory.change_directory(line[5:])
            elif line.startswith("dir"):
                current_directory.add_dir(line[4:], current_directory)
            elif line != "$ ls":
                file_size, name = line.split()
                current_directory.add_file(name, file_size)

    free_space = 70000000 - root_dir.calculate_size()
    needed = 30000000 - free_space

    smallest = None
    for dir in root_dir.get_directories():
        if dir.calculate_size() > needed:
            if smallest is None or smallest.calculate_size() > dir.calculate_size():
                smallest = dir

    return smallest.calculate_size()


if __name__ == '__main__':
    print(f"The solution for part_1 is: {part1()}")
    print(f"The solution for part_2 is: {part2()}")
