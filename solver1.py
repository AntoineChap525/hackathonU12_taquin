from collections import deque
import numpy as np
import find_neighbours

start = ("087654321", (0, 0))
solution = ("123456780", (2, 2))
chgt = 0

def solve(start, solution):
    global chgt
    # node : [distance to start, is dealt, previous node]
    nodes = {start: [0, False, None], solution: [np.inf, False, None]}
    queue = deque([start])

    while not nodes[solution][1]:
        actual_node = queue.popleft()
        if not nodes[actual_node][1]:  # if not dealt
            chgt +=1
            neighbours = find_neighbours.neighbours(actual_node[0], actual_node[1])
            for neighbour in neighbours:
                if (not neighbour in nodes) or neighbour[0] == solution[0]:
                    nodes[neighbour] = [nodes[actual_node][0] + 1, False, actual_node]
                    queue.append(neighbour)
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


