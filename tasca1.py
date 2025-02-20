import networkx as nx

def build_lastgraph():
    edgelist = []
    with open("lastfm_asia_edges_copy.csv","r") as fitxer:
        next(fitxer)
        for linia in fitxer:
            node1, node2 = linia.strip().split(",")
            edgelist.append((int(node1), int(node2)))
    
    G = nx.Graph()
    G.add_edges_from(edgelist)
    return G

G = build_lastgraph()

print(list(G.neighbors(3)))
#G.edges([1, 3])