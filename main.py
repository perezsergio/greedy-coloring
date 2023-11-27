import csv
from collections import defaultdict


def get_graph_from_csv(file_path: str) -> dict[int, list[int]]:
    """
    Read a csv file where each row represents a pair of neighboring vertices in a vertex graph,
    compute the list of neighboring vertices for each vertex.

    Args:
    file_path: str -- Path of a csv file that defines a vertex graph. The format of the csv file should be as follows:
        the vertices are represented by integers, each row contains a pair of neighboring vertices, the first row is a header.

    Returns:
    graph: dict -- Dictionary of key-value pairs, where each key represents a vertex and the corresponding value is a list of
        integers that represent the neighboring vertices.
    """
    vertices_neighbors = defaultdict(list)
    with open(file_path, "r") as csv_file:
        reader = csv.reader(csv_file, delimiter=" ")
        next(reader)  # Skip first row (header)
        for row in reader:
            vertex1, vertex2 = map(int, row)
            vertices_neighbors[vertex1].append(vertex2)
            vertices_neighbors[vertex2].append(vertex1)
    return dict(vertices_neighbors)


def greedy_coloring(graph: dict[int, list[int]]):
    """
    Apply the greedy coloring algorithm with the 'largest_first' ordering strategy to a graph,
    return the colored graph.
    """
    colors = {}
    # Sort vertices by the number of neighbors, in descending order.
    vertices_sorted = sorted(
        graph,
        key=lambda x: len(graph[x]),
        reverse=True,
    )

    # The color of the vertex must be an element of the set {0, ..., num_of_nodes -a}
    possible_colors = set(range(len(graph)))

    for vertex in vertices_sorted:
        neighbors = graph[vertex]
        # Get the set of colors used by the neighbors
        neighbor_colors = set(
            colors[neighbor] for neighbor in neighbors if neighbor in colors
        )
        # The color must be possible colors and must not be in used_colors
        available_colors = possible_colors - neighbor_colors
        # We choose to use the smallest value available
        colors[vertex] = min(available_colors)
    return colors


def main():
    """
    Read graph from csv at file_path, color graph with greedy coloring,
    display the number of colors used
    """
    file_path = "../graph-coloring/data/graphs/gc_20_3"  # Replace with the path to your CSV file
    graph = get_graph_from_csv(file_path)
    colors = greedy_coloring(graph)
    print(f"Colored graph with {max(colors.values()) + 1} colors")


main()
