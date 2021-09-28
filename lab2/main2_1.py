class Graph:
    graph = {}

    def __init__(self, start_v, end_v):
        self.start = start_v  # start vertex
        self.end = end_v  # end vertex
        self.path = start_v  # path

    def add_edge(self, source, dist, weight):
        # if source vertex hasn't in graph than create this vertex otherwise add new edge to this vertex
        if source in self.graph.keys():
            self.graph[source].append([dist, float(weight)])
        else:
            self.graph[source] = [[dist, float(weight)]]

    def sort_edge(self):

        print('--- Sorting edges ---')
        for vertex in self.graph:
            print(f'Vertex {vertex} sorting')
            print('Before sorting:')
            for item in self.graph[vertex]:
                print(f'{vertex} -> {item[0]} = {item[1]}')
            self.graph[vertex] = sorted(self.graph[vertex], key=lambda k: k[1])  # sorting edges by weight
            print('After Sorting:')
            for item in self.graph[vertex]:
                print(f'{vertex} -> {item[0]} = {item[1]}')
        print('\n')

    def print_path(self):
        print('Result: ', self.path)

    def draw_path(self):

        while self.path[-1] != self.end:
            start_vertex = self.graph[self.start]
            print(f"For vertex '{self.start}' there is edges:")
            for vertex in start_vertex:
                print(f"{vertex[0]} with weight: {vertex[1]}")
            i = -1
            for edges in start_vertex:

                i += 1
                if i == len(start_vertex) - 1 and len(edges) == 3:
                    self.path = self.path[0: -1]
                    self.start = self.path[-1]
                    print(f" Path changed. Current path: {self.path}")
                    break
                if len(edges) == 3:
                    continue

                print(f"Go to '{edges[0]}'")
                self.graph[self.start][i].append(1)  # add 1 as this vertex was visited
                if edges[0] == self.end:  # if current vertex equal end vertex then path was found. break logo
                    print(f"Next vertex '{edges[0]}' equals to end vertex. Path was found")
                    self.path += edges[0]
                    break
                if edges[0] not in self.graph.keys():  # if current vertex haven't edges then break algo
                    print(f"Vertex '{edges[0]}' haven't edges. Algorithm was returned to the previous step")
                    break
                # add new vertex to path
                self.path += edges[0]
                self.start = edges[0]
                print(f"Vertex '{edges[0]} was writed to the path. Current path: {self.path}")
                print('\n')
                break


start, end = input().split(' ')

graph = Graph(start, end)  # create graph

while True:
    try:
        edge = input()
        if len(edge) == 0:
            break
    except EOFError:  # end of line error exception
        break
    edge = edge.split(' ')
    graph.add_edge(edge[0], edge[1], edge[2])  # add edges to graph

# sorting edge
graph.sort_edge()

# found path
graph.draw_path()

# print path
graph.print_path()
