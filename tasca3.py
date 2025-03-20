import networkx as nx
import time
from tasca1 import build_lastgraph

def components_DFS (G):
    inici = time.time()
    llista_final = []
    pila = []
    
    diccionari_estats = {}
    for node in G.nodes():
        diccionari_estats [node] = "no visitat" #inicialitzem un diccionari amb tots els nodes i els seus estats
    
    for node in G.nodes():
        if diccionari_estats[node] == "no visitat":  
            component = [] #si no l'hem visitat, estem a una nova component
            diccionari_estats[node] = "visitat" #i el marquem com visitat
            pila.append(node) #i el posem a la pila
            while len(pila) != 0: #mentre hi hagi nodes a la pila
                node_actual = pila.pop() #treiem el més proper com a node actual
                for vei in G.neighbors(node_actual):
                    if diccionari_estats[vei] == "no visitat": #i per cada veí del node actual, si no l'hem visitat, el marquem com visitat i el posem a la pila
                        diccionari_estats[vei] = "visitat"
                        pila.append(vei) #d'aquesta manera, la pila es va actualitzant amb cada nou node (veí de l'anterior), i cerquem en profunditat
                component.append(node_actual)
            llista_final.append(component) #afegim la component trobada a la llista final
    
    final = time.time()
    return llista_final, (final - inici)

if __name__ == "__main__":
    G = build_lastgraph()
    components, temps_execucio = components_DFS(G)
    print(components)
    print(f"Temps d'execució: {temps_execucio}s")
    print(f"El graf té {len(components)} component/s")