from collections import defaultdict
import heapq
import matplotlib.pyplot as plt
import networkx as nx

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, u, v, weight):
        self.graph[u].append((v, weight))
        if v not in self.graph:
            self.graph[v] = []

    def bfs(self, start, end):
        queue = [(0, start)]
        distances = {node: float('inf') for node in self.graph}
        distances[start] = 0
        path = {node: None for node in self.graph}

        while queue:
            current_distance, current_node = heapq.heappop(queue)

            if current_node == end:
                break

            for neighbor, weight in self.graph[current_node]:
                distance = current_distance + weight

                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    path[neighbor] = current_node
                    heapq.heappush(queue, (distance, neighbor))

        shortest_path = []
        while end is not None:
            shortest_path.append(end)
            end = path[end]
        shortest_path.reverse()

        return shortest_path, distances[shortest_path[-1]]

    def plot_graph(self, shortest_path, filename='graph.png'):
        G = nx.DiGraph()
        
        # Add nodes and edges to the NetworkX graph
        for node, neighbors in self.graph.items():
            for neighbor, weight in neighbors:
                G.add_edge(node, neighbor, weight=weight)
        
        pos = nx.spring_layout(G)
        labels = nx.get_edge_attributes(G, 'weight')

        # Draw the graph
        nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=500, font_size=10, font_weight='bold', arrows=True)
        nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)

        # Highlight the shortest path
        edge_list = [(shortest_path[i], shortest_path[i+1]) for i in range(len(shortest_path) - 1)]
        nx.draw_networkx_edges(G, pos, edgelist=edge_list, width=3, edge_color='r')

        # Save the graph as a PNG
        plt.savefig(filename, format='png')
        print(f"Graph saved as {filename}")
        plt.close()  # Close the plot to avoid displaying it inline

# Example usage
g = Graph()
g.add_edge(0, 1, 1)
g.add_edge(0, 2, 1)
g.add_edge(2, 1, 2)
g.add_edge(1, 3, 1)
g.add_edge(2, 3, 5)

start_node = 0
end_node = 3
path, distance = g.bfs(start_node, end_node)
print(f"Shortest path from {start_node} to {end_node} is {path} with distance {distance}")

# Plot the graph, highlight the shortest path, and save it as 'graph.png'
g.plot_graph(path, 'graph_bfs.png')
