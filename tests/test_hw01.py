import pytest
import sys
import os

# Add parent directory to path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from main import build_graph, degree_dict

def test_small_undirected_basic():
    edges = [('PC1','SW1'), ('SW1','PR1'), ('PR1','PC2')]
    g = build_graph(edges, directed=False)
    assert set(g['SW1']) == {'PC1', 'PR1'}
    assert set(g['PR1']) == {'SW1', 'PC2'}
    d = degree_dict(g)
    assert d['SW1'] == 2 and d['PR1'] == 2 and d['PC2'] == 1

def test_directed_out_degree():
    edges = [('A','B'), ('B','C'), ('C','A')]
    g = build_graph(edges, directed=True)
    d = degree_dict(g)
    assert d['A'] == 1 and d['B'] == 1 and d['C'] == 1

def test_self_loop_counts_once_undirected():
    edges = [('X','X')]
    g = build_graph(edges, directed=False)
    assert g['X'] == ['X', 'X']  # both directions are the same node
    d = degree_dict(g)
    assert d['X'] == 2  # neighbor list has two entries

def test_empty_edges():
    g = build_graph([], directed=False)
    assert g == {}
    assert degree_dict(g) == {}

@pytest.mark.parametrize("directed", [False, True])
def test_multiple_edges_accumulate(directed):
    edges = [('A','B'), ('A','B'), ('B','A')]
    g = build_graph(edges, directed=directed)
    # We allow duplicates; sizes should reflect adds
    if directed:
        assert g['A'].count('B') == 2
    else:
        # Each ('A','B') adds A->B and B->A
        assert g['A'].count('B') == 3  # two from first two, one from ('B','A') undirected mirror

def test_degree_dict_matches_neighbor_lengths():
    edges = [('P','Q'), ('Q','R'), ('R','S'), ('S','P')]
    g = build_graph(edges, directed=False)
    d = degree_dict(g)
    for u in g:
        assert d[u] == len(g[u])

def test_isolated_nodes_not_forced():
    # No node appears unless present in edges
    g = build_graph([('A','B')], directed=False)
    assert 'Z' not in g

def test_chain_degrees():
    edges = [('N1','N2'), ('N2','N3'), ('N3','N4')]
    g = build_graph(edges, directed=False)
    d = degree_dict(g)
    assert d['N1'] == 1 and d['N4'] == 1 and d['N2'] == 2 and d['N3'] == 2

def test_directed_asymmetric_neighbors():
    edges = [('K','L'), ('L','M')]
    g = build_graph(edges, directed=True)
    assert g['K'] == ['L']
    assert g['L'] == ['M']
    assert g['M'] == []
