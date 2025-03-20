import networkx as nx

def build_lastgraph():
    edgelist = []
    with open("lastfm_asia_edges.csv","r") as fitxer:
        next(fitxer)
        for linia in fitxer:
            node1, node2 = linia.strip().split(",") #strip per eliminar espais no desitjats i 
            #split per separar el contingut en una llista amb els dos nodes com a valors
            edgelist.append((int(node1), int(node2))) #afegim els dos nodes en forma d'aresta a
            #la llista d'arestes
    
    G = nx.Graph()
    G.add_edges_from(edgelist) #creem el graf a partir de la llista d'arestes
    return G

if __name__ == "__main__":
    G = build_lastgraph()
    print(G.edges)