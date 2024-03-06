# This function will go through the crossover process, from calculating if it will occur to mutating the offspring.
import random
import mutation as mt
def crossover(parent1, parent2, rate):
    crossover_rate = rate # The probability that crossover will occur.
    crossover_occurs = random.random()

    print(crossover_rate, crossover_occurs)
    # Perform partially mapped crossover (PMX). PMX chosen for adjacency preservation.
    if crossover_rate > crossover_occurs:

        # Perform PMX on offspring1.
        offspring1_raw = pmx(parent1, parent2)

        # Perform PMX on offspring2, with the role of the parents reversed from offspring1.
        offspring2_raw = pmx(parent2, parent1)

    # Crossover does not occur, directly copy parents as offspring.
    else:
        offspring1_raw = parent1
        offspring2_raw = parent2

    # Call mutation function on both offspring.
    offspring1 = mt.mutate(offspring1_raw)
    offspring2 = mt.mutate(offspring2_raw)
    offsprings = [offspring1, offspring2]

    return offsprings