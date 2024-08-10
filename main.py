import matplotlib.pyplot as plt
import networkx as nx

# Define the edges and their weights
edges = [
    ("Data center", "Kantor1", 30),
    ("Data center", "Kantor2", 20),
    ("Data center", "Pemukiman1", 10),
    ("Kantor1", "Pemukiman1", 5),
    ("Kantor1", "Pemukiman2", 25),
    ("Kantor2", "Pemukiman1", 13),
    ("Kantor2", "Pemukiman2", 40),
]

# Initialize the MST and the disjoint-set data structure
parent = {}
rank = {}

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(x, y):
    rootX = find(x)
    rootY = find(y)
    if rootX != rootY:
        if rank[rootX] > rank[rootY]:
            parent[rootY] = rootX
        elif rank[rootX] < rank[rootY]:
            parent[rootX] = rootY
        else:
            parent[rootY] = rootX
            rank[rootX] += 1

# Initialize disjoint-set
vertices = set([u for edge in edges for u in edge[:2]])
for vertex in vertices:
    parent[vertex] = vertex
    rank[vertex] = 0

# Sort edges by weight
edges.sort(key=lambda x: x[2])

# Kruskal's Algorithm
mst = []
for u, v, weight in edges:
    if find(u) != find(v):
        union(u, v)
        mst.append((u, v, weight))

# Print the result
print("Edges in the Minimum Spanning Tree:")
total_weight = 0
for u, v, weight in mst:
    print(f"{u} - {v}: {weight} km")
    total_weight += weight

print(f"Total weight: {total_weight} km")

# Create a graph
G = nx.Graph()
for u, v, weight in edges:
    G.add_edge(u, v, weight=weight)
for u, v, weight in mst:
    G[u][v]['color'] = 'red'  # MST edges in red

# Draw the graph
pos = nx.spring_layout(G)  # Layout for nodes
edges_to_draw = G.edges()
edge_colors = [G[u][v].get('color', 'black') for u, v in edges_to_draw]

plt.figure(figsize=(10, 8))
nx.draw_networkx_nodes(G, pos, node_size=700)
nx.draw_networkx_edges(G, pos, edgelist=edges_to_draw, edge_color=edge_colors)
nx.draw_networkx_labels(G, pos, font_size=16, font_family='sans-serif')
edge_labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
plt.title("Minimum Spanning Tree Visualization")
plt.show()