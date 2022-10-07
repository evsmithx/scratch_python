"""
symmetries are good...
room is a rectangle, unfold the reflections
"""
import math


def get_reflections(x_range, y_range, dimensions, position):
    positions = []
    for i in range(-x_range, x_range + 1):
        if i % 2 == 0:
            x = i * dimensions[0] + position[0]
        else:
            x = (i + 1) * dimensions[0] - position[0]
        for j in range(-y_range, y_range + 1):
            if i == j == 0:  # this is not a reflection
                continue
            if j % 2 == 0:
                y = j * dimensions[1] + position[1]
            else:
                y = (j + 1) * dimensions[1] - position[1]
            positions.append([x, y])
    return positions


def get_corner_reflections(x_range, y_range, dimensions):
    positions = []
    for i in range(-x_range, x_range + 1):
        x = i * dimensions[0]
        for j in range(-y_range, y_range + 1):
            y = j * dimensions[1]
            positions.append([x, y])
    return positions


def solution(dimensions, your_position, trainer_position, distance):
    # make multiple tiled reflections
    x_tile_range = distance // dimensions[0] + 1
    y_tile_range = distance // dimensions[1] + 1

    trainer_positions = get_reflections(x_tile_range, y_tile_range, dimensions, trainer_position)
    trainer_positions.append(trainer_position)
    your_positions = get_reflections(x_tile_range, y_tile_range, dimensions, your_position)
    corner_positions = get_corner_reflections(x_tile_range, y_tile_range, dimensions)

    good_angles = {}
    for tp in trainer_positions:
        angle = [tp[0] - your_position[0], tp[1] - your_position[1]]
        t_dist = math.sqrt(angle[0] ** 2 + angle[1] ** 2)
        angle_deg = math.atan2(angle[1], angle[0]) * 180 / math.pi
        if t_dist <= distance:
            if angle_deg not in good_angles:
                good_angles[angle_deg] = t_dist
            else:
                good_angles[angle_deg] = min(good_angles[angle_deg], t_dist)

    # remove angles where you would be hit first
    for tp in your_positions:
        angle = [tp[0] - your_position[0], tp[1] - your_position[1]]
        t_dist = math.sqrt(angle[0] ** 2 + angle[1] ** 2)
        angle_deg = math.atan2(angle[1], angle[0]) * 180 / math.pi
        if angle_deg in good_angles and good_angles[angle_deg] > t_dist:
            good_angles.pop(angle_deg)

    # remove corners in the same way
    for corner in corner_positions:
        angle = [corner[0] - your_position[0], corner[1] - your_position[1]]
        t_dist = math.sqrt(angle[0] ** 2 + angle[1] ** 2)
        angle_deg = math.atan2(angle[1], angle[0]) * 180 / math.pi
        if t_dist * 2 <= distance:  # corners are only a problem if they are d/2 away
            if angle_deg in good_angles and good_angles[angle_deg] > t_dist:
                good_angles.pop(angle_deg)

    return len(good_angles)


print(solution([3, 2], [1, 1], [2, 1], 4), 7)
print(solution([300, 275], [150, 150], [185, 100], 500), 9)
