# shortest-path

## Project Overview

This project implements and visualizes three different algorithms for finding the shortest path in a directed weighted graph:

1. **Dijkstra's Algorithm** - implemented using a custom AVL tree for managing the priority queue.
2. **Breadth-First Search (BFS)** based shortest path - implemented using Python's \`heapq\` for priority management.
3. **Depth-First Search (DFS)** based shortest path - implemented with recursive backtracking.

Each algorithm builds a graph, computes the shortest path between given start and end nodes, and visualizes the graph highlighting the shortest path using \`networkx\` and \`matplotlib\`.

---

## Features

- **AVL Tree Implementation:**  
  A fully functional AVL tree is implemented to manage nodes by their tentative shortest distances efficiently for Dijkstra's algorithm.

- **Graph Data Structure:**  
  The graph is represented as adjacency lists with weighted edges using Python dictionaries or \`defaultdict\`.

- **Shortest Path Algorithms:**  
  - **Dijkstra's Algorithm** uses the AVL tree to prioritize nodes with minimum distances.  
  - **BFS with Priority Queue** uses \`heapq\` for efficient minimum distance extraction.  
  - **DFS with Backtracking** explores all paths to find the shortest path.

- **Graph Visualization:**  
  Uses \`networkx\` to create directed graphs and \`matplotlib\` to display and save images of the graphs, highlighting shortest paths in red.

---

## Installation

Make sure you have Python 3 installed. Install the required dependencies using pip:

\`\`\`bash
pip install matplotlib networkx sortedcontainers
\`\`\`

---

## Usage

### Dijkstra's Algorithm with AVL Tree

- Construct a graph and add edges using \`Graph.add_edge(u, v, w)\`.
- Call \`Graph.dijkstra(start_node, end_node)\` to get shortest distances, path, and edges in the shortest path.
- Use \`draw_graph(graph.graph, path_edges=path_edges)\` to visualize and save the graph image with the shortest path highlighted.

Example snippet:

\`\`\`python
g = Graph()
g.add_edge(1, 2, 1)
g.add_edge(2, 3, 2)
g.add_edge(1, 3, 4)
g.add_edge(3, 4, 1)

distances, path, path_edges = g.dijkstra(1, 3)
draw_graph(g.graph, path_edges=path_edges)
print(f\"Shortest distance: {distances[3]}\")
print(f\"Path: {path}\")
\`\`\`

---

### BFS-based Shortest Path

- Use the \`Graph\` class that implements BFS with a priority queue.
- Add edges similarly and call \`bfs(start, end)\` to get the shortest path and distance.
- Call \`plot_graph(shortest_path, filename)\` to visualize and save the graph.

Example:

\`\`\`python
g = Graph()
g.add_edge(0, 1, 1)
g.add_edge(0, 2, 1)
g.add_edge(2, 1, 2)
g.add_edge(1, 3, 1)
g.add_edge(2, 3, 5)

path, distance = g.bfs(0, 3)
print(f\"Shortest path: {path} with distance: {distance}\")
g.plot_graph(path, 'graph_bfs.png')
\`\`\`

---

### DFS-based Shortest Path

- Use the \`Graph\` class that implements DFS with backtracking.
- Add edges and call \`shortest_path(start, end)\` to find the shortest path and distance.
- Visualize using \`plot_graph\`.

Example:

\`\`\`python
g = Graph()
g.add_edge(0, 3, 2)
g.add_edge(0, 2, 5)
g.add_edge(0, 1, 1)
g.add_edge(1, 2, 1)
g.add_edge(2, 3, 1)

result = g.shortest_path(0, 3)
if isinstance(result, tuple):
    path, distance = result
    print(f\"Shortest path: {path} with distance: {distance}\")
    g.plot_graph(path, 'graph_dfs.png')
else:
    print(result)
\`\`\`

---

## Dependencies

- \`matplotlib\` - for plotting and saving graph images
- \`networkx\` - for creating and managing graph visualizations
- \`sortedcontainers\` - used in AVL tree implementation (if needed)
- \`heapq\` - standard Python library for priority queues

---

## Project Structure

- \`AVLTree\` and \`AVLNode\` classes implement the balanced tree for priority management.
- \`Graph\` class contains graph methods for adding edges and running shortest path algorithms.
- Visualization functions use \`networkx\` and \`matplotlib\` to plot graphs and highlight paths.

---

## Notes

- The AVL tree based Dijkstra's algorithm is a custom implementation to demonstrate balanced tree usage as an alternative to a binary heap.
- BFS here is adapted to handle weighted graphs using a priority queue (\`heapq\`).
- DFS explores all paths exhaustively and is less efficient for large graphs.

