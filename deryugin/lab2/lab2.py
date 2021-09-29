import math


def sort_edges(vertexes, end):
    print('--- Sorting edges---')

    for vertex in vertexes:
        if not vertexes[vertex]:
            print(f'Vertex "{vertex}" has not edges')
            continue
        print(f'Sorting vertex "{vertex}"')
        print('Before sorting')
        for edges in vertexes[vertex]:
            print(f"{vertex} -> {edges[0]} = {edges[1]}")
            # sorting edges
        vertexes[vertex] = sorted(vertexes[vertex], key=lambda item: abs(ord(item[0]) - ord(end)) + item[1])
        print('After sorting')
        for edges in vertexes[vertex]:
            print(f"{vertex} -> {edges[0]} = {edges[1]}")


def h(vertex, end):
    # found Heuristic estimate of vertex to end vertex
    return abs(ord(vertex) - ord(end))


def min_f(opened, f):
    # found values of Heuristic function
    minimum = [math.inf, None]
    for vertex in opened:
        if f[vertex] < minimum[0]:
            minimum = [f[vertex], vertex]
    return minimum[1]


def a_star(start, end, vertexes):
    fromed = {}  # found paths
    closed = []  # closed queue
    opened = [start]  # opened queue
    # costs of path from start vertex to current vertex
    g = {
        start: [0, None]
    }
    # values of Heuristic function
    f = {
        start: g[start][0] + h(start, end)
    }

    while opened:
        print(f'Opened queue: ')
        for item in opened:
            print(item, end=' ')
        print('\n')
        # found minimum value of Heuristic function between vertexes in opened queue
        current = min_f(opened, f)
        if current == end:
            print(f'Path was found')
            break
        # remove from opened queue and add to closed queue
        opened.remove(current)
        closed.append(current)
        print(f'Remove vertex {current} from opened queue')
        # if vertex hasn't edges
        if current not in vertexes:
            print(f'Vertex "{current}" has not edges')
            continue
        # iterating over neighbors of current vertex
        for neighbor in vertexes[current]:
            print(f'Looking path {current} -> {neighbor[0]} = {neighbor[1]}')
            # found costs of price to neighbor
            temp_g = g[current][0] + neighbor[1]
            print(f'Path(g) to vertex {neighbor[0]} equals {temp_g}')
            if neighbor[0] in closed and temp_g >= g[neighbor[0]][0]:
                print(f'Vertex {neighbor[0]} was already visited from other vertex')
                continue
            # add new vertex to g(x) and f(x) functions
            if neighbor[0] not in closed or temp_g < g[neighbor[0]][0]:
                fromed[neighbor[0]] = current
                g[neighbor[0]] = [temp_g, current]
                print(f'Add vertex {neighbor[0]} with g = {temp_g} to weight of paths g(x) ')
                f[neighbor[0]] = g[neighbor[0]][0] + h(neighbor[0], end)
                print(f'Heuristic of vertex {neighbor[0]} is {f[neighbor[0]]}')
            # add vertex to opened queue
            if neighbor[0] not in opened:
                print(f"Add vertex {neighbor[0]} to opened queue")
                opened.append(neighbor[0])

    vertex = fromed[end]
    path = end + vertex
    # print result
    while vertex != start:
        vertex = fromed[vertex]
        path += vertex
    print(path[::-1])


def main():
    start, end = input().split(' ')

    # dict of vertexes
    vertexes = {
        start: [],
        end: []
    }

    while True:
        try:
            edge = input()
            if len(edge) == 0:
                break
        except EOFError: # end of line error exception
            break
        edge = edge.split(' ')
        if edge[0] in vertexes:
            vertexes[edge[0]].append([edge[1], float(edge[2])])
        else:
            vertexes[edge[0]] = [[edge[1], float(edge[2])]]
    sort_edges(vertexes, end)

    a_star(start, end, vertexes)


main()
