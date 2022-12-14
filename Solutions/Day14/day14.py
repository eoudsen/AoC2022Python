def retrieve_input():
    return [x.strip() for x in open('input.txt')]


def solve_part1():
    lines = retrieve_input()
    rock_locations = set()
    lowest_point = 0
    for line in lines:
        lines_to_draw = line.split("->")
        x = None
        y = None
        for line_to_draw in lines_to_draw:
            if x is None:
                x, y = line_to_draw.strip().split(",")
                if int(y) > lowest_point:
                    lowest_point = int(y)
                continue
            x2, y2 = line_to_draw.strip().split(",")
            if int(y2) > lowest_point:
                lowest_point = int(y2)
            if int(x) == int(x2):
                if int(y) < int(y2):
                    for i in range(int(y), int(y2) + 1):
                        rock_locations.add((int(x), i))
                else:
                    for i in range(int(y2), int(y) + 1):
                        rock_locations.add((int(x), i))
            elif int(y) == int(y2):
                if int(x) < int(x2):
                    for i in range(int(x), int(x2) +1):
                        rock_locations.add((i, int(y)))
                else:
                    for i in range(int(x2), int(x) + 1):
                        rock_locations.add((i, int(y)))
            x = int(x2)
            y = int(y2)

    current_position = (500, 0)
    settled = 0
    while True:
        if current_position[1] > lowest_point:
            return settled
        if not rock_locations.__contains__((current_position[0], current_position[1] + 1)):
            current_position = (current_position[0], current_position[1] + 1)
        elif not rock_locations.__contains__((current_position[0] - 1, current_position[1] + 1)):
            current_position = (current_position[0] - 1, current_position[1] + 1)
        elif not rock_locations.__contains__((current_position[0] + 1, current_position[1] + 1)):
            current_position = (current_position[0] + 1, current_position[1] + 1)
        else:
            settled += 1
            rock_locations.add(current_position)
            current_position = (500, 0)


def solve_part2():
    lines = retrieve_input()
    rock_locations = set()
    lowest_point = 0
    for line in lines:
        lines_to_draw = line.split("->")
        x = None
        y = None
        for line_to_draw in lines_to_draw:
            if x is None:
                x, y = line_to_draw.strip().split(",")
                if int(y) > lowest_point:
                    lowest_point = int(y)
                continue
            x2, y2 = line_to_draw.strip().split(",")
            if int(y2) > lowest_point:
                lowest_point = int(y2)
            if int(x) == int(x2):
                if int(y) < int(y2):
                    for i in range(int(y), int(y2) + 1):
                        rock_locations.add((int(x), i))
                else:
                    for i in range(int(y2), int(y) + 1):
                        rock_locations.add((int(x), i))
            elif int(y) == int(y2):
                if int(x) < int(x2):
                    for i in range(int(x), int(x2) + 1):
                        rock_locations.add((i, int(y)))
                else:
                    for i in range(int(x2), int(x) + 1):
                        rock_locations.add((i, int(y)))
            x = int(x2)
            y = int(y2)

    lowest_point = lowest_point + 2
    for i in range(-500, 1500):
        rock_locations.add((i, lowest_point))

    current_position = (500, 0)
    settled = 0
    while True:
        if not rock_locations.__contains__((current_position[0], current_position[1] + 1)):
            current_position = (current_position[0], current_position[1] + 1)
        elif not rock_locations.__contains__((current_position[0] - 1, current_position[1] + 1)):
            current_position = (current_position[0] - 1, current_position[1] + 1)
        elif not rock_locations.__contains__((current_position[0] + 1, current_position[1] + 1)):
            current_position = (current_position[0] + 1, current_position[1] + 1)
        else:
            settled += 1
            if current_position[0] == 500 and current_position[1] == 0:
                return settled
            rock_locations.add(current_position)
            current_position = (500, 0)


if __name__ == "__main__":
    print(solve_part1())  # 892
    print(solve_part2())  # 27155
