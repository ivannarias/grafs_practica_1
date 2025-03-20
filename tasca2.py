import networkx as nx
import time
from tasca1 import build_lastgraph

G = build_lastgraph()

def components_BFS(G):
    inici = time.time()
    nodes_ja_visitats = set() #conjunt de nodes que ja hem visitat per evitar visitar la mateixa component dues vegades
    llista_final = [] #llista que guardara les components de G
    
    for node in G.nodes():
        if node not in nodes_ja_visitats:
            Q = [] #llista de vèrtexs pendents. DE CADA COMPONENT
            R = [] #llista de vèrtexs visitats. DE CADA COMPONENT
            Q.append(node)
            
            while Q:
                node_actual = Q.pop(0) #agafem el primer node de la pila com a node actual
                
                if node_actual not in nodes_ja_visitats:
                    nodes_ja_visitats.add(node_actual)
                    R.append(node_actual) #afegim el node actual a la llista de nodes visitats de la component
                    
                    for vei in G.neighbors(node_actual):
                        if vei not in nodes_ja_visitats: #afegim tots els veïns del node actual a la llista de pendents per visitar-los després
                            Q.append(vei)
            
            llista_final.append(R) #afegim cada component trobada a la llista final de components
    final = time.time()
    return llista_final, (final - inici)

if __name__ == "__main__":
    components, temps_execucio = components_BFS(G)
    print(components)
    print(f"Temps d'execució: {temps_execucio}s")
    print(f"El graf té {len(components)} component/s")