import networkx as nx
import time
from tasca1 import build_lastgraph

def components_DFS (G):
    llista_final = []
    pila = []
    
    diccionari_estats = {}
    for node in G.nodes():
        diccionari_estats [node] = "no visitat"
    
    for node in G.nodes():
        if diccionari_estats[node] == "no visitat":
            component = []
            diccionari_estats[node] = "visitat"
            pila.append(node)
            while len(pila) != 0:
                node_actual = pila.pop()
                for vei in G.neighbors(node_actual):
                    if diccionari_estats[vei] == "no visitat":
                        diccionari_estats[vei] = "visitat"
                        pila.append(vei)
                component.append(node_actual)
        llista_final.append(component)
    
    return llista_final

G = build_lastgraph()
components = components_DFS(G)
print(components)