# This function will go through the crossover process, from calculating if it will occur to mutating the offspring.
def crossover(parent1, parent2):
    offspring_base = [] # Where the two offspring will go
    crossover_rate = 0.9 # The probability that crossover will occur.
    crossover_occurs = random.random()

    print(crossover_rate, crossover_occurs)
    # Perform partially mapped crossover (PMX). PMX chosen for adjacency preservation.
    if crossover_rate > crossover_occurs:

        # Perform PMX on offspring1.
        offspring1 = pmx(parent1, parent2)

        # Perform PMX on offspring2, with the role of the parents reversed from offspring1.
        offspring2 = pmx(parent2, parent1)

        offspring_base = [offspring1, offspring2]
    # Crossover does not occur, directly copy parents as offspring.
    else:
        offspring_base = [parent1, parent2]

    # Call mutation function on both offspring.
    offspring = [mutate(offspring_base(0)), mutate(offspring_base(1))]

    return offspring
