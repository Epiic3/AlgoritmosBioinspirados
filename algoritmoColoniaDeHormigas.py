import networkx as nx
import random

def add_pheromone(trails, ants, graph):
    evaporation = 0.5
    for i, row in enumerate(trails):
        for j, col in enumerate(row):
            trails[i][j] *= evaporation
            for ant in ants:
                if j == ant[i + 1]:
                    trails[i][j] += (1.0 / ant[-1])

def ant_tour(graph, trails, alpha, beta):
    start = random.randint(0, len(graph.nodes()) - 1)
    ant = [start]
    visited = set()
    visited.add(start)
    while len(ant) < len(graph.nodes()):
        current = ant[-1]
        numerator = [trails[current][neighbor] ** alpha * ((1.0 / graph[current][neighbor]['weight']) ** beta) if neighbor not in visited else 0 for neighbor in graph.neighbors(current)]
        denominator = sum(numerator)
        probabilities = [val / denominator for val in numerator]
        next_node = random.choices(list(graph.neighbors(current)), probabilities)[0]
        ant.append(next_node)
        visited.add(next_node)
    return ant + [1.0 / sum([graph[ant[i]][ant[i + 1]]['weight'] for i in range(len(ant) - 1)])]

def ant_colony(graph, iterations, alpha, beta):
    trails = [[1.0] * len(graph.nodes()) for _ in range(len(graph.nodes()))]
    best_tour = None
    best_length = float('inf')
    for _ in range(iterations):
        ants = [ant_tour(graph, trails, alpha, beta) for _ in range(len(graph.nodes()))]
        for ant in ants:
            if ant[-1] < best_length:
                best_tour = ant[:-1]
                best_length = ant[-1]
        add_pheromone(trails, ants, graph)
    return best_tour, best_length

# Ejemplo de uso
# Crear un grafo aleatorio
graph = nx.complete_graph(5)
for (u, v, w) in graph.edges(data=True):
    w['weight'] = random.randint(1, 10)

best_tour, best_length = ant_colony(graph, iterations=100, alpha=1, beta=2)
print("Mejor recorrido encontrado:", best_tour)
print("Longitud del mejor recorrido:", best_length)
