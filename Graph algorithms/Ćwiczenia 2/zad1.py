# Edmonds-Karp algorithm. Passed all tests attached to the exercise.

from math import inf
from collections import deque
from dimacs import *


def bfs(graph, parent, s, t):
    n = len(graph)
    visited = [0]*n
    Q = deque()
    Q.append(s)
    visited[s] = 1
    while Q:
        u = Q.popleft()
        for x in range(n):
            if graph[u][x] != 0 and visited[x] == 0:
                visited[x] = 1
                parent[x] = u
                if x == t:
                    return True
                Q.append(x)


def edmonds_karp_algorithm(graph, s, t):
    n = len(graph)
    parent = [-1]*n
    max_flow = 0
    while bfs(graph, parent, s, t):
        flow = inf
        v = t
        while v != s:
            flow = min(flow, graph[parent[v]][v])
            v = parent[v]
        v = t
        max_flow += flow
        while v != s:
            graph[parent[v]][v] -= flow
            graph[v][parent[v]] += flow
            v = parent[v]
    return max_flow


def list_to_matrix(v, list):
    graph = [[0 for _ in range(v+1)] for _ in range(v+1)]
    for x in range(len(list)):
        graph[list[x][0]][list[x][1]] = list[x][2]
    return graph


(V, L) = loadWeightedGraph("graphs-lab2/flow/simple")
print(L)
graph = list_to_matrix(V, L)
print(graph)
print("Maximum flow is: %d" % edmonds_karp_algorithm(graph, 1, V))
