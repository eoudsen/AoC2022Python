def retrieve_input():
    return [x.strip() for x in open('input.txt')]


def solve_part1():
    lines = retrieve_input()
    actual_grid = []
    for line in lines:
        actual_grid.append([int(x) for x in list(line)])
    count_grid = [[0] * len(actual_grid[0]) for _ in range(len(actual_grid))]
    for x in range(len(actual_grid)):
        for y in range(len(actual_grid[x])):
            current_value = actual_grid[x][y]
            index = 1
            visible = False
            while True:
                if y - index < 0:
                    visible = True
                    break
                if actual_grid[x][y - index] >= current_value:
                    break
                index += 1
            index = 1
            while True:
                if y + index > len(actual_grid[x]) - 1:
                    visible = True
                    break
                if actual_grid[x][y + index] >= current_value:
                    break
                index += 1
            index = 1
            while True:
                if x - index < 0:
                    visible = True
                    break
                if actual_grid[x - index][y] >= current_value:
                    break
                index += 1
            index = 1
            while True:
                if x + index > len(actual_grid) - 1:
                    visible = True
                    break
                if actual_grid[x + index][y] >= current_value:
                    break
                index += 1
            if visible:
                count_grid[x][y] = 1
    return sum(sum(count_grid, []))


def solve_part2():
    lines = retrieve_input()
    actual_grid = []
    for line in lines:
        actual_grid.append([int(x) for x in list(line)])
    count_grid = [[1] * len(actual_grid[0]) for _ in range(len(actual_grid))]
    for x in range(len(actual_grid)):
        for y in range(len(actual_grid[x])):
            if x == 0 or y == 0 or x == len(actual_grid) - 1 or y == len(actual_grid[x]) - 1:
                continue
            current_value = actual_grid[x][y]
            index = 1
            while True:
                if y - index <= 0:
                    count_grid[x][y] *= index
                    break
                if actual_grid[x][y - index] >= current_value:
                    count_grid[x][y] *= index
                    break
                index += 1
            index = 1
            while True:
                if y + index >= len(actual_grid[x]) - 1:
                    count_grid[x][y] *= index
                    break
                if actual_grid[x][y + index] >= current_value:
                    count_grid[x][y] *= index
                    break
                index += 1
            index = 1
            while True:
                if x - index <= 0:
                    count_grid[x][y] *= index
                    break
                if actual_grid[x - index][y] >= current_value:
                    count_grid[x][y] *= index
                    break
                index += 1
            index = 1
            while True:
                if x + index >= len(actual_grid) - 1:
                    count_grid[x][y] *= index
                    break
                if actual_grid[x + index][y] >= current_value:
                    count_grid[x][y] *= index
                    break
                index += 1
    return max(map(max, count_grid))


if __name__ == "__main__":
    print(solve_part1())  # 1763
    print(solve_part2())  # 671160
