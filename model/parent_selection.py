import numpy as np

# Parent selection - tournament
def tournament_select(population, fitness, mating_pool_size, tournament_size):
    parent_indices = []
    parent_list = population.copy()
    # Get a random subset of the population to compete in the tournament
    while(len(parent_indices) < mating_pool_size):
        # Chooses random subset of population with no repetition
        pop_idx = list(np.random.randint(len(parent_list), size=tournament_size))
        pop_subset = []
        for i in pop_idx:
            pop_subset.append(parent_list[i])
        

        # Finds index of parent with greatest fitness from subset
        best_fitness = 0
        best_idx = 0
        best_idv = parent_list[0]
        for idv in pop_subset:
            i = population.index(idv)
            if(fitness[i] > best_fitness):
                best_fitness = fitness[i]
                best_idx = i
                best_idv = idv
        parent_indices.append(best_idx)

        # Done so that future subsets will not contain repeats.
        parent_list.remove(best_idv)

    return parent_indices