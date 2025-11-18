"""
HW01 — Cables and Devices

Implement:
- build_graph(edges, directed=False)
- degree_dict(graph)

Do NOT add type hints. Use only the standard library.
"""

def build_graph(edges, directed=False):
    """
    Return a dictionary: node -> list of neighbors.

    edges: list of (u, v) pairs.
    directed: if True, add only u->v; if False, add both u->v and v->u.
    """
    graph = {}

    for u, v in edges:
        # Ensure u exists
        if u not in graph:
            graph[u] = []
        # Ensure v exists (even if it gets no outgoing edges)
        if v not in graph:
            graph[v] = []

        # Always add u -> v
        graph[u].append(v)

        if not directed:
            # Add reverse direction for undirected graphs
            graph[v].append(u)

    return graph


def degree_dict(graph):
    """
    Return a dictionary: node -> degree (number of neighbors).

    For directed graphs, this is out-degree.
    For undirected graphs, this equals the usual degree.
    """
    d = {}
    for node, neighbors in graph.items():
        d[node] = len(neighbors)
    return d


if __name__ == "__main__":
    # Optional manual check
    sample = [('PC1','SW1'), ('SW1','PR1'), ('PR1','PC2')]
    g = build_graph(sample, directed=False)
    print("Graph:", g)
    print("Degrees:", degree_dict(g))
