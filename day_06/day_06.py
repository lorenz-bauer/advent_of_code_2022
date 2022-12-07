def part1():
    with open("input", "r") as file:
        for line in file.readlines():
            last_three: list = list(line[:3])
            for index in range(3, len(line)):
                last_three.append(line[index])
                if not contains_duplicates(last_three):
                    return index + 1
                last_three.pop(0)


def part2():
    with open("input", "r") as file:
        for line in file.readlines():
            last_three: list = list(line[:13])
            for index in range(13, len(line)):
                last_three.append(line[index])
                if not contains_duplicates(last_three):
                    return index + 1
                last_three.pop(0)


def contains_duplicates(values: list):
    for value in values:
        if values.count(value) > 1:
            return True
    return False


if __name__ == '__main__':
    print(f"The solution for part_1 is: {part1()}")
    print(f"The solution for part_2 is: {part2()}")
