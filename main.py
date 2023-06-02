import networkx as nx
import numpy as np

# Number of Requirements and Elements
num_requirements = 100000
num_requirements = 50000
num_elements = 500
num_elements = 300

# Initialize a directed graph
G = nx.DiGraph()

# Create nodes for Requirements and Elements
# We differentiate them by prefixing with 'R' and 'E' respectively
requirements = np.array(['R'+str(i) for i in range(num_requirements)])
elements = np.array(['E'+str(i) for i in range(num_elements)])

# Add nodes to the graph
G.add_nodes_from(requirements)
G.add_nodes_from(elements)

# Create an array with random "goodness" scores, shape (num_requirements, num_elements)
goodness_scores = np.random.randint(0, 10, size=(num_requirements, num_elements))

# Indices where goodness score > 0
goodness_indices = np.where(goodness_scores > 0)

# Create a list of edges using these indices
edges = list(zip(requirements[goodness_indices[0]], elements[goodness_indices[1]]))

# Add edges to the graph with "goodness" scores
G.add_edges_from(edges, weight=goodness_scores[goodness_scores > 0])

print(f"Graph is created with {G.number_of_nodes()} nodes and {G.number_of_edges()} edges.")

