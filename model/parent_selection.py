import random

def parent_select(population, subset_size):
    subset_point = random.randrange(len(population))
    subset = []
    # If the subset_point selected is greater than the length of the population with itself subtracted,
    # then the ending index of the subset would be out of range. Therefore, we will need to wrap around
    # the population.
    if subset_point >= len(population)-subset_size:
        index_to_add = subset_point
        while len(subset) < subset_size:
            try:
                # Add next element to the subset
                subset.append(population[index_to_add])
                index_to_add += 1
            except:
                # Wrap around
                index_to_add -= len(population)

    # No need to wrap around
    else:
        subset = population[subset_point:subset_point+subset_size]

    # Subset has been selected, pick the 2 fittest.
    # Fitness function is TBD, so this cannot be implemented just yet.