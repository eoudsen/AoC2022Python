def retrieve_input():
    return [x.strip() for x in open('input.txt')]


def move_head(direction, head):
    if direction == "U":
        return head[0] + 1, head[1]
    elif direction == "D":
        return head[0] - 1, head[1]
    elif direction == "L":
        return head[0], head[1] -1
    elif direction == "R":
        return head[0], head[1] + 1
    return head


def update_tail(head, tail):
    # x is equal
    if head[0] == tail[0]:
        if head[1] == tail[1] + 2:
            return tail[0], tail[1] + 1
        if head[1] == tail[1] - 2:
            return tail[0], tail[1] - 1
    # y is equal
    if head[1] == tail[1]:
        if head[0] == tail[0] + 2:
            return tail[0] + 1, tail[1]
        if head[0] == tail[0] - 2:
            return tail[0] - 1, tail[1]
    # head is higher
    if head[0] > tail[0]:
        # head is further to the right
        if head[1] > tail[1]:
            # tail is still connected
            if head[0] == tail[0] + 1 and head[1] == tail[1] + 1:
                return tail
            return tail[0] + 1, tail[1] + 1
        # head is further to the left
        if head[1] < tail[1]:
            if head[0] == tail[0] + 1 and head[1] == tail[1] - 1:
                return tail
            return tail[0] + 1, tail[1] - 1
    # head is lower
    if head[0] < tail[0]:
        # head is further to the right
        if head[1] > tail[1]:
            if head[0] == tail[0] - 1 and head[1] == tail[1] + 1:
                return tail
            return tail[0] - 1, tail[1] + 1
        if head[1] < tail[1]:
            if head[0] == tail[0] - 1 and head[1] == tail[1] - 1:
                return tail
            return tail[0] - 1, tail[1] - 1
    return tail


def solve_part1():
    lines = retrieve_input()
    visited_tail_positions = set()
    head_position = (0, 0)
    tail_position = (0, 0)
    for line in lines:
        direction = line.split(" ")[0]
        number_of_steps = int(line.split(" ")[1])
        for i in range(number_of_steps):
            visited_tail_positions.add(tail_position)
            head_position = move_head(direction, head_position)
            tail_position = update_tail(head_position, tail_position)
    visited_tail_positions.add(tail_position)
    return len(visited_tail_positions)




def solve_part2():
    lines = retrieve_input()
    visited_tail_positions = set()
    rope_positions = [(0,0), (0,0), (0,0), (0,0), (0,0), (0,0), (0,0), (0,0), (0,0), (0,0)]
    for line in lines:
        direction = line.split(" ")[0]
        number_of_steps = int(line.split(" ")[1])
        for i in range(number_of_steps):
            visited_tail_positions.add(rope_positions[-1])
            rope_positions[0] = move_head(direction, rope_positions[0])
            index = 1
            while index < len(rope_positions):
                rope_positions[index] = update_tail(rope_positions[index - 1], rope_positions[index])
                index += 1
    visited_tail_positions.add(rope_positions[-1])
    return len(visited_tail_positions)


if __name__ == "__main__":
    print(solve_part1())  # 5902
    print(solve_part2())  # 2445
