import random
from typing import Dict, List, Tuple
import math
from PIL import Image


def choose_start_and_end_loc(image: Image) -> Tuple[Tuple[int, int], Tuple[int, int]]:
    """
    Randomly chooses start, end locations in the top left and
    bottom right portions of the image avoiding obstacles.
    """
    grid_size = image.size[0]
    limit = int(10 * grid_size / 100)

    # Filter out feasible start locations in the NorthWest
    feasible_starts = []
    for i in range(limit):  # x
        for j in range(limit):  # y
            if image.getpixel((i, j)) == (0, 0, 0):
                continue
            feasible_starts.append((i, j))

    # Filter out feasible end locations in the SouthEast
    feasible_ends = []
    for i in range(grid_size - limit, grid_size):  # x
        for j in range(grid_size - limit, grid_size):  # y
            if image.getpixel((i, j)) == (0, 0, 0):
                continue
            feasible_ends.append((i, j))

    return random.choice(feasible_starts), random.choice(feasible_ends)


def create_adjacency_dict(image: Image) -> Dict:
    """
    Creates adjacency dict as a representation of graph from the image
    """
    adjacency = {}
    grid_size = image.size[0]
    for i in range(grid_size):  # y
        for j in range(grid_size):  # x
            adjacency[(i, j)] = get_valid_node_neighbours((i, j), grid_size, image)

    return adjacency


def create_adjacency_dict_for_weighted_graphs(image: Image) -> Dict:
    """
    Creates adjacency list as a representation of graph from the image
    """
    adjacency = {}
    grid_size = image.size[0]
    for i in range(grid_size):  # y
        for j in range(grid_size):  # x
            adjacency[(i, j)] = get_valid_node_neighbours_with_weights(
                (i, j), grid_size, image
            )

    return adjacency


def get_valid_node_neighbours(current: Tuple, grid_size: int, image: Image) -> List:
    """
    Gets the valid traversable neighbours of a particular node.
    Invalid neighbours include out of bound coordinates(tuples) or coordinates
    that house obstacles.
    """
    if image.getpixel(current) == (0, 0, 0):
        return []  # Exit early if the node in question is part of an obstacle

    x, y = current[0], current[1]
    valid_neighbours = []

    for neighbour in [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]:
        if not (
            0 <= neighbour[0] <= grid_size - 1 and 0 <= neighbour[1] <= grid_size - 1
        ):
            continue
        if image.getpixel(neighbour) == (0, 0, 0):
            continue
        valid_neighbours.append(neighbour)
    return valid_neighbours


def get_valid_node_neighbours_with_weights(
    current: Tuple, grid_size: int, image: Image
) -> Dict:
    """
    Gets the valid traversable neighbours of a particular node. These include
    the diagonal ones too. Invalid neighbours include out of bound coordinates
    or coordinates that house obstacles. The neighbours are returned as a
    dictionary where the keys denote the nodes and the values, the distance from
    the current node.
    """
    if image.getpixel(current) == (0, 0, 0):
        return {}  # Exit early if the node in question is part of an obstacle

    x, y = current[0], current[1]
    valid_neighbours = {}

    for neighbour in [
        (x - 1, y),
        (x + 1, y),
        (x, y - 1),
        (x, y + 1),
        (x - 1, y - 1),
        (x - 1, y + 1),
        (x + 1, y - 1),
        (x + 1, y + 1),
    ]:
        if not (
            0 <= neighbour[0] <= grid_size - 1 and 0 <= neighbour[1] <= grid_size - 1
        ):
            continue
        if image.getpixel(neighbour) == (0, 0, 0):
            continue
        valid_neighbours[neighbour] = math.dist(current, neighbour)
    return valid_neighbours


def get_unvisited_children(node: Tuple, graph: Dict, visited: Dict) -> List:
    """
    Gets the unvisited children of a particular node
    """
    unvisited_children = []
    for child_node in graph.get(node, []):
        if visited[child_node]:
            continue
        unvisited_children.append(child_node)
    return unvisited_children
