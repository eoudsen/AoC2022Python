stacks = []


def retrieve_input():
    return [x.rstrip('\n') for x in open('input.txt')]


def parse_input(line):
    line_in_list = list(line)
    if not line_in_list.__contains__('['):
        return False
    max_num_of_blocks_to_add = len(line_in_list) // 4 + 1
    for i in range(max_num_of_blocks_to_add):
        value = line_in_list[i * 4 + 1]
        if value != ' ':
            while len(stacks) - 1 < i:
                stacks.append([])
            stacks[i].append(value)
    return True


def get_result():
    result_string = ""
    for stack in stacks:
        result_string += stack.pop()
    return result_string


def solve_part1():
    lines = retrieve_input()
    parsing_input = True
    for line in lines:
        if len(line) == 0:
            for stack in stacks:
                stack.reverse()
            continue
        if parsing_input:
            parsing_input = parse_input(line)
            continue
        num_to_move = int(line.split(" ")[1])
        move_from = int(line.split(" ")[3])
        move_to = int(line.split(" ")[5])
        for i in range(num_to_move):
            value = stacks[move_from - 1].pop()
            stacks[move_to - 1].append(value)
    return get_result()


def solve_part2():
    lines = retrieve_input()
    parsing_input = True
    for line in lines:
        if len(line) == 0:
            for stack in stacks:
                stack.reverse()
            continue
        if parsing_input:
            parsing_input = parse_input(line)
            continue
        num_to_move = int(line.split(" ")[1])
        move_from = int(line.split(" ")[3])
        move_to = int(line.split(" ")[5])
        temp_list = []
        for i in range(num_to_move):
            temp_list.append(stacks[move_from - 1].pop())
        for i in range(len(temp_list)):
            stacks[move_to - 1].append(temp_list.pop())
    return get_result()


if __name__ == "__main__":
    print(solve_part1())  # HBTMTBSDC
    stacks = []
    print(solve_part2())  # PQTJRSHWS
