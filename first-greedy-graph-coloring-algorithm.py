import networkx as nx
import matplotlib.pyplot as plt

def greedy_coloring(graph):
    """
    Функция для раскраски графа с использованием жадного алгоритма
    """
    coloring = {}
    for node in graph.nodes():
        available_colors = set(range(len(graph.nodes())))
        for neighbor in graph.neighbors(node):
            if neighbor in coloring:
                available_colors.discard(coloring[neighbor])
        coloring[node] = min(available_colors)
    return coloring

# Генерация случайного графа с заданным количеством узлов и вероятностью ребра
def generate_random_graph(num_nodes, edge_prob):
    graph = nx.erdos_renyi_graph(num_nodes, edge_prob)
    return graph

# Визуализация раскраски графа
def visualize_graph(graph, coloring):
    plt.figure(figsize=(12, 8))
    pos = nx.spring_layout(graph)
    colors = [coloring[node] for node in graph.nodes()]
    nx.draw(graph, pos, node_color=colors, with_labels=True, node_size=500, font_color='white', cmap=plt.cm.tab20)
    plt.show()

if __name__ == "__main__":
    num_nodes = 20
    edge_prob = 0.2

    random_graph = generate_random_graph(num_nodes, edge_prob)
    graph_coloring = greedy_coloring(random_graph)

    visualize_graph(random_graph, graph_coloring)
