import convert
from collections import deque
import numpy as np
import find_neighbours

start = ("087654321", (0, 0))
solution = ("123456780", (2, 2))


def manhattan_cost(taquin: str, solution: str):
    taquin = convert.from_str_to_tab(taquin)
    solution = convert.from_str_to_tab(solution)

    position_solution = {}
    n = len(solution)
    for i in range(n):
        for j in range(n):
            position_solution[solution[i][j]] = (i, j)

    distance = 0
    for i in range(n):
        for j in range(n):
            correct_position = position_solution[taquin[i][j]]
            distance += abs(i - correct_position[0]) + abs(j - correct_position[1])

    return distance


def solve(start, solution):
    # node : [total distance (D+M), distance to start, is dealt, previous node]
    nodes = {
        start: [manhattan_cost(start[0], solution[0]), 0, False, None],
        solution: [np.inf, np.inf, False, None],
    }

    actual_node = start

    while not nodes[solution][2]:
        if not nodes[actual_node][2]:  # if not dealt
            neighbours = find_neighbours.neighbours(actual_node[0], actual_node[1])
            for neighbour in neighbours:
                distance_to_start = nodes[actual_node][1] + 1
                total_distance = distance_to_start + manhattan_cost(
                    neighbour[0], solution[0]
                )
                if not neighbour in nodes:
                    nodes[neighbour] = [
                        total_distance,
                        distance_to_start,
                        False,
                        actual_node,
                    ]
                if nodes[neighbour][0] > total_distance:
                    nodes[neighbour][0] = total_distance
                    nodes[neighbour][1] = distance_to_start
                    nodes[neighbour][3] = actual_node

            nodes[actual_node][2] = True  # dealt node

            # Search minimum distance (amoung non dealt nodes)
            min = np.inf
            for node in nodes:
                if (not nodes[node][2]) and (min > nodes[node][0]):
                    min, min_node = nodes[node][0], node

            actual_node = min_node

    # Find path
    node = solution
    path = [node[0]]
    while node[0] != start[0]:
        node = nodes[node][3]
        path = [node[0]] + path
    return path


def display(path):
    for board in path:
        print(board[0:3])
        print(board[3:6])
        print(board[6:9])
        print("####")


path = solve(start, solution)
display(path)
