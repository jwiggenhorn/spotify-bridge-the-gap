import networkx as nx
from main import add_related_artists, get_access_token

G = nx.read_gml("artists.gml")

source = [node for node, attr in G.nodes(data=True) if attr['name']=='potsu'][0]
target = [node for node, attr in G.nodes(data=True) if attr['name']=='Pig Destroyer'][0]

path = nx.shortest_path(G, source, target)

for node in [node for node in G.nodes if node not in path]:
    G.remove_node(node)

for node in path:
    add_related_artists(G, node, get_access_token())

nx.write_gml(G, "artists-pruned.gml")