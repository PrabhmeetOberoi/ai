#########----BFS---###########
grap = {"A": ["B", "C"],
        "B": ["D", "E"],
        "C": ["F", "G"],
        "D": [],
        "E": [],
        "F": [],
        "G": []}
start = 'A'
goal = 'E'
open_list = []

def bfs(grap, goal):
    open_list.append(start)
    visited = {node: False for node in grap.keys()}
    visited[start] = True
    while len(open_list) > 0:
        current = open_list.pop(0)
        print(current + " ---> ", end="")
        if current == goal:
            print("found")
            break
        for neighbors in grap[current]:
            if not visited[neighbors]:
                visited[neighbors] = True
                open_list.append(neighbors)

bfs(grap, goal)

#########----DFS---###########
graph = {
    "A": ["B", "C"],
    "B": ["D", "E"],
    "C": ["F", "G"],
    "D": [],
    "E": [],
    "F": [],
    "G": []
}

start = 'A'
goal = 'E'
visited = {node: False for node in graph.keys()}

def dfs(node, visited, graph, goal):
    # Mark the current node as visited
    visited[node] = True
    print(node)

    # Check if the current node is the goal node
    if node == goal:
        print("Goal node found!")
        return True

    # Recur for all the vertices adjacent to this vertex
    for neighbor in graph[node]:
        if not visited[neighbor]:
            if dfs(neighbor, visited, graph, goal):
                return True

    return False

dfs(start, visited, graph, goal)

#########----UCS---###########
from queue import PriorityQueue

# define the graph as an adjacency matrix
graph = {
    'A': {'B': 9, 'C': 4},
    'B': {'C': 2, 'D': 7, 'E': 3},
    'C': {'D': 1, 'E': 6},
    'D': {'E': 4, 'F': 8},
    'E': {'F': 2},
    'F': {}
}


def ucs(start, goal):
    # initialize the open list with the start node and its cost
    open_list = PriorityQueue()
    open_list.put((0, start))
    # initialize the closed list
    closed_list = {}
    # initialize the cost and parent dictionaries
    cost = {start: 0}
    parent = {start: None}
    i = 0
    while not open_list.empty():
        # get the node with the lowest cost from the open list
        current_cost, current_node = open_list.get()
        # add the current node to the closed list
        closed_list[current_node] = current_cost
        # check if the goal node has been reached
        if current_node == goal:
            # reconstruct the path from the goal node to the start node
            path = []
            while current_node is not None:
                path.append(current_node)
                current_node = parent[current_node]
            path.reverse()
            return path, cost[goal]
        # expand the current node
        for neighbor, neighbor_cost in graph[current_node].items():
            # compute the cost of reaching the neighbor node from the current node
            tentative_cost = current_cost + neighbor_cost
            # check if the neighbor node is already in the closed list
            if neighbor in closed_list:
                continue
            # check if the neighbor node is already in the open list
            if neighbor in cost and tentative_cost >= cost[neighbor]:
                continue
            # add the neighbor node to the open list with its cost
            open_list.put((tentative_cost, neighbor))
            # update the cost and parent dictionaries
            cost[neighbor] = tentative_cost
            parent[neighbor] = current_node
            i += 1

            # print the current state of the algorithm
            print('--- Iteration', i, '---')
            print('Open List:', list(open_list.queue))
            print('Closed List:', closed_list)
            print('-----------------')
    # if the goal node cannot be reached, return None
    return None


path, cost = ucs('A', 'F')
print('Path:', path)
print('Cost:', cost)

#########----DFID---###########
tree = {'A': {
    'B': {
        'D': None,
        'E': None
    },
    'C': {
        'F': None,
        'G': None
    }
}}
q = list(tree.keys())
print(q)

goal = 'G'

def dfid(tree: dict, goal, current_depth, max_depth):
    q = list(tree.keys())
    #print(q)
    for node in q:
        print(node, "-> ", end="")
        if node == goal:
            print("Found")
            return True

        if tree[node]!=None and current_depth<max_depth and dfid(tree[node].copy(), goal, current_depth+1, max_depth):
            return True
    return False

found = False
for i in range(0,4):
    print(f"Searching at depth {i} : ")
    found = dfid(tree, goal, 0, i)
    if found:
        break

