import copy

import matplotlib.pyplot as plt

from graph_searches import dfs, bfs, dijkstra, random_planner
from hw0.obstacle_course import create_obstacle_grid
from utils import create_adjacency_list, choose_start_and_end_loc

powder_blue = (182, 208, 226)
cherry = (210, 4, 45)
forest_green = (34, 139, 34)
kelly_green = (76, 187, 23)


def generate_bfs_output(grid_size: int, coverage: int):
    # Create obstacle grid with desired size and coverage
    grid = create_obstacle_grid(grid_size, coverage)

    # Get graph representation from image
    graph = create_adjacency_list(grid)

    # Place path ends on graph
    start, end = choose_start_and_end_loc(grid)
    grid.putpixel(start, cherry)
    grid.putpixel(end, forest_green)
    plt.imshow(grid)

    nodes_with_stages, path, visited = bfs(graph, start, end)
    stage_for_end_node = nodes_with_stages.get(end)

    level_order = {}
    for k, v in nodes_with_stages.items():
        level_order[v] = level_order.get(v, []) + [k]
    level_order.pop(-1)

    stages_without_path_ends = copy.deepcopy(level_order)
    stages_without_path_ends.pop(0)
    stages_without_path_ends.pop(stage_for_end_node)

    # Traversal
    for key, value in stages_without_path_ends.items():
        for coord in value:
            grid.putpixel(coord, powder_blue)
            plt.imshow(grid)
        plt.pause(0.001)

    # Final path
    for node in path:
        grid.putpixel(node, kelly_green)

    plt.imshow(grid)
    plt.show()
    print("Iterations taken:", len(path))
    count = 0
    for node in visited.values():
        if not node:
            continue
        count += 1
    print("visited nodes:", count)


def generate_dfs_output(grid_size: int, coverage: int):
    # Create obstacle grid with desired size and coverage
    grid = create_obstacle_grid(grid_size, coverage)

    # Get graph representation from image
    graph = create_adjacency_list(grid)

    # Place path ends on graph
    start, end = choose_start_and_end_loc(grid)
    grid.putpixel(start, cherry)
    grid.putpixel(end, forest_green)
    plt.imshow(grid)

    path = dfs(graph, start, end)

    # Remove path ends so as not to overwrite the color in the graph
    path_without_ends = copy.deepcopy(path)
    path_without_ends.pop(0)
    path_without_ends.pop()

    # Traversal
    for coord in path_without_ends:
        grid.putpixel(coord, powder_blue)
        plt.imshow(grid)
        plt.pause(0.001)

    # Final path
    for node in path_without_ends:
        grid.putpixel(node, kelly_green)

    plt.imshow(grid)
    plt.show()
    print("Iterations taken:", len(path))


def generate_random_traversal_output(grid_size: int, coverage: int):
    # Create obstacle grid with desired size and coverage
    grid = create_obstacle_grid(grid_size, coverage)

    # Get graph representation from image
    graph = create_adjacency_list(grid)

    # Place path ends on graph
    start, end = choose_start_and_end_loc(grid)
    # end = (10, 6)
    grid.putpixel(start, cherry)
    grid.putpixel(end, forest_green)
    plt.imshow(grid)

    path = random_planner(graph, start, end)

    # Remove path ends so as not to overwrite the color in the graph
    path_without_ends = copy.deepcopy(path)
    path_without_ends.pop(0)
    path_without_ends.pop()

    # Traversal
    for coord in path_without_ends:
        grid.putpixel(coord, powder_blue)
        plt.imshow(grid)
        plt.pause(0.001)

    # Final path
    for node in path_without_ends:
        grid.putpixel(node, kelly_green)

    plt.imshow(grid)
    plt.show()


def generate_dijkstras_output(grid_size: int, coverage: int):
    # Create obstacle grid with desired size and coverage
    grid = create_obstacle_grid(grid_size, coverage)

    # Get graph representation from image
    graph = create_adjacency_list(grid)

    # Place path ends on graph
    start, end = choose_start_and_end_loc(grid)
    grid.putpixel(start, cherry)
    grid.putpixel(end, forest_green)
    plt.imshow(grid)

    nodes_with_stages, path, visited = dijkstra(graph, start, end)
    stage_for_end_node = nodes_with_stages.get(end)

    level_order = {}
    for k, v in nodes_with_stages.items():
        level_order[v] = level_order.get(v, []) + [k]
    level_order.pop(-1)

    stages_without_path_ends = copy.deepcopy(level_order)
    stages_without_path_ends.pop(0)
    stages_without_path_ends.pop(stage_for_end_node)

    # Traversal
    for key, value in stages_without_path_ends.items():
        for coord in value:
            grid.putpixel(coord, powder_blue)
            plt.imshow(grid)
        plt.pause(0.001)

    # Final path
    for node in path:
        grid.putpixel(node, kelly_green)

    plt.imshow(grid)
    plt.show()


if __name__ == "__main__":
    grid_size, coverage = 50, 5

    generate_dfs_output(grid_size, coverage)
    # generate_bfs_output(grid_size, coverage)
    # generate_dijkstras_output(grid_size, coverage)
    # generate_random_traversal_output(grid_size, coverage)