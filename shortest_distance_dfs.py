from collections import defaultdict
import matplotlib.pyplot as plt
import networkx as nx

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, u, v, weight):
        self.graph[u].append((v, weight))

    def dfs(self, start, end, path, visited, distances, min_path, min_distance):
        visited.add(start)
        path.append(start)

        if start == end:
            if distances[end] < min_distance[0]:
                min_distance[0] = distances[end]
                min_path[:] = path[:]
        else:
            for neighbor, weight in self.graph[start]:
                if neighbor not in visited:
                    distances[neighbor] = distances[start] + weight
                    self.dfs(neighbor, end, path, visited, distances, min_path, min_distance)
                    distances[neighbor] = float('inf')

        path.pop()
        visited.remove(start)

    def shortest_path(self, start, end):
        visited = set()
        path = []
        distances = defaultdict(lambda: float('inf'))
        distances[start] = 0
        min_path = []
        min_distance = [float('inf')]

        self.dfs(start, end, path, visited, distances, min_path, min_distance)

        if min_path:
            return min_path, min_distance[0]
        else:
            return "No path found"

    def plot_graph(self, shortest_path, filename='graph_dfs.png'):
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
g.add_edge(0, 3, 2)
g.add_edge(0, 2, 5)
g.add_edge(0, 1, 1)
g.add_edge(1, 2, 1)
g.add_edge(2, 3, 1)

start_node = 0
end_node = 3
result = g.shortest_path(start_node, end_node)

if isinstance(result, tuple):
    path, distance = result
    print(f"Shortest path from {start_node} to {end_node} is {path} with distance {distance}")
    
    # Plot the graph, highlight the shortest path, and save it as 'graph_dfs.png'
    g.plot_graph(path, 'graph_dfs.png')
else:
    print(result)
