import random
from collections import deque
from queue import Queue
from typing import Dict, List, Tuple

from utils import get_unvisited_children


def bfs(graph: Dict, start: Tuple, end: Tuple):
    """
    Traverses the graph using BFS logic.
    """
    tracking_queue = Queue()
    traversed_path = []
    visited = {key: False for key in graph.keys()}
    parent = {key: None for key in graph.keys()}
    level = {key: -1 for key in graph.keys()}

    visited[start] = True
    level[start] = 0
    tracking_queue.put(start)

    while not tracking_queue.empty():
        current_node = tracking_queue.get()
        traversed_path.append(current_node)
        for child in graph[current_node]:
            if visited[child]:  # Ignore already visited nodes
                continue

            if child == end:  # If goal reached, terminate traversal
                visited[child] = True
                parent[child] = current_node
                level[child] = level[current_node] + 1
                with tracking_queue.mutex:
                    tracking_queue.queue.clear()
                break

            visited[child] = True
            parent[child] = current_node
            level[child] = level[current_node] + 1
            tracking_queue.put(child)

    path = []
    current = end
    while current != start:
        next = parent[current]
        path.append(next)
        current = next
    path.pop()

    return level, path, visited


def dfs(graph: Dict, start: Tuple, end: Tuple) -> List:
    """
    Traverses the graph using DFS logic.
    """
    stack = deque()
    traversed_path = []
    visited = {key: False for key in graph.keys()}
    parent = {key: None for key in graph.keys()}

    current_node = start
    visited[current_node] = True
    traversed_path.append(current_node)
    stack.append(current_node)

    while len(stack):
        children = get_unvisited_children(current_node, graph, visited)
        if not children:
            current_node = stack.pop()

        for child in children:
            if visited[child]:
                continue

            if child == end:  # If goal reached, terminate traversal
                visited[child] = True
                parent[child] = current_node
                traversed_path.append(child)
                stack.clear()
                break

            visited[child] = True
            parent[child] = current_node
            traversed_path.append(child)
            stack.append(current_node)
            current_node = child
            break

    return traversed_path


def random_planner(graph: Dict, start: Tuple, end: Tuple) -> List:
    """
    Random planner that simply moves to a random neighboring cell
    at each iteration.
    """
    traversed_path = []
    visited = {key: False for key in graph.keys()}
    parent = {key: None for key in graph.keys()}

    current_node = start
    visited[current_node] = True
    traversed_path.append(current_node)

    index, max_iterations = 0, 1000
    while current_node != end:
        children = get_unvisited_children(current_node, graph, visited)
        if not children:  # If there's nowhere to go, take a step back
            current_node = parent[current_node]
            continue

        child = random.choice(graph[current_node])
        if visited[child]:
            continue

        if child == end:  # If goal reached, terminate traversal
            visited[child] = True
            traversed_path.append(child)
            parent[child] = current_node
            break

        visited[child] = True
        traversed_path.append(child)
        current_node = child

        index += 1
        print(index)
        if index > max_iterations:
            break

    return traversed_path


def dijkstra(graph: Dict, start: Tuple, end: Tuple):
    """
    Traverses the graph using Dijkstra logic.
    """
    tracking_queue = Queue()
    traversed_path = []
    visited = {key: False for key in graph.keys()}
    parent = {key: None for key in graph.keys()}
    level = {key: -1 for key in graph.keys()}

    visited[start] = True
    level[start] = 0
    tracking_queue.put(start)

    while not tracking_queue.empty():
        current_node = tracking_queue.get()
        traversed_path.append(current_node)
        for child in graph[current_node]:
            if visited[child]:  # Ignore already visited nodes
                continue

            if child == end:  # If goal reached, terminate traversal
                visited[child] = True
                parent[child] = current_node
                level[child] = level[current_node] + 1
                with tracking_queue.mutex:
                    tracking_queue.queue.clear()
                break

            visited[child] = True
            parent[child] = current_node
            level[child] = level[current_node] + 1
            tracking_queue.put(child)

    path = []
    current = end
    while current != start:
        next = parent[current]
        path.append(next)
        current = next
    path.pop()

    return level, path, visited
