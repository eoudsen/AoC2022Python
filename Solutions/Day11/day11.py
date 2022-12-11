import math


def retrieve_input():
    return [x.strip() for x in open('input.txt')]


def initialize_monkeys(lines):
    current_monkey_index = 0
    monkey_items = []
    divisible_by = []
    monkey_operation = []
    true_monkey = []
    false_monkey = []
    for line in lines:
        if line.startswith("Monkey"):
            # Start new monkey
            current_monkey_index = int(line.split(" ")[1].rstrip(":"))
            monkey_items.append([])
            continue
        if line.startswith("Starting"):
            split = line.split(" ")
            values = split[2:]
            for value in values:
                if value.__contains__(","):
                    monkey_items[current_monkey_index].append(value.rstrip(","))
                else:
                    monkey_items[current_monkey_index].append(value)
            continue
        if line.startswith("Operation"):
            equation = line.split("=")[1].strip()
            monkey_operation.append(equation)
            continue
        if line.startswith("Test"):
            divisible_by.append(int(line.split(" ")[-1]))
            continue
        if line.startswith("If true"):
            true_monkey.append(int(line.split(" ")[-1]))
            continue
        if line.startswith("If false"):
            false_monkey.append(int(line.split(" ")[-1]))
    return monkey_items, divisible_by, monkey_operation, true_monkey, false_monkey


def execute_operation(equation, item):
    equation = equation.replace("old", str(item))
    if equation.__contains__("+"):
        return int(equation.split(" ")[0]) + int(equation.split(" ")[2])
    return int(equation.split(" ")[0]) * int(equation.split(" ")[2])


def solve_part1():
    lines = retrieve_input()
    monkey_items, divisible_by, monkey_operation, true_monkey, false_monkey = initialize_monkeys(lines)
    inspected = [0,0,0,0,0,0,0,0]
    for i in range(20):
        for monkey in range(len(monkey_items)):
            for item in monkey_items[monkey]:
                inspected[monkey] += 1
                new_value = execute_operation(monkey_operation[monkey], item)
                new_value = new_value // 3
                if new_value % divisible_by[monkey] == 0:
                    monkey_to_place = true_monkey[monkey]
                else:
                    monkey_to_place = false_monkey[monkey]
                monkey_items[monkey_to_place].append(new_value)
            monkey_items[monkey] = []
    ordered = sorted(inspected)
    return ordered[-1] * ordered[-2]


def solve_part2():
    lines = retrieve_input()
    monkey_items, divisible_by, monkey_operation, true_monkey, false_monkey = initialize_monkeys(lines)
    inspected = [0, 0, 0, 0, 0, 0, 0, 0]
    total_modulo = 1
    for x in divisible_by:
        total_modulo *= x
    for i in range(10000):
        for monkey in range(len(monkey_items)):
            for item in monkey_items[monkey]:
                inspected[monkey] += 1
                new_value = execute_operation(monkey_operation[monkey], item)
                if new_value % divisible_by[monkey] == 0:
                    monkey_to_place = true_monkey[monkey]
                else:
                    monkey_to_place = false_monkey[monkey]
                monkey_items[monkey_to_place].append(new_value % total_modulo)
            monkey_items[monkey] = []
    ordered = sorted(inspected)
    return ordered[-1] * ordered[-2]


if __name__ == "__main__":
    print(solve_part1())  # 151312
    print(solve_part2())  # 51382025916
