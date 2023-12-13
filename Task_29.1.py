from collections import defaultdict


class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def dfs(self, v, visited, stack):
        visited[v] = True
        for i in self.graph[v]:
            if not visited[i]:
                self.dfs(i, visited, stack)
        stack.append(v)

    def get_transpose(self):
        g = Graph(self.V)
        for i in self.graph:
            for j in self.graph[i]:
                g.add_edge(j, i)
        return g

    def fill_order(self, v, visited, stack):
        visited[v] = True
        for i in self.graph[v]:
            if not visited[i]:
                self.fill_order(i, visited, stack)
        stack.append(v)

    def print_scc(self):
        stack = []
        visited = [False] * (self.V)

        for i in range(self.V):
            if not visited[i]:
                self.dfs(i, visited, stack)

        gr = self.get_transpose()

        visited = [False] * (self.V)

        result = []
        while stack:
            i = stack.pop()
            if not visited[i]:
                temp_stack = []
                gr.fill_order(i, visited, temp_stack)
                result.append(temp_stack)

        return result


# Example usage:
g = Graph(5)
g.add_edge(0, 1)
g.add_edge(1, 2)
g.add_edge(2, 0)
g.add_edge(1, 3)
g.add_edge(3, 4)

print("Strongly Connected Components:")
print(g.print_scc())