#########----ASTAR---###########
def aStarAlgo(start_node, stop_node):
    open_set = set(start_node)
    closed_set = set()
    g = {}  # store distance from starting node
    parents = {}  # parents contains an adjacency map of all nodes
    # distance of starting node from itself is zero
    g[start_node] = 0
    # start_node is root node i.e it has no parent nodes
    # so start_node is set to its own parent node
    parents[start_node] = start_node
    while len(open_set) > 0:
        n = None
        # node with lowest f() is found
        for v in open_set:
            if n == None or g[v] + heuristic(v) < g[n] + heuristic(n):
                n = v
        if n == stop_node or Graph_nodes[n] == None:
            pass
        else:
            for (m, weight) in get_neighbors(n):
                # nodes 'm' not in first and last set are added to first
                # n is set its parent
                if m not in open_set and m not in closed_set:
                    open_set.add(m)
                    parents[m] = n
                    g[m] = g[n] + weight
                # for each node m,compare its distance from start i.e g(m) to the
                # from start through n node
                else:
                    if g[m] > g[n] + weight:
                        # update g(m)
                        g[m] = g[n] + weight
                        # change parent of m to n
                        parents[m] = n
                        # if m in closed set,remove and add to open
                        if m in closed_set:
                            closed_set.remove(m)
                            open_set.add(m)
        if n == None:
            print('Path does not exist!')
            return None

        # if the current node is the stop_node
        # then we begin reconstructin the path from it to the start_node
        if n == stop_node:
            path = []
            while parents[n] != n:
                path.append(n)
                n = parents[n]
            path.append(start_node)
            path.reverse()
            print('Path found: {}'.format(path))
            return path
        # remove n from the open_list, and add it to closed_list
        # because all of his neighbors were inspected
        open_set.remove(n)
        closed_set.add(n)
    print('Path does not exist!')
    return None


# define fuction to return neighbor and its distance
# from the passed node
def get_neighbors(v):
    if v in Graph_nodes:
        return Graph_nodes[v]
    else:
        return None


def heuristic(n):
    H_dist = {
        'A': 11,
        'B': 6,
        'C': 5,
        'D': 7,
        'E': 3,
        'F': 6,
        'G': 5,
        'H': 3,
        'I': 1,
        'J': 0
    }
    return H_dist[n]


# Describe your graph here
Graph_nodes = {
    'A': [('B', 6), ('F', 3)],
    'B': [('A', 6), ('C', 3), ('D', 2)],
    'C': [('B', 3), ('D', 1), ('E', 5)],
    'D': [('B', 2), ('C', 1), ('E', 8)],
    'E': [('C', 5), ('D', 8), ('I', 5), ('J', 5)],
    'F': [('A', 3), ('G', 1), ('H', 7)],
    'G': [('F', 1), ('I', 3)],
    'H': [('F', 7), ('I', 2)],
    'I': [('E', 5), ('G', 3), ('H', 2), ('J', 3)],
}

aStarAlgo('A', 'J')

#########----GENETICS---###########
import random

# Define the fitness function to evaluate the individuals


def fitness(individual):
    # In this example, the fitness function simply counts the number of 1s in the binary string
    return sum(individual)

# Define the genetic algorithm function


