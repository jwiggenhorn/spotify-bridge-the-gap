import sys
import networkx as nx
import matplotlib.pyplot as plt

G = nx.read_gml("artists.gml")

source = [node for node, attr in G.nodes(data=True) if attr['name']==sys.argv[1]][0]
target = [node for node, attr in G.nodes(data=True) if attr['name']==sys.argv[2]][0]

path = [G.nodes[node]['name'] for node in nx.shortest_path(G, source, target)]
print(f'Shortest path length: {len(path)}')
print(*path, sep = " -> ")

plt.title('\nDegree distribution (log-log scale)')
plt.xlabel('Degree\n(log scale)')
plt.ylabel('Number of Nodes\n(log scale)')
plt.xscale("log")
plt.yscale("log")
plt.plot(nx.degree_histogram(G))
plt.show()