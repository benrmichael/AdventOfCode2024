import os
from collections import defaultdict

with open(os.path.join(os.getcwd(), 'resources', 'day8.txt')) as file:
    lines = [line for line in file if not line.isspace()]

antennas = defaultdict(set)
for i, row in enumerate(lines):
    for j, char in enumerate(row):
        if char != '.':
            antennas[char].add((i, j))

# Get the distance between two coordinates in a cartesian coordinate system
def cartesian_distance(p1: tuple[int, int], p2: tuple[int, int]):
    return p1[0] - p2[0], p1[1] - p2[1]

def puzzle_one() -> int:
    """
    test input, should find 14 anti-nodes:
    ............
    ........0...
    .....0......
    .......0....
    ....0.......
    ......A.....
    ............
    ............
    ........A...
    .........A..
    ............
    ............

    antennas = map of all unique locations each antenna type occurs at
    locations = set of unique locations that an anti-node exists at
    for each antenna in antennas
        for each location in antenna
            create two anti-nodes, where the anti-node is placed along the line connecting the antenna pair and is at
            least as far away as the distance between the pair (excluding locations off the map, including locations
            that might cover an existing antenna)
    return len(locations)
    """
    return 0

def puzzle_two() -> int:
    return 0


print(f"puzzle one solution = {puzzle_one()}")
print(f"puzzle two solution = {puzzle_two()}")