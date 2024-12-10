import os
from collections import defaultdict

with open(os.path.join(os.getcwd(), 'resources', 'day8.txt')) as file:
    lines = [line.strip() for line in file if not line.isspace()]

antennas = defaultdict(list)
for i, row in enumerate(lines):
    for j, char in enumerate(row):
        if char != '.':
            antennas[char].append((i, j))

dim = (len(lines), len(lines[0]))

def add_tuples(tup1, tup2):
    return tuple(map(sum, zip(tup1, tup2)))

def cartesian_distance(p1, p2):
    return p1[0] - p2[0], p1[1] - p2[1]

def in_bounds(point):
    return 0 <= point[0] < dim[0] and 0 <= point[1] < dim[1]

def generate_antinodes(p1: tuple[int, int], p2: tuple[int, int]):
     antinodes = [add_tuples(p1, cartesian_distance(p1, p2)), add_tuples(p2, cartesian_distance(p2, p1))]
     return [p for p in antinodes if in_bounds(p)]

def puzzle_one() -> int:
    locations = set()
    for antenna, nodes in antennas.items():
        for index in range(len(nodes)):
            for node in nodes[index + 1:]:
                antinodes = generate_antinodes(nodes[index], node)
                locations.update(antinodes)

    return len(locations)

def puzzle_two() -> int:
    return 0


print(f"puzzle one solution = {puzzle_one()}")
print(f"puzzle two solution = {puzzle_two()}")