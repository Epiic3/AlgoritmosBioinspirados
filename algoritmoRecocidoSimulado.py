import math
import random

def simulated_annealing(initial_solution, evaluate, neighbor, temperature, cooling_schedule, max_iterations):
    current_solution = initial_solution
    current_energy = evaluate(current_solution)

    for i in range(max_iterations):
        T = cooling_schedule(i)
        if T == 0:
            break

        neighbor_solution = neighbor(current_solution)
        neighbor_energy = evaluate(neighbor_solution)

        energy_delta = neighbor_energy - current_energy

        if energy_delta < 0 or random.random() < math.exp(-energy_delta / T):
            current_solution = neighbor_solution
            current_energy = neighbor_energy

    return current_solution, current_energy

# Ejemplo de uso
# Definir la función de evaluación
def evaluate(solution):
    return sum(solution)  # ejemplo de función objetivo

# Definir la función vecina
def neighbor(solution):
    neighbor_solution = solution.copy()
    idx = random.randint(0, len(neighbor_solution) - 1)
    neighbor_solution[idx] = random.randint(0, 100)  # ejemplo de vecindad aleatoria
    return neighbor_solution

# Definir el esquema de enfriamiento
def cooling_schedule(iteration):
    return 100 / (1 + iteration)  # enfriamiento lineal

# Definir la solución inicial
initial_solution = [random.randint(0, 100) for _ in range(10)]

# Ejecutar el algoritmo
best_solution, best_energy = simulated_annealing(initial_solution, evaluate, neighbor, temperature=100, cooling_schedule=cooling_schedule, max_iterations=1000)

print("Mejor solución encontrada:", best_solution)
print("Energía de la mejor solución:", best_energy)
