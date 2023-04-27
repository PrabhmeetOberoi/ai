def dfs(node, visited, graph, goal):
    # Mark the current node as visited
    visited[node] = True
    print(node)

    # Check if the current node is the goal node
    if node == goal:
        print("Goal node found!")
        return True

    # Recur for all the vertices adjacent to this vertex
    for neighbor in graph[node]:
        if not visited[neighbor]:
            if dfs(neighbor, visited, graph, goal):
                return True

    return False

# Example usage
if __name__ == '__main__':
    # Define the graph as an adjacency list
    graph = {
        0: [1, 2],
        1: [2],
        2: [0, 3],
        3: [3]
    }

    # Define the starting node and the goal node
    start_node = 2
    goal_node = 3

    # Initialize the visited array
    visited = [False] * len(graph)

    # Call dfs() with the starting node and the goal node
    dfs(start_node, visited, graph, goal_node)
