import string

priority_mapping = {}

index = 1
for letter in list(string.ascii_letters):
    priority_mapping.update({letter: index})
    index += 1


def retrieve_input():
    return [x.strip() for x in open('input.txt')]


def solve_part1():
    lines = retrieve_input()
    total_priority = 0
    for line in lines:
        ruck_sack_left = line[:int(len(line)/2)]
        ruck_sack_right = line[int(len(line)/2):]
        intersect = set(list(ruck_sack_left)).intersection(set(list(ruck_sack_right)))
        for item in intersect:
            total_priority += priority_mapping.get(item)
    return total_priority


def solve_part2():
    lines = retrieve_input()
    i = 0
    total_priority = 0
    while i < len(lines):
        intersect = set(list(lines[i])).intersection(set(list(lines[i+1])).intersection(set(list(lines[i+2]))))
        i += 3
        for item in intersect:
            total_priority += priority_mapping.get(item)
    return total_priority


if __name__ == "__main__":
    print(solve_part1())  # 8039
    print(solve_part2())  # 2510
