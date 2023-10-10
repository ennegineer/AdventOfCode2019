# Untangle the two wires by finding the intersection point closest to the central port.

# Wire paths are described in U D L R (up, down, left, right) and a number of spaces traveled.
# Find all the places where the wires cross, i.e. pass the same coordinates
# Identify the distance of the crossing point closest to the central port (x + y distances = answer)

# Import the data
with open("input.txt", "r") as input:
    data = input.read().split('\n')

# The directions for the path of the two wires are in a list, data. data[0] is the path of the first wire, data[1] is the second wire.
wire1_directions = data[0].split(',')
wire2_directions = data[1].split(',')

# Start at 0,0 as the central port
wire1_path = [[0,0]]
wire2_path = [[0,0]]

# Pass the directions into a function to determine the paths
def find_path(directions, path):
    current_position = [0,0]
    for i in directions:
        direction = i[0]
        distance = int(i[1:])

        # if starts with L: current_position[0] + number / append to wire path list
        if direction == 'L':
            while distance > 0:
                current_position[0] -= 1
                path.append(current_position.copy())
                distance -= 1
                if distance <= 0:
                    break
        # if starts with R: current_position[0] - number
        elif direction == 'R':
            while distance > 0:
                current_position[0] += 1
                path.append(current_position.copy())
                distance -= 1
                if distance <= 0:
                    break
        # if starts with U: current_position[1] + number
        elif direction == 'U':
            while distance > 0:
                current_position[1] += 1
                path.append(current_position.copy())
                distance -= 1
                if distance <= 0:
                    break
        # if starts with D: current_position[1] - number
        elif direction == 'D':
            while distance > 0:
                current_position[1] -= 1
                path.append(current_position.copy())
                distance -= 1
                if distance <= 0:
                    break
    return path

find_path(wire1_directions, wire1_path)
find_path(wire2_directions, wire2_path)
    
# To find the intersections, look for set of coordinates that match between both wire paths
wire1_set = set(map(tuple, wire1_path))
wire2_set = set(map(tuple, wire2_path))

intersections = wire1_set.intersection(wire2_set)

# Remove the central port
intersections.remove((0,0))

# x + y = distance from central port. find the shortest distance.
closest_intersection = []
for item in intersections:
    closest_intersection.append([abs(item[0]) + abs(item[1])])

print(min(closest_intersection))

# For part two, we want to instead find the intersection where the sum of both wires' steps is lowest.

# First, get the format of the list of intersections (0,0) to match the wire path lists [0,0]
intersections_conversion = list(intersections)
intersections_list = []
for coord in list(intersections_conversion):
    intersections_list.append([coord[0], coord[1]])


def find_distances():
    dist = []
    for coordpair in intersections_list:

        for i, item in enumerate(wire1_path):
            if item == coordpair:
                points_1 = i
                break
        for i, item in enumerate(wire2_path):
            if item == coordpair:
                points_2 = i
                break
        new_dist = int(points_1)+int(points_2)
        dist.append(new_dist)
    print(min(dist))

find_distances()
# 101956 is correct!