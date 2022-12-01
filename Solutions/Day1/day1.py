
def retrieve_input():
    return [line.strip() for line in open('input.txt')]


def solve_part1():
    lines = retrieve_input()
    max_calories = 0
    current_elf_calories = 0
    for line in lines:
        if len(line) == 0:
            if current_elf_calories > max_calories:
                max_calories = current_elf_calories
            current_elf_calories = 0
            continue
        current_elf_calories += int(line)
    if current_elf_calories > max_calories:
        max_calories = current_elf_calories
    return max_calories


def solve_part2():
    lines = retrieve_input()
    elf_calories = []
    current_elf_calories = 0
    for line in lines:
        if len(line) == 0:
            elf_calories.append(current_elf_calories)
            current_elf_calories = 0
            continue
        current_elf_calories += int(line)
    elf_calories.append(current_elf_calories)
    sorted_elf_categories = sorted(elf_calories)
    sorted_elf_categories.reverse()
    return sum(sorted_elf_categories[:3])


if __name__ == "__main__":
    print(solve_part1())  # 69528
    print(solve_part2())  # 206152
