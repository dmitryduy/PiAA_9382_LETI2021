import math


class Vertex:
    visited = False  # visited or not
    vertex_from = [None, 0]  # from vertex vertex_from[0] with weight vertex_from[1]

    def __init__(self, name):
        self.name = name
        self.edges = {}  # list of neighbours


class Graph:
    vertexes = {}  # dict of vertexes
    source = None
    sunk = None
    flow = 0

    def add_edge(self, name_from, name_to, weight):
        if name_from in self.vertexes.keys():

            self.vertexes[name_from].edges[name_to] = [weight, 0, 1]
        else:

            self.vertexes[name_from] = Vertex(name_from)
            self.vertexes[name_from].edges[name_to] = [weight, 0, 1]
        if name_to in self.vertexes.keys():

            self.vertexes[name_to].edges[name_from] = [0, 0, -1]
        else:

            self.vertexes[name_to] = Vertex(name_to)
            self.vertexes[name_to].edges[name_from] = [0, 0, -1]


# sorted vertex by alphabetic order
def filter_vertexes(vertexes):
    l = list(vertexes.keys())
    l.sort()
    new_v = []
    for item in l:
        new_v.append(vertexes[item])
    return new_v


# found minimum flow on path
def found_min(visited_vertexes, graph):
    minimum = math.inf
    minimum_vertex = 'z'
    previous_vertex = None
    weight = 0
    for visit_vertex in visited_vertexes:
        print(f'Looking vertex {visit_vertex} with edges:')
        for name, edge in graph.vertexes[visit_vertex].edges.items():
            print(f'{visit_vertex} -> {name} = {edge[0]}')
        for name, edge in graph.vertexes[visit_vertex].edges.items():
            print(f'Looking edge: {visit_vertex} -> {name} = {edge[0]}')
            if graph.vertexes[name].visited:
                print(f'Vertex {name} has been already visited. Choosing other edge')
                continue
            if (abs(ord(visit_vertex) - ord(name)) < minimum or abs(
                    ord(visit_vertex) - ord(name)) == minimum and minimum_vertex > name) and edge[0] > 0:
                print(f'Found new minimum by alphabetic order edge: {visit_vertex} -> {name} = {edge[0]}')
                previous_vertex = visit_vertex
                minimum = abs(ord(visit_vertex) - ord(name))
                minimum_vertex = name
                weight = edge[0]
    if minimum == math.inf:
        return False
    return [previous_vertex, minimum_vertex, weight]


def start_algorithm(graph):
    visited_vertexes = [graph.source]
    graph.vertexes[graph.source].visited = True
    current_vertex = graph.source

    while current_vertex != graph.sunk:
        print('Array of visited vertexes:')
        for vertex in visited_vertexes:
            print(vertex, end=' ')
        print('\n')
        edge = found_min(visited_vertexes, graph)


        if not edge:
            return False
        print('New choosing vertex: ', edge[1])
        visited_vertexes.append(edge[1])
        graph.vertexes[edge[1]].visited = True
        graph.vertexes[edge[1]].vertex_from = [edge[0], edge[2]]
        current_vertex = edge[1]
    return True


def find_min_flow(graph):
    min = graph.vertexes[graph.sunk].vertex_from[1]
    current_vertex = graph.sunk
    while graph.vertexes[current_vertex].vertex_from[0]:
        if min > graph.vertexes[current_vertex].vertex_from[1]:
            min = graph.vertexes[current_vertex].vertex_from[1]
        current_vertex = graph.vertexes[current_vertex].vertex_from[0]
    return min


def remove_path(graph, minimum):
    current_vertex = graph.vertexes[graph.sunk].vertex_from[0]
    previous_vertex = graph.sunk
    path = graph.sunk
    print('Counting max flow on current path')
    while graph.vertexes[current_vertex].vertex_from[0]:
        path += current_vertex
        print(
            f'Previous weight of edge {previous_vertex} -> {current_vertex} was \
{graph.vertexes[current_vertex].edges[previous_vertex][0]}. New weight - \
{graph.vertexes[current_vertex].edges[previous_vertex][0] - minimum}')
        graph.vertexes[current_vertex].edges[previous_vertex][0] -= minimum
        graph.vertexes[current_vertex].edges[previous_vertex][1] += minimum

        graph.vertexes[previous_vertex].edges[current_vertex][0] += minimum
        graph.vertexes[previous_vertex].edges[current_vertex][1] -= minimum

        previous_vertex = current_vertex
        current_vertex = graph.vertexes[current_vertex].vertex_from[0]

    path += current_vertex
    print(f'Previous weight of edge {previous_vertex} -> {current_vertex} was \
{graph.vertexes[current_vertex].edges[previous_vertex][0]}. New weight - \
{graph.vertexes[current_vertex].edges[previous_vertex][0] - minimum}')
    graph.vertexes[current_vertex].edges[previous_vertex][0] -= minimum
    graph.vertexes[current_vertex].edges[previous_vertex][1] += minimum
    print('Current path:')
    print(path[::-1])


def print_result(graph):
    for vertex in graph.vertexes:
        for name, edge in graph.vertexes[vertex].edges.items():
            print(f'{vertex} {name} {edge[1]}') if edge[1] >= 0 and edge[2] != -1 else None


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

    while start_algorithm(graph):
        minimum_flow = find_min_flow(graph)
        graph.flow += minimum_flow
        remove_path(graph, minimum_flow)

        for vertex in graph.vertexes:
            graph.vertexes[vertex].vertex_from = [None, 0]
            graph.vertexes[vertex].visited = False
    print(graph.flow)
    print_result(graph)


main()
