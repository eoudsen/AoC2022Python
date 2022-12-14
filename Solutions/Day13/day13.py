from functools import cmp_to_key


def retrieve_input():
    return [x.strip() for x in open('input.txt')]


def is_in_order(left, right):
    max_len = max(len(left), len(right))
    for index in range(max_len):
        if index == len(left) and index < len(right):
            return True
        if index < len(left) and index == len(right):
            return False

        left_value = left[index]
        right_value = right[index]
        if isinstance(left_value, int) and isinstance(right_value, int):
            if left_value < right_value:
                return True
            if left_value > right_value:
                return False
        elif isinstance(left_value, list) and isinstance(right_value, list):
            result = is_in_order(left_value, right_value)
            if result is not None:
                return result
        elif isinstance(left_value, int) and isinstance(right_value, list):
            result = is_in_order([left_value], right_value)
            if result is not None:
                return result
        elif isinstance(left_value, list) and isinstance(right_value, int):
            result = is_in_order(left_value, [right_value])
            if result is not None:
                return result


def solve_part1():
    lines = retrieve_input()
    left = None
    right = None
    pair_number = 1
    ordered = 0
    for line in lines:
        if left is None:
            left = eval(line)
            continue
        elif right is None:
            right = eval(line)
            continue

        if is_in_order(left, right):
            ordered += pair_number
        pair_number += 1
        left = None
        right = None
    return ordered


def solve_part2():
    lines = [line.strip() for line in open("input.txt").read().replace('\n\n', '\n').split('\n')]
    lines.append('[[2]]')
    lines.append('[[6]]')
    packets = [eval(line) for line in lines]
    sorted_packets = sorted(packets, key=cmp_to_key(lambda a, b: -1 if is_in_order(a, b) else 1))
    return (sorted_packets.index([[2]]) + 1) * (sorted_packets.index([[6]]) + 1)


if __name__ == "__main__":
    print(solve_part1())  # 5659
    print(solve_part2())  # 22110
