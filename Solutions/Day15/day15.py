import re
from itertools import tee


def retrieve_input():
    return [x.strip() for x in open('input.txt')]


def pairwise(iterable):
    a, b = tee(iterable)
    next(b, None)
    yield from zip(a, b)


def manhattan_distance(sensor_x, sensor_y, beacon_x, beacon_y):
    return abs(sensor_x - beacon_x) + abs(sensor_y - beacon_y)


def solve_part1():
    lines = retrieve_input()
    non_beacon_positions = set()
    sensor_ranges = dict()
    for i, line in enumerate(lines):
        sensor_x, sensor_y, beacon_x, beacon_y = [int(x) for x in re.findall(r'-?\d+', line)]
        manhattan = manhattan_distance(sensor_x, sensor_y, beacon_x, beacon_y)
        sensor_ranges[(sensor_x, sensor_y)] = manhattan

        for x in range(sensor_x - manhattan, sensor_x + manhattan + 1):
            if x == beacon_x and beacon_y == 2000000:
                continue

            if manhattan_distance(sensor_x, sensor_y, x, 2000000) <= manhattan:
                non_beacon_positions.add((x, 2000000))

    return len(non_beacon_positions)


def solve_part2():
    lines = retrieve_input()
    sensor_distances = {}

    for line in lines:
        sensor_x, sensor_y, beacon_x, beacon_y = [int(x) for x in re.findall(r'-?\d+', line)]
        sensor_distances[(sensor_x, sensor_y)] = manhattan_distance(sensor_x, sensor_y, beacon_x, beacon_y)

    for y in range(0, 4000000 + 1):
        ranges = []
        for (sensor_x, sensor_y), sensor_manhattan_distance in sensor_distances.items():
            sensor_row_distance = abs(sensor_y - y)
            if sensor_manhattan_distance > sensor_row_distance:
                distance_x = sensor_manhattan_distance - sensor_row_distance
                ranges.append((max(0, sensor_x - distance_x), min(4000000 + 1, sensor_x + distance_x + 1)))

        ranges = sorted(ranges)
        beacon_x_location = 0

        for (_, high), (low, _) in pairwise(ranges):
            beacon_x_location = max(beacon_x_location, high)
            if beacon_x_location < low:
                return beacon_x_location * 4000000 + y


if __name__ == "__main__":
    print(solve_part1())  # 5176944
    print(solve_part2())  # 13350458933732
