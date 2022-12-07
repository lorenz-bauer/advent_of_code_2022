import re
def part1():
    crates = {1: "", 2: "", 3: "", 4: "", 5: "", 6: "", 7: "", 8: "", 9: ""}
    with open("input", "r") as file:
        lines: list = file.readlines()
        index = 0

        for i in range(len(lines)):
            if lines[i] == '\n':
                index += 1
                break
            for y in range(len(lines[i])):
                if lines[i][y].isalpha():
                    crates[y // 4 + 1] += lines[i][y]
            index += 1
        for i in range(len(lines) - index):
            move(crates, lines[index + i], False)

        return crates

def part2():
    crates = {1: "", 2: "", 3: "", 4: "", 5: "", 6: "", 7: "", 8: "", 9: ""}
    with open("input", "r") as file:
        lines: list = file.readlines()
        index = 0

        for i in range(len(lines)):
            if lines[i] == '\n':
                index += 1
                break
            for y in range(len(lines[i])):
                if lines[i][y].isalpha():
                    crates[y // 4 + 1] += lines[i][y]
            index += 1
        for i in range(len(lines) - index):
            move(crates, lines[index + i], True)

        return crates

def move(crates: dict, line: str, is_crateMover_9001:bool):
    information = re.findall("\d+", line)
    quantity: int = int(information[0])
    src: int = int(information[1])
    dst: int = int(information[2])
    crates[dst] = crates[src][:quantity][::1 if is_crateMover_9001 else -1] + crates[dst]
    crates[src] = crates[src][quantity:]


def print_crates(crates:dict):
    for line in crates.values():
        if line:
            print(line[0], end="")
    print()

if __name__ == '__main__':
    print("The answer for part1 is : ")
    print_crates(part1())
    print("The answer for part2 is : ")
    print_crates(part2())
