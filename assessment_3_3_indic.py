"""
Assessment 3.3: Non-Linear Data Structure
Last name: INDIC

Builds a binary tree and a graph from the letters of the last name,
then prints the BFS and DFS traversal order of each.

Run:  python assessment_3_3_indic.py
"""
from collections import deque

LETTERS = ['I1', 'N', 'D', 'I2', 'C']   # the two I's are separate nodes: I1 and I2


# ---------------------------------------------------------------- Binary tree
class Node:
    def __init__(self, label):
        self.label = label
        self.left = None
        self.right = None


def build_tree(labels):
    """Fill the tree level by level, left to right (level-order)."""
    nodes = [Node(x) for x in labels]
    for i, node in enumerate(nodes):
        left, right = 2 * i + 1, 2 * i + 2
        if left < len(nodes):
            node.left = nodes[left]
        if right < len(nodes):
            node.right = nodes[right]
    return nodes[0]


def tree_bfs(root):
    """Visit level by level using a queue."""
    order, queue = [], deque([root])
    while queue:
        node = queue.popleft()
        order.append(node.label)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    return order


def tree_dfs(node, order=None):
    """Go deep first (preorder: node, left, right) using recursion."""
    if order is None:
        order = []
    if node is None:
        return order
    order.append(node.label)
    tree_dfs(node.left, order)
    tree_dfs(node.right, order)
    return order


# ---------------------------------------------------------------------- Graph
EDGES = [('I1', 'N'), ('I1', 'D'), ('N', 'I2'), ('D', 'C'), ('I2', 'C')]


def build_graph(labels, edges):
    """Adjacency list; neighbors kept in the order the letters appear in the name."""
    adj = {x: [] for x in labels}
    for a, b in edges:
        adj[a].append(b)
        adj[b].append(a)
    position = {x: i for i, x in enumerate(labels)}
    for x in adj:
        adj[x].sort(key=lambda y: position[y])
    return adj


def graph_bfs(adj, start):
    """Visit nearest vertices first using a queue and a visited set."""
    visited, order, queue = {start}, [], deque([start])
    while queue:
        v = queue.popleft()
        order.append(v)
        for w in adj[v]:
            if w not in visited:
                visited.add(w)
                queue.append(w)
    return order


def graph_dfs(adj, v, visited=None, order=None):
    """Go as deep as possible, then backtrack (recursion + visited set)."""
    if visited is None:
        visited, order = set(), []
    visited.add(v)
    order.append(v)
    for w in adj[v]:
        if w not in visited:
            graph_dfs(adj, w, visited, order)
    return order


if __name__ == "__main__":
    root = build_tree(LETTERS)
    print("Last name:", "INDIC")
    print("Binary Tree BFS:", " - ".join(tree_bfs(root)))
    print("Binary Tree DFS:", " - ".join(tree_dfs(root)))

    graph = build_graph(LETTERS, EDGES)
    print("Graph BFS      :", " - ".join(graph_bfs(graph, LETTERS[0])))
    print("Graph DFS      :", " - ".join(graph_dfs(graph, LETTERS[0])))
