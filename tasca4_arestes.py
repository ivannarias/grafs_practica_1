import networkx as nx
import random
from tasca1 import build_lastgraph
from tasca3 import components_DFS

def comprovar_arestes():
    G = build_lastgraph()
    components, temps_execucio = components_DFS(G)
    iteracions = 0

    while len(components) == 1: #executem el bucle mentre hi hagi una única component
        iteracions += 1
        llista_arestes = G.edges()
        if len(G.edges()) > 0: #ens assegurem que la longitud de la llista d'arestes no sigui 0
            aresta_random = random.choice(list(G.edges())) #escollim una aresta a l'atzar
            G.remove_edge(*aresta_random) # * desempaqueta la tupla que forma l'aresta
            components, temps_execucio = components_DFS(G) #escollim un dels algorismes per obtenir el nombre de components
        else:
            print("S'han acabat les arestes")
            break
    return iteracions
#print(f"Ha calgut eliminar {iteracions} arestes.")

l = []
for _ in range(200):
    l.append(comprovar_arestes())

print(f"De mitja hem hagut d'eliminar {sum(l) / len(l)} arestes.")