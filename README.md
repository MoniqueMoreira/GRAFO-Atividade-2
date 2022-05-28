# GRAFO-Atividade-2

# Problema:-------------------------------------------------

```
  import numpy as np
```

Considere o problema em que existe uma instalação de múltiplos sensores em uma área rural. Apesar esses sensores trabalharem em uma rede mesh distribuída, os comandos precisam chegar a uma estação central, onde roda um sistema supervisório que monitora as condições climáticas, a saúde da plantação, entre outras coisas.

# Cenário 1:
Nesta aplicação, vamos supor 12 locais de instalação de sensor, mas um deles deve ser escolhido como estação central. Usando os conceitos de teoria dos grafos, cada local de instalação pode ser considerado um vértice, enquanto o custo de comunicação (ou distância) entre eles são as arestas. O grafo a seguir representa isso:

![Screenshot](grafo.jpg)

Para encontrar o melhor vértice para ser o central, podemos aplicar uma otimização considerando dois parâmetros. Tomando um vértice candidato a vértice central, computamos o somatório dos custos para chegar nos demais vértices e o custo para o vértice mais distante, para questões de desempate.

## Leitura do arquivo

Nesse caso, temos um grafo não orientado. Esse grafo pode ser representado pelo arquivo grafo01.txt que segue o formato:
```
<num_vertices> <num_arestas>
<vertice_inicial> <vertice_final> <custo> <- Repetição para cada aresta
```

Foi usado o TAB (\t) como separador. Faça a leitura do arquivo:
                                
## Computação de caminho mínimo
                                               
Implemente um algoritmo de computação de caminho mínimo que considere cada vértice do grafo como potencial vértice inicial, isso deve gerar uma tabela relacionando cada vértice (linhas) e a distância para os demais (colunas).

```
def gerar_tabela_dist(G):
  D = np.zeros((1,1)) # Alterar
  ### Faça o código aqui
  return D

D = gerar_tabela_dist(G)
print(D)                    
```
                
## Cálculo dos vetores de distância
                                               
Calcule os vetores de somatório de distâncias e o vetor de distâncias máximas para cada linha da tabela/matriz D.
                                               
```
def dist_sum_vec(D):
  dist_vec = np.zeros(D.shape[0])
  ### Faça o código aqui
  return dist_vec

def max_dist_vec(D):
  max_vec = np.zeros(D.shape[0])
  ### Faça o código aqui
  return max_vec

dist_vec = dist_sum_vec(D)
max_vec = max_dist_vec(D)

print(dist_vec)
print(max_vec)
```
                                               
## Determinando a estação central
                                               
Use os dados e informações computadas para determinar o vértice que será usado como estação central.
                                               
# Cenário 2:
                                               
Agora que o cenário 1 foi resolvido, vamos testar em outras situações (pode fazer chamadas das funções já implementadas). Encontre o vértice que representa melhor uma estação central no grafo apresentado no arquivo grafo02.txt. Dessa vez, considere um grafo direcionado, portanto a função que calcula a matriz de caminho mínimo gerar_tabela_dist(G) vai mudar.