def genetic_algorithm(population_size, chromosome_size, generations, mutation_rate):
    # Initialize the population with random individuals
    population = [[random.randint(0, 1) for j in range(
        chromosome_size)] for i in range(population_size)]
    for generation in range(generations):
        # Evaluate the fitness of each individual in the population
        fitness_scores = [fitness(individual) for individual in population]
        # Select the best individuals to be the parents of the next generation
        parents = []
        for i in range(population_size // 2):
            parent1 = population[fitness_scores.index(max(fitness_scores))]
            fitness_scores[fitness_scores.index(max(fitness_scores))] = -1
            parent2 = population[fitness_scores.index(max(fitness_scores))]
            fitness_scores[fitness_scores.index(max(fitness_scores))] = -1
            parents.append((parent1, parent2))
        # Create the next generation by recombining the parents' chromosomes and mutating them
        population = []
        for parent1, parent2 in parents:
            child1, child2 = parent1[:], parent2[:]
            for i in range(chromosome_size):
                if random.random() < mutation_rate:
                    child1[i] = 1 - child1[i]
                if random.random() < mutation_rate:
                    child2[i] = 1 - child2[i]
            population.append(child1)
            population.append(child2)
    # Return the fittest individual from the final population
    fitness_scores = [fitness(individual) for individual in population]
    return population[fitness_scores.index(max(fitness_scores))]


# Example usage:
fittest_individual = genetic_algorithm(
    population_size=100, chromosome_size=10, generations=50, mutation_rate=0.01)
print("Fittest individual:", fittest_individual)


#########----HILL CLIMBING ---###########
import numpy as np


def find_neighbours(state, landscape):
    neighbours = []
    dim = landscape.shape

    # left neighbour
    if state[0] != 0:
        neighbours.append((state[0] - 1, state[1]))

    # right neighbour
    if state[0] != dim[0] - 1:
        neighbours.append((state[0] + 1, state[1]))

    # top neighbour
    if state[1] != 0:
        neighbours.append((state[0], state[1] - 1))

    # bottom neighbour
    if state[1] != dim[1] - 1:
        neighbours.append((state[0], state[1] + 1))

    # top left
    if state[0] != 0 and state[1] != 0:
        neighbours.append((state[0] - 1, state[1] - 1))

    # bottom left
    if state[0] != 0 and state[1] != dim[1] - 1:
        neighbours.append((state[0] - 1, state[1] + 1))

    # top right
    if state[0] != dim[0] - 1 and state[1] != 0:
        neighbours.append((state[0] + 1, state[1] - 1))

    # bottom right
    if state[0] != dim[0] - 1 and state[1] != dim[1] - 1:
        neighbours.append((state[0] + 1, state[1] + 1))

    return neighbours


# Current optimization objective: local/global maximum
def hill_climb(curr_state, landscape):
    neighbours = find_neighbours(curr_state, landscape)
    bool
    ascended = False
    next_state = curr_state
    for neighbour in neighbours:  # Find the neighbour with the greatest value
        if landscape[neighbour[0]][neighbour[1]] > landscape[next_state[0]][next_state[1]]:
            next_state = neighbour
            ascended = True

    return ascended, next_state


def __main__():
    landscape = np.random.randint(1, high=50, size=(10, 10))
    print(landscape)
    start_state = (3, 6)  # matrix index coordinates
    current_state = start_state
    count = 1
    ascending = True
    while ascending:
        print("\nStep #", count)
        print("Current state coordinates: ", current_state)
        print("Current state value: ",
              landscape[current_state[0]][current_state[1]])
        count += 1
        ascending, current_state = hill_climb(current_state, landscape)

    print("\nStep #", count)
    print("Optimization objective reached.")
    print("Final state coordinates: ", current_state)
    print("Final state value: ", landscape[current_state[0]][current_state[1]])


__main__()


#########----SIM A ---###########
import random
import math

# Define the objective function


def objective_function(x):
    return x**2

# Define the simulated annealing algorithm function


def simulated_annealing(initial_state, objective_function, max_iterations, max_temperature):
    current_state = initial_state
    current_energy = objective_function(current_state)
    best_state = current_state
    best_energy = current_energy
    temperature = max_temperature

    for i in range(max_iterations):
        # Calculate the acceptance probability
        temperature = temperature * 0.9
        neighbor = current_state + random.uniform(-1, 1)
        neighbor_energy = objective_function(neighbor)
        delta_energy = neighbor_energy - current_energy
        acceptance_probability = math.exp(-delta_energy / temperature)

        # Determine whether to accept the new state
        if delta_energy < 0:
            current_state = neighbor
            current_energy = neighbor_energy
            if current_energy < best_energy:
                best_state = current_state
                best_energy = current_energy
        elif random.uniform(0, 1) < acceptance_probability:
            current_state = neighbor
            current_energy = neighbor_energy

        # Print the current state, energy, and temperature
        print(
            f"Iteration {i}: State = {current_state}, Energy = {current_energy}, Temperature = {temperature}")

    return best_state, best_energy


# Test the algorithm
initial_state = 10
max_iterations = 100
max_temperature = 1000
best_state, best_energy = simulated_annealing(
    initial_state, objective_function, max_iterations, max_temperature)

print(f"\nBest state found: {best_state}")
print(f"Best energy found: {best_energy}")


