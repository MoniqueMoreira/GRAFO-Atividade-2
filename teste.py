from grafo import Grafo

def i():
    g = Grafo()
    for i in range(12):
        g.set_vertice(i)
    g.set_aresta(0,2,12)
    g.matriz_adj()

i()