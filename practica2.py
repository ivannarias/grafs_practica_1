import networkx as nx


def components_BFS(G):
    llista = []
    vist = set()

    for node in G.nodes:
        if node not in vist:
            component = []
            nodes = [node]

            while nodes:
                node = nodes.pop(0)
                if node not in vist:
                    vist.add(node)
                    component.append(node)
                    nodes.append(G[node])
        llista.append(component)
    
    return llista

