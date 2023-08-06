# DarwinPy

 ## Introduction
DarwinPy is a Python-based evolutionary computation module that makes it easy to implement evolutionary methods such as genetic algorithms and evolutionary strategies with only a few lines of code.

## Installing DarwinPy
DarwinPy can be installed with the command `pip install DarwinPy`.

## Classes in DarwinPy
Genetics Classes (`DarwinPy.Genetics.Genetics`)

**Methods:**
* `setSearchSpace(search_space)`: Sets the `search_space` attribute of the DarwinPy object.
* `setChromosomeLength(chromosome_length)`: Sets the `chromosome_length` attribute of the DarwinPy object.
* `setPopulationSize(population_size)`: Sets the `population_size` attribute of the DarwinPy object.
* `setChromosomeMatrix(search_space)`: Sets the `chromosome_matrix` attribute of the DarwinPy object.
* `getChromosomeMatrix()`: Returns the `chromosome_matrix` attribute, which is a NumPy array.
* `getSearchSpace()`: Returns the `search_space` attribute, which is a tuple.
* `populate()`: Initializes the `chromosome_matrix` attribute with initial values or gene population.
* `select(fitness_vector)`: Selects mating pairs based on the fitness.
* `crossover(crossover_rate)`: Mates selected pairs and updates the `chromosome_matrix` attribute.
* `mutate(mutation_rate)`: Mutates the `chromosome_matrix` attribute of the DarwinPy object.
* `evolve(fitness_vector, mutation_rate, crossover_rate)`: Performs a complete genetic algorithm cycle, which includes selection, crossover, and mutation.

| Identifier | Type      |
|------------|-----------|
| `setSearchSpace`      | `None`     |
| `setChromosomeLength` | `None`     |
| `setPopulationSize`   | `None`     |
| `setChromosomeMatrix` | `None`     |
| `getChromosomeMatrix` | `numpy.array` |
| `getSearchSpace`      | `tuple`    |
| `populate`            | `None`     |
| `select`              | `None`     |
| `crossover`           | `None`     |
| `mutate`              | `None`     |
| `evolve`              | `None`     |

**Attributes:**
* `chromosome_length`: The length of each chromosome in the DarwinPy object.
* `population_size`: The size of the population in the DarwinPy object.
* `search_space`: The search space for the genetic algorithm, which is a tuple with an upper and lower bound.
* `chromosome_matrix`: The array of chromosomes in the DarwinPy object.
* `pair_list`: The list of mating pairs.
* `data_type`: The data type in which the genetic algorithm is bounded.

| Identifier           | Type          |
|----------------------|---------------|
| `chromosome_length`   | `int`         |
| `population_size`     | `int`         |
| `search_space`        | `tuple`       |
| `chromosome_matrix`   | `numpy.array` |
| `pair_list`           | `list`        |
| `data_type`           | `type`        |

## A Sample DarwinPy implementation
```python

import DarwinPy
import numpy as np

def hammingDist(goal, matrix):
    result = []
    for i in range(len(matrix)):
        temp = 0.
        for j in range(len(goal)):
            if goal[j] == matrix[i][j]:
                temp += 1.
        result.append(temp)
    return result


if __name__ == "__main__":
    mouse_population = 5
    mutation_rate = 0.5
    search_space = (0,1)
    goal = np.array([1,0,1,1,0,1,1, 0,1,1,0],int)
    chromosome_length = len(goal)

    mouse_species = DarwinPy.Genetics.Genetics(chromosome_length,
    mouse_population, (0,1), int)
    print(f"mouse species instantiated:\n {mouse_species}")

    print("the goal:\n {}".format(goal))

    mouse_species.populate()
    print(f"get mouse matrix(GA):\n {mouse_species.getChromosomeMatrix()}")


    fitness_vector = np.array(
    hammingDist(goal,mouse_species.getChromosomeMatrix()),
    float)

    print(f"get fitness vector: {fitness_vector}")

    is_goal = False
    gen = 1
    while is_goal == False:
        print(f"Generation #{gen}\n")
        gen += 1
        mouse_species.evolve(fitness_vector,
        mutation_rate, 0.5)
        print(f"get mouse matrix(GA):\n {mouse_species.getChromosomeMatrix()}")
        fitness_vector = np.array(
        hammingDist(goal,mouse_species.getChromosomeMatrix()),
        float)

        print(f"get fitness vector: {fitness_vector}")
        if chromosome_length in fitness_vector:
            is_goal = True
```
