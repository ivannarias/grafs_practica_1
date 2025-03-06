import networkx as nx
from tasca1 import build_lastgraph

G = build_lastgraph()

def components_BFS(G):
    nodes_ja_visitats = set() #conjunt de nodes que ja hem visitat per evitar visitar el mateix conjunt dues vegades.
    llista_final = [] #llista que guardara les components de G.
    
    for node in G.nodes():
        if node not in nodes_ja_visitats:
            Q = [] #llista de vèrtexs pendents. DE CADA COMPONENT
            R = [] #llista de vèrtexs visitats. DE CADA COMPONENT
            Q.append(node)
            
            while Q:
                node_actual = Q.pop(0)
                
                if node_actual not in nodes_ja_visitats:
                    nodes_ja_visitats.add(node_actual)
                    R.append(node_actual)
                    
                    for vei in G.neighbors(node_actual):
                        if vei not in nodes_ja_visitats:
                            Q.append(vei)
            
            llista_final.append(R)
        
    return llista_final

components = components_BFS(G)
print(components)