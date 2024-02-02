import convert
from collections import deque
import numpy as np
import find_neighbours

start = ("123485760", (2, 2))
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


def solve(start):
    # node : [distance to start, is dealt, previous node]
    nodes = {start: [0, False, None], solution: [np.inf, False, None]}
    queue = deque([start])

    while not nodes[solution][1]:
        actual_node = queue.popleft()
        if not nodes[actual_node][1]:  # if not dealt
            neighbours = find_neighbours.neighbours(actual_node[0], actual_node[1])
            for neighbour in neighbours:
                if not neighbour in nodes:
                    nodes[neighbour] = (nodes[actual_node][0] + 1, False, actual_node)
                    queue.append(neighbour)
                if nodes[neighbour][0] > nodes[actual_node][0] + 1:
                    nodes[neighbour][0] = nodes[actual_node][0] + 1
            nodes[actual_node][1] = True  # dealt node

    # Find path
    node = solution
    path = [node[0]]
    while node[0] != start[0]:
        node = nodes[node][2]
        path = [node[0]] + path
    return path


def display(path):
    for board in path:
        print(board[0:3])
        print(board[3:6])
        print(board[6:9])
        print("####")


path = solve(start)
display(path)
