def bellman_ford(graph, source):
    # Step 1: Initialize distances and predecessors
    distances = {vertex: float('inf') for vertex in graph}
    distances[source] = 0
    predecessors = {vertex: None for vertex in graph}

    # Step 2: Relax edges repeatedly
    for _ in range(len(graph) - 1):
        for u in graph:
            for v, weight in graph[u]:
                if distances[u] + weight < distances[v]:
                    distances[v] = distances[u] + weight
                    predecessors[v] = u

    # Step 3: Check for negative cycles
    for u in graph:
        for v, weight in graph[u]:
            if distances[u] + weight < distances[v]:
                raise ValueError("Graph contains a negative cycle")

    return distances, predecessors

def djikastra(graph, source):
    # Step 1: Initialize distances and predecessors
    distances = {vertex: float('inf') for vertex in graph}
    distances[source] = 0
    predecessors = {vertex: None for vertex in graph}

    # Step 2: Relax edges repeatedly
    for _ in range(len(graph) - 1):
        for u in graph:
            for v, weight in graph[u]:
                if distances[u] + weight < distances[v]:
                    distances[v] = distances[u] + weight
                    predecessors[v] = u

    return distances, predecessors



def main():
    pass

if __name__ == '__main__':
    main()

