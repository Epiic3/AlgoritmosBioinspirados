import random

def immune_algorithm(initial_population, evaluate, mutation_rate, clone_rate, generations):
    population = initial_population

    for _ in range(generations):
        # Selección de clones
        clones = [(solution, evaluate(solution)) for solution in population]
        clones.sort(key=lambda x: x[1], reverse=True)
        selected_clones = clones[:int(len(clones) * clone_rate)]

        # Clonación y mutación
        mutated_clones = []
        for solution, _ in selected_clones:
            num_clones = int(1 + clone_rate * len(population))
            for _ in range(num_clones):
                mutated_solution = mutate(solution, mutation_rate)
                mutated_clones.append((mutated_solution, evaluate(mutated_solution)))

        # Selección de la próxima generación
        population = [solution for solution, _ in sorted(mutated_clones, key=lambda x: x[1], reverse=True)[:len(population)]]

    best_solution = max(population, key=evaluate)
    best_fitness = evaluate(best_solution)

    return best_solution, best_fitness

def mutate(solution, mutation_rate):
    mutated_solution = []
    for gene in solution:
        if random.random() < mutation_rate:
            mutated_solution.append(random.randint(0, 1))  # Ejemplo de mutación binaria
        else:
            mutated_solution.append(gene)
    return mutated_solution

# Ejemplo de uso
# Definir la función de evaluación
def evaluate(solution):
    return sum(solution)  # Ejemplo de función objetivo

# Definir la población inicial
initial_population = [[random.randint(0, 5) for _ in range(10)] for _ in range(100)]

# Ejecutar el algoritmo
best_solution, best_fitness = immune_algorithm(initial_population, evaluate, mutation_rate=0.1, clone_rate=0.2, generations=100)

print("Mejor solución encontrada:", best_solution)
print("Fitness de la mejor solución:", best_fitness)