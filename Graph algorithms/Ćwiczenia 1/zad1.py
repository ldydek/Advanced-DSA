# Dany jest graf nieskierowany G = (V,E), funkcja c: E -> N dająca wagi krawędziom, oraz wyróżnione wierzchołki s i t.
# Szukamy scieżki z s do t takiej, że najmniejsza waga krawędzi na tej ścieżce jest jak największa.
# Należy zwrócić najmniejszą wagę krawędzi na znalezionej ścieżce.
# (W praktyce ścieżki szukamy tylko koncepcyjnie.)
#
# Rozwiązanie: To podejście opiera się na zmodyfikowanym algorytmie Dijkstry, w którym do kolejki dodajemy wagi
# krawędzi ze zmienionym znakiem tak, aby kolejka ustalała priorytet na największą krawędź. W tablicy distance zamiast
# odległości od źródła zapisuję minimum z wartości, która już się tam znajduje oraz z wagi krawędzi obecnie rozważanej.
from math import inf
from queue import PriorityQueue
from dimacs import *


def dijkstra_algorithm(tab, s, t):
    Q = PriorityQueue()
    n = len(tab)
    distance = [-inf for _ in range(n)]
    distance[s] = inf
    visited = [[False for _ in range(n)] for _ in range(n)]
    Q.put((0, s))

    while not Q.empty():
        a, b = Q.get()
        # a - minimalna waga krawędzi
        # b - wierzchołek
        for x in range(n):
            if tab[b][x] != 0 and visited[b][x] is False:
                visited[b][x] = True
                if distance[x] < min(distance[b], tab[b][x]):
                    distance[x] = min(distance[b], tab[b][x])
                    Q.put((-distance[x], x))
    return distance[t]


def list_to_matrix(list):
    n = len(list)
    v = -10**10
    for x in range(n):
        v = max(list[x][0], list[x][1])
    v += 1
    graph = [[0 for _ in range(v)] for _ in range(v)]
    for x in range(n):
        graph[list[x][0]][list[x][1]] = list[x][2]
    return graph


(V,L) = loadWeightedGraph("graphs/clique5")
print((V, L))
