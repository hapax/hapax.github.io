import networkx as nx
import matplotlib.pyplot as plt

# Example

digraph = nx.DiGraph()
digraph.add_edges_from([(1, 2), (6,2), (2, 3), (3,4), (3,5)])
nx.draw(digraph, with_labels = True)
plt.show()

# Count linear extensions

def count_ext_chains(digraph):
    max_elements = []
    total = 0
    if len(list(digraph.nodes())) == 1:
        total += 1
    else:
        for node in digraph.nodes():
            if not list(digraph.predecessors(node)):
                max_elements.append(node)
    for node in max_elements:
        new_nodes = list(digraph.nodes()).copy()
        new_nodes.remove(node)
        subgraph = digraph.subgraph(new_nodes)
        total += count_ext_chains(subgraph)
    return total
