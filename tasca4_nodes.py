import networkx as nx
import random
from tasca1 import build_lastgraph
from tasca3 import components_DFS

def comprovar_nodes():
    G = build_lastgraph()
    components, temps_execucio = components_DFS(G)
    iteracions = 0

    while len(components) == 1: #executem el bucle mentre hi hagi una única component
        iteracions += 1
        nodes = G.nodes()
        if len(G.nodes()) > 0: #ens assegurem que la longitud de la llista de nodes no sigui 0
            node_random = random.choice(list(G.nodes())) #escollim una aresta a l'atzar
            G.remove_node(node_random) #eliminem el node
            components, temps_execucio = components_DFS(G) #escollim un dels algorismes per obtenir el nombre de components
        else:
            print("S'han acabat les arestes")
            break
    return iteracions
#print(f"Ha calgut eliminar {iteracions} nodes.")

l = []
for _ in range(200):
    l.append(comprovar_nodes())

print(f"De mitja hem hagut d'eliminar {sum(l) / len(l)} nodes.")