def part_1():
    outcomes: dict = {'A': ['Z', 'X', 'Y'], 'B': ['X', 'Y', 'Z'], 'C': ['Y', 'Z', 'X']}
    values: dict = {'X': 1, 'Y': 2, 'Z': 3}
    score: int = 0

    with open("input") as file:
        for line in file.readlines():
            opponents_choice, your_choice = line.split()
            outcome = outcomes[opponents_choice].index(your_choice) * 3
            score += outcome + values[your_choice]
    return score


def part_2():
    outcomes: dict = {'A': [3, 1, 2], 'B': [1, 2, 3], 'C': [2, 3, 1]}
    selected: list = ['X', 'Y', 'Z']
    score: int = 0

    with open("input") as file:
        for line in file.readlines():
            opponents_choice, your_choice = line.split()
            what_to_do = selected.index(your_choice)
            score += what_to_do * 3 + outcomes[opponents_choice][what_to_do]
    return score


if __name__ == '__main__':
    print(f"the score for part_1 is: {part_1()}")
    print(f"the score for part_2 is: {part_2()}")
