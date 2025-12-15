import heapq

GOAL_STATE = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 0]
]

MOVES = [(-1,0), (1,0), (0,-1), (0,1)]  # Up, Down, Left, Right

def find_zero(state):
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                return i, j

def is_goal(state):
    return state == GOAL_STATE

# Manhattan distance heuristic
def manhattan(state):
    distance = 0
    for i in range(3):
        for j in range(3):
            val = state[i][j]
            if val != 0:
                goal_x = (val - 1) // 3
                goal_y = (val - 1) % 3
                distance += abs(i - goal_x) + abs(j - goal_y)
    return distance

def neighbors(state):
    x, y = find_zero(state)
    result = []

    for dx, dy in MOVES:
        nx, ny = x + dx, y + dy
        if 0 <= nx < 3 and 0 <= ny < 3:
            new_state = [row[:] for row in state]
            new_state[x][y], new_state[nx][ny] = new_state[nx][ny], new_state[x][y]
            result.append(new_state)

    return result

def serialize(state):
    return tuple(tuple(row) for row in state)

def a_star(start):
    heap = []
    heapq.heappush(heap, (manhattan(start), 0, start, []))
    visited = set()

    while heap:
        est, cost, state, path = heapq.heappop(heap)

        if is_goal(state):
            return path + [state]

        key = serialize(state)
        if key in visited:
            continue

        visited.add(key)

        for next_state in neighbors(state):
            heapq.heappush(
                heap,
                (cost + 1 + manhattan(next_state),
                 cost + 1,
                 next_state,
                 path + [state])
            )

    return None

def print_path(path):
    for step in path:
        for row in step:
            print(row)
        print()

if __name__ == "__main__":
    start_state = [
        [1, 2, 3],
        [4, 0, 6],
        [7, 5, 8]
    ]

    solution = a_star(start_state)

    if solution:
        print("Solution found in", len(solution) - 1, "moves:\n")
        print_path(solution)
    else:
        print("No solution found.")
