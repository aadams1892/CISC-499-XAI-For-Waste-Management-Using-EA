import numpy as np

# Parent selection - tournament
def parent_select(population, tournament_size):
    
    # Get a random subset of the population to compete in the tournament.
    pop_subset = np.random.choice(population, tournament_size, False)

    # Subset has been selected, pick the 2 fittest.
    # Fitness function is TBD, so this cannot be implemented just yet.
    # The returned value of this function call will be the fitness of all the individuals.
    # This function will return the two fittest individuals.
    
    # indivs_fitness = [], contains all the fitnesses. Indices of the two highest fitnesses are the indices of the
        # individuals we will select as parents.
