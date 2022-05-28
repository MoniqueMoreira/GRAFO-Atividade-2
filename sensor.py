from grafo import Grafo
import  numpy as np

def criar_grafo(G,arq):
    # Criar o grafo de acordo com o arquivo recebido
    linhas = arq.readlines()
    qv,qa = linhas[0].split()
    linhas.pop(0)
    for i in range(int(qv)):
        G.set_vertice(i+1)
    for linha in linhas:
        u,v,peso = linha.split()
        u = int(u)
        v = int(v)
        peso = int(peso)
        G.set_aresta(u,v,peso)
    #g.__str__()
    
def gerar_tabela_dist(G):
    D = np.zeros((G.ord,G.ord)) # Alterar
    D = G.floyd()
    return D

def dist_sum_vec(D):
    dist_vec = np.zeros(D.shape[0])
    for l in range(D.shape[0]):
        for c in range(D.shape[1]):
            dist_vec[l] = dist_vec[l]+D[l][c]
    return dist_vec

def max_dist_vec(D):
    max_vec  = np.zeros(D.shape[0])
    for l in range(D.shape[0]):
        for c in range(D.shape[1]):
            if max_vec[l] < D[l][c]:
                max_vec[l] = D[l][c]
    return max_vec

def central(dist_vec,max_vec):
    sm = 99999
    central = -1
    for i in range(len(dist_vec)):
        if dist_vec[i] < sm:
            sm = dist_vec[i]
            central = i
        elif dist_vec[i] == sm:
            if max_vec[i] < max_vec[central-1]:
                sm = dist_vec[i]
                central = i
    return central + 1

def Caso_1():
    G = Grafo()
    arq = open("grafo01.txt")
    criar_grafo(G,arq)
    #G.__str__()
    # --------------
    D = gerar_tabela_dist(G)
    print("Tabela de Distâncias:")
    print(D,"\n")
    dist_vec = dist_sum_vec(D)
    max_vec = max_dist_vec(D)
    print("Somatório dos custos para chegar nos demais vértices:")
    print(dist_vec,"\n")
    print("Custo para o vértices mais distantes:")
    print(max_vec,"\n")   
    c = central(dist_vec,max_vec)
    print("O melhor vértice para ser central é:")
    print(c)

def Caso_2():
    G = Grafo()
    G.set_orientado() # define que grafo é orientado
    arq = open("grafo02.txt")
    criar_grafo(G,arq)
    print(G.matriz_adj())
    #G.__str__()
    # --------------
    D = gerar_tabela_dist(G)
    print("Tabela de Distâncias:")
    print(D,"\n")
    dist_vec = dist_sum_vec(D)
    max_vec = max_dist_vec(D)
    print("Somatório dos custos para chegar nos demais vértices:")
    print(dist_vec,"\n")
    print("Custo para o vértices mais distantes:")
    print(max_vec,"\n")   
    c = central(dist_vec,max_vec)
    print("O melhor vértice para ser central é:")
    print(c)

def i():
    Caso_1()
    Caso_2()

i()