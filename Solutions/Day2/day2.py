part1_table = [[4, 8, 3],
               [1, 5, 9],
               [7, 2, 6]]

part2_table = [[3, 4, 8],
               [1, 5, 9],
               [2, 6, 7]]

letterToIndexMapping = {"A": 0, "B": 1, "C": 2, "X": 0, "Y": 1, "Z": 2}


def retrieve_input():
    return [x.strip() for x in open('input.txt')]


def solve_part1():
    lines = retrieve_input()
    total_score = 0
    for line in lines:
        choices = line.split(" ")
        total_score += part1_table[letterToIndexMapping.get(choices[0])][letterToIndexMapping.get(choices[1])]
    return total_score


def solve_part2():
    lines = retrieve_input()
    total_score = 0
    for line in lines:
        choices = line.split(" ")
        total_score += part2_table[letterToIndexMapping.get(choices[0])][letterToIndexMapping.get(choices[1])]
    return total_score


if __name__ == "__main__":
    print(solve_part1())  # 13446
    print(solve_part2())  # 13509
