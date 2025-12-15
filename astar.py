def get(graph, a, b=None):
    links = graph.setdefault(a, {})
    if b is None:
        return links
    else:
        return links[b]


class Node:
    def __init__(self, name: str, parent):
        self.name = name
        self.parent = parent
        self.g = 0
        self.h = 0
        self.f = 0

    def __eq__(self, other):
        return self.name == other.name

    def __lt__(self, other):
        return self.f < other.f

    def __repr__(self):
        return f"({self.name},{self.f})"


def add_to_open(open_list, neighbor):
    for node in open_list:
        if neighbor == node and neighbor.f >= node.f:
            return False
    return True


def astar_search(graph, heuristics, start, end):
    open_list = []
    closed_list = []

    start_node = Node(start, None)
    goal_node = Node(end, None)

    open_list.append(start_node)
    print("Initial open list:", open_list)
    while open_list:
        open_list.sort()
        current_node = open_list.pop(0)
        closed_list.append(current_node)

        if current_node == goal_node:
            path = []
            while current_node:
                path.append(current_node.name + ": " + str(current_node.g))
                current_node = current_node.parent
            return path[::-1]

        neighbors = graph.get(current_node.name, {})
        for key, value in neighbors.items():
            neighbor = Node(key, current_node)

            if neighbor in closed_list:
                continue

            neighbor.g = current_node.g + value
            neighbor.h = heuristics[neighbor.name]
            neighbor.f = neighbor.g + neighbor.h

            if add_to_open(open_list, neighbor):
                open_list.append(neighbor)

    return None


# Graph and Heuristic
g = {
    'a': {'b': 4, 'c': 3},
    'b': {'f': 5, 'e': 12},
    'c': {'e': 10, 'd': 7},
    'd': {'e': 2},
    'e': {'z': 5},
    'f': {'z': 16},
    'z': {}
}

h = {
    'a': 14,
    'b': 12,
    'c': 11,
    'd': 6,
    'e': 4,
    'f': 11,
    'z': 0
}

path = astar_search(g, h, 'a', 'z')
print(path)
