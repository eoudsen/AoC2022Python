from itertools import islice


def retrieve_input():
    return [x.strip() for x in open('input.txt')]


def rolling_window(input_list, window_size):
    for i in range(len(input_list) - window_size + 1):
        yield input_list[i: i + window_size]


def solve_part1():
    line = retrieve_input()[0]
    return [len(set(x)) for x in rolling_window(list(line), 4)].index(4) + 4


def solve_part2():
    line = retrieve_input()[0]
    return [len(set(x)) for x in rolling_window(list(line), 14)].index(14) + 14


if __name__ == "__main__":
    print(solve_part1())  # 1816
    print(solve_part2())  # 2625
