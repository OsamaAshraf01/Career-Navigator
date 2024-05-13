import matplotlib.pyplot as plt
import networkx as nx
import pandas as pd


def wrap(txt: str) -> str:
    if len(txt) > 20:
        return txt[0:21] + '...  '
    return txt + '  '


def calc_betweenness(edges: list[tuple], main_nodes: list = [], exclude: list = []) -> pd.Series:
    # Prepare Graph
    G = nx.Graph()  # Graph for drawing
    G_with_exclude = nx.Graph()  # Graph for calculate betweenness

    # Add Edges
    G.add_edges_from(edges)
    G_with_exclude.add_edges_from([edge for edge in edges if edge[0] not in exclude and edge[
        1] not in exclude])  # Exclude some nodes before continue

    # Claculate Betweenness and Degree
    betweenness = {k: v * 100 for k, v in nx.betweenness_centrality(G_with_exclude).items()}  # , normalized=False)
    degree = dict(G.degree)

    # Filter betweennes from main nodes
    filtered_betweenness = {wrap(k): round(v, 2) for k, v in betweenness.items() if k not in main_nodes}
    filtered_betweenness = pd.Series(filtered_betweenness).sort_values(ascending=False)  # Sort Descendingly
    try:
        filtered_betweenness = filtered_betweenness[:50]
    except:
        pass  # Don't crop

    filtered_betweenness = filtered_betweenness.sort_values(
        ascending=True)  # Sort Ascendingly to be rversed in the plot

    return filtered_betweenness


def generate_network(titles_nodes, skills_nodes, edges):
    all_nodes = [('skill', skill) for skill in skills_nodes] + [('title', title) for title in titles_nodes]

    graph_nodes = [
        {
            'data': {'id': label, 'label': label},
            # 'size': 7000 if Type=='title' else 1000,
            'classes': 'title' if (Type == 'title') else 'skill'
        }
        for Type, label in all_nodes
    ]
    graph_edges = [
        {
            'data': {'source': source, 'target': target},
            'classes': 'edge'
        }
        for source, target in edges
    ]
    Graph_elements = graph_nodes + graph_edges
    
    print("Rendering Network has finished !")

    return Graph_elements


# if __name__ == "__main__":
#     edges = [
#         ('A', 'A1'),
#         ('A', 'A2'),
#         ('A', 'A3'),
#         ('A', 'A4'),
#         ('A', 'A5'),
#         ('A', 'A6'),

#         ('B', 'A1'),
#         ('B', 'B2'),
#         ('B', 'B3'),

#         ('C', 'A2'),
#         ('C', 'A3'),
#         ('C', 'B2'),
#         ('C', 'C1'),
#         ('C', 'C2'),
#         ('C', 'C3'),
#     ]

#     MAIN = ['A', 'B', 'C']

#     filtered = calc_betweenness(edges, main_nodes=MAIN)  # , exclude=['A1', 'A2'])
#     print(filtered.sort_values(ascending=False).head(50))

#     plt.show()

#     # ! Filter Nodes with Zero centrality
#     # filtered_edges = []
#     # filtered_degree = {}
#     # for key in degree:
#     #     if betweenness[key] != 0:
#     #         if key not in MAIN:
#     #             filtered_degree[key] = 10
#     #         else:
#     #             filtered_degree[key] = 100

#     # G2 = nx.Graph()
#     # for edge in edges:
#     #     if betweenness[edge[0]] != 0 and betweenness[edge[1]] != 0:
#     #         filtered_edges.append(edge)

#     # G2.add_edges_from(filtered_edges)
