# Algorytm prześlij-przemianuj.
# Implementacja niby działa, choć nie jestem pewien, czy ten warunek "while overflow_vertex" nie będzie psuć złożoności.
# Oczekiwana złożoność: O(|V|^2|E|)

from math import inf


def push_relabel_algorithm(graph, s, t):
    n = len(graph)
    height = [0]*n
    excess = [0]*n
    height[s] = n
    for x in range(n):
        if graph[s][x] != 0:
            excess[s] -= graph[s][x]
            excess[x] = graph[s][x]
            graph[x][s] = graph[s][x]
            graph[s][x] = 0
    while overflow_vertex(excess, s, t):
        x = overflow_vertex(excess, s, t)
        b = relabel(graph, excess, height, x)
        if not b:
            for y in range(n):
                xd1 = push(graph, excess, height, x, y)
                if xd1:
                    k = min(excess[x], graph[x][y])
                    graph[x][y] -= k
                    graph[y][x] += k
                    excess[x] -= k
                    excess[y] += k
        else:
            height[x] = b
    return excess[t]


def relabel(graph, excess, height, u):
    if excess[u] == 0:
        return False
    n = len(graph)
    k = inf
    for x in range(n):
        if graph[u][x] != 0:
            if height[u] > height[x]:
                return False
            k = min(k, height[x])
    return k+1


def push(graph, excess, height, u, v):
    if height[u] != height[v] + 1:
        return False
    k = min(excess[u], graph[u][v])
    if k == 0:
        return False
    return True


def overflow_vertex(excess, s, t):
    n = len(excess)
    for x in range(n):
        if x != s and x != t:
            if excess[x] > 0:
                return x


graph = [[0, 0, 0, 0, 0, 0, 0], [0, 0, 16, 13, 0, 0, 0], [0, 0, 0, 4, 12, 0, 0], [0, 0, 0, 0, 9, 14, 0],
         [0, 0, 0, 0, 0, 7, 20], [0, 0, 0, 0, 0, 0, 4], [0, 0, 0, 0, 0, 0, 0]]
print(push_relabel_algorithm(graph, 1, 6))

