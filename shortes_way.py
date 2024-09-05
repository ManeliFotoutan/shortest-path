import heapq
from sortedcontainers import SortedDict
import matplotlib.pyplot as plt
import networkx as nx

class AVLNode:
    def __init__(self, key, value, height=1, left=None, right=None):
        self.key = key
        self.value = value
        self.height = height
        self.left = left
        self.right = right

class AVLTree:
    def __init__(self):
        self.root = None
    
    def get_height(self, node):
        if not node:
            return 0
        return node.height
    
    def get_balance(self, node):
        if not node:
            return 0
        return self.get_height(node.left) - self.get_height(node.right)
    
    def rotate_right(self, y):
        x = y.left
        T2 = x.right
        
        x.right = y
        y.left = T2
        
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))
        x.height = 1 + max(self.get_height(x.left), self.get_height(x.right))
        
        return x
    
    def rotate_left(self, x):
        y = x.right
        T2 = y.left
        
        y.left = x
        x.right = T2
        
        x.height = 1 + max(self.get_height(x.left), self.get_height(x.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))
        
        return y
    
    def insert(self, node, key, value):
        if not node:
            return AVLNode(key, value)
        
        if key < node.key:
            node.left = self.insert(node.left, key, value)
        elif key > node.key:
            node.right = self.insert(node.right, key, value)
        else:
            node.value = value
            return node
        
        node.height = 1 + max(self.get_height(node.left), self.get_height(node.right))
        
        balance = self.get_balance(node)
        
        if balance > 1 and key < node.left.key:
            return self.rotate_right(node)
        
        if balance < -1 and key > node.right.key:
            return self.rotate_left(node)
        
        if balance > 1 and key > node.left.key:
            node.left = self.rotate_left(node.left)
            return self.rotate_right(node)
        
        if balance < -1 and key < node.right.key:
            node.right = self.rotate_right(node.right)
            return self.rotate_left(node)
        
        return node
    
    def min_value_node(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current
    
    def delete(self, node, key):
        if not node:
            return node
        
        if key < node.key:
            node.left = self.delete(node.left, key)
        elif key > node.key:
            node.right = self.delete(node.right, key)
        else:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            
            temp = self.min_value_node(node.right)
            node.key = temp.key
            node.value = temp.value
            node.right = self.delete(node.right, temp.key)
        
        if not node:
            return node
        
        node.height = 1 + max(self.get_height(node.left), self.get_height(node.right))
        
        balance = self.get_balance(node)
        
        if balance > 1 and self.get_balance(node.left) >= 0:
            return self.rotate_right(node)
        
        if balance > 1 and self.get_balance(node.left) < 0:
            node.left = self.rotate_left(node.left)
            return self.rotate_right(node)
        
        if balance < -1 and self.get_balance(node.right) <= 0:
            return self.rotate_left(node)
        
        if balance < -1 and self.get_balance(node.right) > 0:
            node.right = self.rotate_right(node.right)
            return self.rotate_left(node)
        
        return node
    
    def search(self, node, key):
        if not node or node.key == key:
            return node
        if key < node.key:
            return self.search(node.left, key)
        return self.search(node.right, key)
    
    def insert_key_value(self, key, value):
        self.root = self.insert(self.root, key, value)
    
    def delete_key(self, key):
        self.root = self.delete(self.root, key)
    
    def search_key(self, key):
        node = self.search(self.root, key)
        if node:
            return node.value
        return None

class Graph:
    def __init__(self):
        self.graph = {}
    
    def add_edge(self, u, v, w):
        if u not in self.graph:
            self.graph[u] = []
        self.graph[u].append((v, w))
    
    def dijkstra(self, start, end):
        avl_tree = AVLTree()
        avl_tree.insert_key_value(start, 0)
        
        distances = {node: float('inf') for node in self.graph}
        distances[start] = 0
        
        predecessors = {node: None for node in self.graph}
        
        while avl_tree.root:
            current_node = avl_tree.root.key
            current_distance = avl_tree.root.value
            avl_tree.delete_key(current_node)
            
            if current_node == end:
                break
            
            for neighbor, weight in self.graph.get(current_node, []):
                distance = current_distance + weight
                
                if distance < distances.get(neighbor, float('inf')):
                    distances[neighbor] = distance
                    predecessors[neighbor] = current_node
                    avl_tree.insert_key_value(neighbor, distance)
        
        path = []
        while end is not None:
            path.append(end)
            end = predecessors[end]
        path.reverse()
        
        # Collect path edges for visualization
        path_edges = set()
        for i in range(len(path) - 1):
            path_edges.add((path[i], path[i + 1]))
        
        return distances, path, path_edges

def draw_graph(graph, path_edges=None, filename="graph.png"):
    G = nx.DiGraph()
    
    # Add nodes and edges from the graph
    for u, neighbors in graph.items():
        for v, w in neighbors:
            G.add_edge(u, v, weight=w)
    
    pos = nx.spring_layout(G)  # Positioning for nodes
    edge_labels = nx.get_edge_attributes(G, 'weight')  # Get edge weights

    # Set the color for all edges
    edge_colors = ['black' for _ in G.edges()]
    
    if path_edges:
        # Highlight path edges in red
        edge_colors = ['red' if (u, v) in path_edges or (v, u) in path_edges else 'black' for u, v in G.edges()]

    plt.figure(figsize=(10, 8))
    nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=3000, font_size=10, font_weight='bold', edge_color=edge_colors, arrows=True)
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
    
    plt.title("Graph Visualization")
    plt.savefig(filename)
    plt.show()

# Example Usage
g = Graph()
g.add_edge(1, 2, 1)
g.add_edge(2, 3, 2)
g.add_edge(1, 3, 4)
g.add_edge(3, 4, 1)

# Compute shortest paths
start_node = 1
end_node = 3
distances, path, path_edges = g.dijkstra(start_node, end_node)

# Draw and save the graph with the shortest path highlighted
draw_graph(g.graph, path_edges=path_edges)

print(f"Shortest distance from {start_node} to {end_node} is {distances[end_node]}")
print(f"Path: {path}")
