# Dany jest graf nieskierowany G = (V,E), funkcja c: E -> N dająca wagi krawędziom, oraz wyróżnione wierzchołki s i t.
# Szukamy scieżki z s do t takiej, że najmniejsza waga krawędzi na tej ścieżce jest jak największa.
# Należy zwrócić najmniejszą wagę krawędzi na znalezionej ścieżce.
# (W praktyce ścieżki szukamy tylko koncepcyjnie.)
#
# Rozwiązanie: Podejście za pomocą zbiorów rozłącznych. Pewna analogia do algorytmu Kruskala wyznaczającego MST.
# Sortuję krawędzie malejąco po ich wagach a następnie buduję nowy graf dzięki operacji "union" do momentu aż
# dwa wierzchołki (źródło oraz ujście) nie będą w jednym zbiorze. Jeżeli w jednym zbiorze się znajdą, to oznaczać to
# będzie, że istnieje pewna ścieżka pomiędzy tymi wierzchołkami a dodana waga jest naszą szukaną odpowiedzią.


def matrix_to_list(graph):
    list = []
    n = len(graph)
    for x in range(n):
        for y in range(x+1, n):
            if graph[x][y] != 0:
                list.append((x, y, graph[x][y]))
    return list


def find(parent, i):
    if parent[i] != i:
        parent[i] = find(parent, parent[i])
    return parent[i]


def union(x, y, parent, rank):
    x = find(parent, x)
    y = find(parent, y)
    if rank[x] > rank[y]:
        parent[y] = x
    elif rank[x] < rank[y]:
        parent[x] = y
    else:
        parent[x] = y
        rank[y] += 1


def path(graph, s, t):
    v = len(graph)
    parent = [x for x in range(v)]
    rank = [0] * v
    list = matrix_to_list(graph)
    list.sort(key=lambda x: x[2], reverse=True)
    for x in range(len(list)):
        union(list[x][0], list[x][1], parent, rank)
        if find(parent, s) == find(parent, t):
            return list[x][2]


graph = [[0, 3, 5, 0, 0, 0], [3, 0, 4, 2, 5, 0], [5, 4, 0, 6, 1, 0], [0, 2, 6, 0, 3, 4], [0, 5, 1, 3, 0, 5],
         [0, 0, 0, 4, 5, 0]]
print(path(graph, 0, 5))

