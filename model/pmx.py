import random

# This function performs Partially Mapped Crossover (PMX)
def pmx(parent1, parent2):

    # Get a continuous subset from p1, then perform PMX on offspring1. No limit on initial subset size, but we start at 1 to ensure
    # that some crossover does actually occur.
    subset_size = random.randrange(1, len(parent1))
    offspring_subset = rand_subset(parent1, subset_size)
    # Get starting and ending indices of subset so we can place it in offspring1.
    start_index = parent1.index(offspring_subset[0])
    end_index = parent1.index(offspring_subset[subset_size-1])
    # Initialize offspring
    print(start_index, end_index, offspring_subset)
    offspring = [False]*len(parent1)

    # Assign the initial subset
    # If the subset wraps around
    if end_index < start_index:
        index_to_add = start_index
        for i in offspring_subset:
            # Add value
            if index_to_add < len(parent1):
                offspring[index_to_add] = i
                index_to_add += 1

            # Wrap around
            if index_to_add == len(parent1):
                index_to_add = 0

    # No wrap around
    else:
        offspring[start_index:end_index] = offspring_subset

    print([parent1, parent2, offspring])
    # Go through parent2, starting from start_index, and map the remainding values.
    # If we add a value to the offspring
    value_added = True
    i = start_index # Initially start at the left end of the original subset.
    while value_added:
        value_added = False

        # Loop iterates len(paren2) times.
        for _ in range(len(parent2)):

            # Value of parent2 at index i is not in the offspring, add it. Skip otherwise.
            if parent2[i] not in offspring:

                # If index i of the offspring is currently empty, add the value there.
                if offspring[i] == False:
                    offspring[i] = parent2[i]
                    value_added = True

                # Index i of the offspring is filled. Find an alternate index.
                else:
                    print("Index", i, "of offspring filled.")
                    # Make copy of i so we keep a constant progression of values of i.
                    index = i
                    index_found = False
                    while not index_found:
                        # Get the location in parent2 of offspring[index]
                        free_index = parent2.index(offspring[index])
                        print("Free index:", free_index)
                        # Index in offspring is empty, add value from parent2 here.
                        if offspring[free_index] == False:
                            print("Index", free_index, "of offspring empty.")
                            offspring[free_index] = parent2[index]
                            index_found = True
                            value_added = True
                            print("Offspring updated:", offspring)

                        # That index in the offspring is already filled by another value. Repeat process.
                        else:
                            print("Index", free_index, "of offspring filled, repeating.")
                            index = free_index
                            
            # Move to next index
            i += 1
            # Since we started at start_index, if we hit the 'end' of parent2, we still need to go from index 0 to start_index-1.
            if i == len(parent2):
                i = 0

            print(offspring)
        
        input("Iteration over, continue: ")

    return offspring