def retrieve_input():
    return [x.strip() for x in open('input.txt')]


def check_strength(cycle):
    if (cycle == 20 or (cycle - 20) % 40 == 0) and cycle < 221:
        return True
    return False


def solve_part1():
    operations = retrieve_input()
    signal_strengths = []
    cycle = 0
    x_value = 1
    for op in operations:
        cycle += 1
        if op == "noop":
            print()
        if op.startswith("addx"):
            value_to_add = op.split(" ")[1]
            to_save = check_strength(cycle)
            if to_save:
                signal_strengths.append(x_value * cycle)
            cycle += 1
            to_save = check_strength(cycle)
            if to_save:
                signal_strengths.append(x_value * cycle)
            x_value += int(value_to_add)
            continue
        to_save = check_strength(cycle)
        if to_save:
            signal_strengths.append(x_value * cycle)
    return sum(signal_strengths)


def draw(cycle, x_value):
    cycle = cycle - 1
    if cycle % 40 == 0:
        print("", end="\n")
    if cycle >= 40:
        cycle = cycle % 40
    if x_value - 1 <= cycle <= x_value + 1:
        print("#", end="")
    else:
        print(".", end="")


def solve_part2():
    operations = retrieve_input()
    cycle = 0
    x_value = 1
    for op in operations:
        cycle += 1
        if op == "noop":
            draw(cycle, x_value)
        if op.startswith("addx"):
            value_to_add = op.split(" ")[1]
            draw(cycle, x_value)
            cycle += 1
            draw(cycle, x_value)
            x_value += int(value_to_add)
            continue


if __name__ == "__main__":
    print(solve_part1())  # 15360
    print(solve_part2())  # PHLHJGZA
