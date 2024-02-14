import random
# For the implementation of an evolutionary algorithm for CISC499
"""
Needed:
    - Population initialization - set of distances to other trash bins
    - Parent selection - select fittest
    - Fitness function
    - Crossover
    - Mutation function
    - Survivor selection
"""


# For testing, the tests will be hardcoded.


# The population will consist of a set of trash bin addresses, intialized randomly.
# The addresses will be in the form of postal/zip codes.
def pop_init(pop_size, postal_codes):
    population = []
    while len(population) < pop_size:
        # Arbitrary value from 0-9 for an individual, used just for testing.
        # Each individual is initialized as a random permutation of postal codes
        indiv = postal_codes[:]
        random.shuffle(indiv)
        #print("pop length is", len(population), "and random shuffle is", indiv)
        # For testing purposes, the second element of an individual will just be a random number.
        # This will later change, as mentioned below.
        f = random.randrange(pop_size)
        # For each element in the individual, we now add the distance between it and all the other trash bins.
        # TBD when we will calculate all the trash bins.
        population.append((indiv, f))

    return population

# Function for calculating the fitness of the population
def fitness(population):

    # In this function, we will need to use the traffic congestion data as part of the calculation for fitness.

    # For now, this is a placeholder function.
    penalty = 0
    max_penalty = 0
    for indiv in population:
        for i in range(len(indiv)):
            penalty += indiv[i+1] - indiv[i] # Distance between consecutive points
        
    return penalty


# This function will perform crossover on two parents according to certain crossover strategy
def recomb(parent1, parent2):
    offspring = [] # Where the two offspring will go

    # Perform crossover
    # Call mutation function on both offspring

    return offspring


# This function perform mutation on an individual
def mutate(indiv):
    mutated_indiv = indiv # Start by assigning the individual directly
    
    # Mutate the individual according to a certain mutation strategy

    return mutated_indiv


# Parent selection - tournament
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


# Sorting the population initially or used for survivor selection.
# The sorting algorithm used here is insertion sort. This does not necessarily need to be the sorting algorithm
# used in the final algorithm.
def insert_sort(pop, indiv=None, indiv_fitness=None):
    # If the population is currently empty
    if not len(pop):
        return [[indiv, indiv_fitness]]
    # Each element in pop is the form [individual, individual_fitness]

    if len(pop) == 1:
        if pop[0][1] > indiv_fitness:
            temp = pop[0]
            pop[0] = [indiv, indiv_fitness]
            pop.append(temp)
            return pop

    # If we are adding a new individual to the population
    if indiv:
        inserted = 0
        i = 0
        while i < len(pop) and inserted == 0:
            if pop[i][1] > indiv_fitness:
                below_indiv_fitness = pop[1:i] # Start at index 1 to remove weakest individual.
                above_indiv_fitness = pop[i:]
                pop = below_indiv_fitness + [[indiv, indiv_fitness]] + above_indiv_fitness
                inserted = 1
            i += 1

    # Initial sorting of population.
    else:
        swap = 1
        # While the order of the population is still changing.
        while swap:
            swap = 0
            for i in range(len(pop)-1):
                # If two individuals are out of order.
                if pop[i][1] > pop[i+1][1]:
                    fit_to_sort = pop[i+1][1]
                    pop[i][1], pop[i+1][1] = pop[i+1][1], pop[i][1] # Swap values.
                    swap = 1
                    rec_i = i-1 # Recursive index for going back through the list
                    # We check back through the entire population to see if any more swaps are needed.
                    while rec_i >= 0:
                        if pop[rec_i][1] > fit_to_sort:
                            fit_to_sort = pop[rec_i][1]
                            pop[rec_i][1], fit_to_sort = fit_to_sort, pop[rec_i][1] # Swap
                        rec_i -=1
                    
    return pop


# This function will perform survivor selection according to some selection strategy.
def survivor_select(population):
    new_pop = [] # The survivors of survivor selection

    # Due to the nature of the individuals of the population, we will likely use a fitness-proportional survivor selection strategy.

    return new_pop


# Main
def main():
    hardcode = 0

    # Hardcoded examples
    if hardcode:
        new_dude = 'MM4'
        new_fit = 4
        pop_unsorted = [['SM8', 8], ['MN3', 3], ['OW2', 2], ['AW7', 7], ['LC9', 9]]

        empty_pop = []
        print("empty_pop:", empty_pop)
        print("Empty sorting...")
        empty_pop_sort = insert_sort(empty_pop, new_dude, new_fit)
        print("Empty sorted:", empty_pop_sort)
        print("\n")

        mini_pop = [['YZ5', 5]]
        print("mini_pop:", mini_pop)
        print("Mini sorting...")
        mini_pop_sort = insert_sort(mini_pop, new_dude, new_fit)
        print("Mini sorted:", mini_pop_sort)
        print("\n")

        print("pop_unsorted:", pop_unsorted)
        print("Sorting...")
        population = insert_sort(pop_unsorted)
        print("Sorted:", population)
        print("\n")
        
        print("Add new individual", new_dude, "with fitness", new_fit)
        print("Adding...")
        population = insert_sort(population, new_dude, new_fit)
        print("Added:", population)

    
    test_pop = pop_init(10, ['KN', 'AB', 'WS', 'ED', 'RF', 'TG', 'YH', 'UJ', 'IK', 'OL'])
    print("Initialized population:")
    for i in test_pop:
        print(i)

main()