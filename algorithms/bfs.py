'''
Traverse the nodes in a DIRECTED graph in a breadth-first fashion.

    0
   / \
   1  2
  / \   \
 3  4    5
          \
          6   (assume theres edge from 6 to 2).

Output: [0, 1, 2, 3, 4, 5, 6]
'''

from collections import deque, defaultdict

class Graph():
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, a, b):
        self.graph[a].append(b)

def bfs(G, start_node):
    q = deque([start_node])
    visited = set()
    res = []

    while q:
        node = q.popleft()
        if node not in visited:
            # add node to output.
            res.append(node)
            # visit the children and add them to q.
            for c in G[node]:
                q.append(c)
            # mark the node as visited.
            visited.add(node)

    return res

if __name__ == '__main__':
    G = Graph()
    G.add_edge(0, 1)
    G.add_edge(0, 2)
    G.add_edge(1, 3)
    G.add_edge(1, 4)
    G.add_edge(2, 5)
    G.add_edge(5, 6)
    G.add_edge(6, 2)

    print(bfs(G.graph, 0))