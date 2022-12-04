def retrieve_input():
    return [x.strip() for x in open('input.txt')]


def solve_part1():
    lines = retrieve_input()
    total_inside = 0
    for line in lines:
        left_elf = line.split(",")[0]
        right_elf = line.split(",")[1]
        if (int(left_elf.split("-")[0]) <= int(right_elf.split("-")[0]) and int(left_elf.split("-")[1]) >= int(right_elf.split("-")[1])) or (int(left_elf.split("-")[0]) >= int(right_elf.split("-")[0]) and int(left_elf.split("-")[1]) <= int(right_elf.split("-")[1])):
            total_inside += 1
    return total_inside


def solve_part2():
    lines = retrieve_input()
    total_overlap = 0
    for line in lines:
        left_elf = line.split(",")[0]
        right_elf = line.split(",")[1]
        if (int(left_elf.split("-")[0]) <= int(right_elf.split("-")[0]) and int(left_elf.split("-")[1]) >= int(right_elf.split("-")[1])) or (int(left_elf.split("-")[0]) >= int(right_elf.split("-")[0]) and int(left_elf.split("-")[1]) <= int(right_elf.split("-")[1])):
            total_overlap += 1
        elif int(right_elf.split("-")[0]) <= int(left_elf.split("-")[0]) <= int(right_elf.split("-")[1]):
            total_overlap += 1
        elif int(left_elf.split("-")[0]) <= int(right_elf.split("-")[0]) <= int(left_elf.split("-")[1]):
            total_overlap += 1
    return total_overlap


if __name__ == "__main__":
    print(solve_part1())  # 571
    print(solve_part2())  # 917
