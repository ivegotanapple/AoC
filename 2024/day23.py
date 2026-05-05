#!/usr/bin/env python3
# Written by claude

from collections import defaultdict

with open('input_day23', 'r', encoding='utf-8') as f:
    data = f.read().strip()

edges = [line.split('-') for line in data.splitlines()]
graph = defaultdict(set)
for a, b in edges:
    graph[a].add(b)
    graph[b].add(a)

nodes = list(graph.keys())

# Part 1: count triangles containing a 't' node
triangles = set()
for a in nodes:
    for b in graph[a]:
        for c in graph[b]:
            if c in graph[a]:
                triple = tuple(sorted([a, b, c]))
                triangles.add(triple)

count_t = sum(1 for tri in triangles if any(n.startswith('t') for n in tri))
print(count_t)

# Part 2: find largest clique (Bron-Kerbosch with pivoting)
def bron_kerbosch(R, P, X, cliques):
    if not P and not X:
        cliques.append(frozenset(R))
        return
    pivot = max(P | X, key=lambda v: len(graph[v] & P))
    for v in P - graph[pivot]:
        bron_kerbosch(R | {v}, P & graph[v], X & graph[v], cliques)
        P = P - {v}
        X = X | {v}

cliques = []
bron_kerbosch(set(), set(nodes), set(), cliques)
largest = max(cliques, key=len)
print(','.join(sorted(largest)))
