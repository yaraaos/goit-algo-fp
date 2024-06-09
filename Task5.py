import uuid
import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.colors import to_hex
from matplotlib import cm
import numpy as np


class Node:
    def __init__(self, key, color="skyblue"):
        self.left = None
        self.right = None
        self.val = key
        self.color = color  # Додатковий аргумент для зберігання кольору вузла
        self.id = str(uuid.uuid4())  # Унікальний ідентифікатор для кожного вузла


def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node is not None:
        graph.add_node(node.id, color=node.color, label=node.val)  # Використання id та збереження значення вузла
        if node.left:
            graph.add_edge(node.id, node.left.id)
            l = x - 1 / 2 ** layer
            pos[node.left.id] = (l, y - 1)
            l = add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            r = x + 1 / 2 ** layer
            pos[node.right.id] = (r, y - 1)
            r = add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)
    return graph


def draw_tree(tree_root, highlight_nodes=None):
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    tree = add_edges(tree, tree_root, pos)

    colors = [node[1]['color'] for node in tree.nodes(data=True)]
    labels = {node[0]: node[1]['label'] for node in tree.nodes(data=True)}

    plt.figure(figsize=(8, 5))
    nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors)
    
    if highlight_nodes:
        highlight_colors = [highlight_nodes.get(node, node_data['color']) for node, node_data in tree.nodes(data=True)]
        nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=highlight_colors)
    
    plt.show()


def generate_colors(num_colors):
    colors = cm.viridis(np.linspace(0, 1, num_colors))
    hex_colors = [to_hex(c) for c in colors]
    return hex_colors


def bfs(root):
    queue = [root]
    order = []
    while queue:
        node = queue.pop(0)
        order.append(node)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    return order


def dfs(root):
    stack = [root]
    order = []
    while stack:
        node = stack.pop()
        order.append(node)
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)
    return order


def visualize_traversal(root, traversal_func):
    order = traversal_func(root)
    colors = generate_colors(len(order))
    highlight_nodes = {node.id: color for node, color in zip(order, colors)}
    draw_tree(root, highlight_nodes)


# Створення дерева
root = Node(0)
root.left = Node(4)
root.left.left = Node(5)
root.left.right = Node(10)
root.right = Node(1)
root.right.left = Node(3)

# Відображення обходу в ширину
visualize_traversal(root, bfs)

# Відображення обходу в глибину
visualize_traversal(root, dfs)
