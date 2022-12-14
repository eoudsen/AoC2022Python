from collections import deque


def retrieve_input():
    return [list(x) for x in open('input.txt').read().split("\n")]


def parse_grid():
    grid = retrieve_input()
    a_list = []
    start = end = None
    for i, row in enumerate(grid):
        for j, v in enumerate(row):
            if v == "S":
                start = (i, j)
                a_list.append((i, j))
                grid[i][j] = "a"
            elif v == "E":
                end = (i, j)
                grid[i][j] = "z"
            elif v == "a":  # add a's to a list to loop over
                a_list.append((i, j))
    return grid, start, end, a_list


def bfs(grid, start, end):
    q = deque()
    q.append((start, 0))
    seen = set()
    while q:
        pos, dist = q.popleft()
        if pos == end:
            return dist
        if pos in seen:
            continue
        seen.add(pos)
        x, y = pos
        for dx, dy in ((0, 1), (1, 0), (0, -1), (-1, 0)):
            if (
                0 <= x + dx < len(grid)
                and 0 <= y + dy < len(grid[0])
                and ord(grid[x + dx][y + dy]) - ord(grid[x][y]) <= 1
            ):
                q.append(((x + dx, y + dy), dist + 1))
    return float("inf")


def solve_part1():
    grid, start, end, a_list = parse_grid()
    return bfs(grid, start, end)


def solve_part2():
    grid, start, end, a_list = parse_grid()
    a_distances = [bfs(grid, a, end) for a in a_list]
    return min(a_distances)


if __name__ == "__main__":
    print(solve_part1())  # 462
    print(solve_part2())  # 451
