class Vertex:

    def __init__(self, name):
        self.name = name
        self.edges = []


class Graph:
    vertexes = {}
    max_flow = 0
    flows = []
    visited_vertexes = []
    source = None
    sunk = None

    def add_edge(self, name_from, name_to, weight):
        if name_from in self.vertexes.keys():
            self.vertexes[name_from].edges.append([name_to, weight, 0, 1])
        else:
            self.vertexes[name_from] = Vertex(name_from)
            self.vertexes[name_from].edges.append([name_to, weight, 0, 1])
        if name_to in self.vertexes.keys():
            self.vertexes[name_to].edges.append([name_from, weight, 0, -1])
        else:
            self.vertexes[name_to] = Vertex(name_to)
            self.vertexes[name_to].edges.append([name_from, weight, 0, -1])


def find_min_flow(graph):
    print('--- Path was found---\n Path:')
    weights = []
    for edge in graph.flows:
        print(f'{edge[0]}->{edge[1]}[{edge[2]}; {edge[3]}]  ', end=' ')
        if edge[4] == 1:
            weights.append(edge[2])
        else:
            weights.append(edge[3])
    print(f'\n Minimum flow in this path: {min(weights)}')
    return min(weights)


def remove_path(graph, min):
    graph.visited_vertexes = []  # clear visited vertexes
    print('\n--- Updating flows---')
    for edge in graph.flows:

        if edge[4] == 1:
            for edge_inner in graph.vertexes[edge[0]].edges:
                if edge_inner[0] == edge[1] and edge_inner[3] == 1:
                    print(f'Old flow: {edge[0]}->{edge[1]} = [{edge[2]}, {edge[3]}]')
                    print(f'New flow: {edge[0]}->{edge[1]} = [{edge[2] - min}, {edge[3] + min}]\n')
                    edge_inner[1] -= min
                    edge_inner[2] += min
            for edge_inner_negative in graph.vertexes[edge[1]].edges:
                if edge_inner_negative[0] == edge[0] and edge_inner_negative[3] == -1:
                    edge_inner_negative[1] -= min
                    edge_inner_negative[2] += min

        if edge[4] == -1:
            for edge_inner in graph.vertexes[edge[0]].edges:
                if edge_inner[0] == edge[1] and edge_inner[3] == -1:
                    print(f'Old flow: {edge[0]}->{edge[1]} = [{edge[2]}, {edge[3]}]')
                    print(f'New flow: {edge[0]}->{edge[1]} = [{edge[2] + min}, {edge[3] - min}]\n')
                    edge_inner[1] += min
                    edge_inner[2] -= min
            for edge_inner_positive in graph.vertexes[edge[1]].edges:
                if edge_inner_positive[0] == edge[0] and edge_inner_positive[3] == 1:
                    edge_inner_positive[1] += min
                    edge_inner_positive[2] -= min
    graph.flows = []


def start_algorithm(graph, current_vertex):
    if current_vertex != graph.sunk:
        print(f'\nCurrent vertex: "{current_vertex}". Edges:')
        for edge in graph.vertexes[current_vertex].edges:
            if edge[3] == 1 and edge[1] != 0:
                print(f'{current_vertex} -> {edge[0]} = {edge[1]}')
            elif edge[3] == -1 and edge[2] != 0:
                print(f'{current_vertex} -> {edge[0]} = {edge[2] * -1}')

    for edge in graph.vertexes[current_vertex].edges:
        if edge[3] == 1:
            print(f'View path: {current_vertex}->{edge[0]} = {edge[1]}')
        elif edge[3] == -1:
            print(f'View path: {current_vertex}->{edge[0]} = {edge[2] * -1}')
        if current_vertex == graph.sunk:
            print('Sunk vertex found')
            minimum = find_min_flow(graph)  # find minimum flow in current step
            graph.max_flow += minimum  # add up previous flow and new flow
            remove_path(graph, minimum)  # clear path and recalculation flows
            return True
        if edge[1] > 0 and edge[3] == 1 and edge[0] not in graph.visited_vertexes \
                or edge[2] > 0 and edge[3] == -1 and edge[0] not in graph.visited_vertexes:
            print(f'Vertex "{edge[0]}" was added to path')
            graph.visited_vertexes.append(edge[0])  # add new vertex as visited
            graph.flows.append([current_vertex, edge[0], edge[1], edge[2], edge[3]])
            if start_algorithm(graph, edge[0]):
                return True
            graph.flows.pop()  # remove last vertex from path
        else:
            print('Current path not good\n')
    return False


def filter_vertexes(vertexes):
    print('--- Sorting vertexes---')
    for vertex in vertexes.values():
        if not vertex.edges:
            continue
        print(f'Sorting vertex {vertex.name}')
        print('Edges before sorting:')
        for edge in vertex.edges:
            if edge[3] == -1:
                continue
            print(f'{vertex.name} -> {edge[0]} = {edge[1]}', sep=' ')

        # sorting edges by alphabetic order
        vertex.edges = sorted(vertex.edges, key=lambda item: abs(ord(item[0]) - ord(vertex.name)))

        for edge in range(0, len(vertex.edges) - 1):
            if abs(ord(vertex.name) - ord(vertex.edges[edge][0])) == abs(
                    ord(vertex.name) - ord(vertex.edges[edge + 1][0])) and ord(vertex.edges[edge][0]) > ord(vertex.edges[edge + 1][0]):
                vertex.edges[edge + 1][0], vertex.edges[edge][0] = vertex.edges[edge][0], vertex.edges[edge + 1][0]

        print('Edges after sorting:')
        for edge in vertex.edges:
            if edge[3] == -1:
                continue
            print(f'{vertex.name} -> {edge[0]} = {edge[1]}', sep=' ')


def main():
    count_of_edges = int(input())  # count of edges
    graph = Graph()  # create graph
    graph.source = input()  # add source
    graph.sunk = input()  # add sunk

    # add edges to graph
    for _ in range(0, count_of_edges):
        name_from, name_to, weight = input().split(" ")
        graph.add_edge(name_from, name_to, int(weight))

    # filter vertexes
    filter_vertexes(graph.vertexes)

    graph.visited_vertexes.append(graph.source)  # add source as visited vertex

    while start_algorithm(graph, graph.source):
        graph.visited_vertexes.append(graph.source)

    print(graph.max_flow)
    edges = []
    for vertex in graph.vertexes.values():
        for edge in vertex.edges:
            if edge[3] == 1:
                edges.append([f"{vertex.name}{edge[0]}", edge[2]])

    sorted_edges = sorted(edges, key=lambda item: item[0])
    for edge in sorted_edges:
        print(edge[0][0], edge[0][1], edge[1])


main()
