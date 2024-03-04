# This function performs Partially Mapped Crossover (PMX)
def pmx(parent1, parent2):

    # Get a continuous subset from p1, then perform PMX on offspring1. No limit on initial subset size.
    offspring_subset = rand_subset(parent1, random.randrange(len(parent1)))
    print(offspring_subset)
    # Get starting and ending indices of subset so we can place it in offspring1.
    start_index = parent1.index(offspring_subset[0])
    end_index = parent1.index(offspring_subset[-1])
    # Initialize offspring
    offspring = [0]*len(parent1)

    return offspring
