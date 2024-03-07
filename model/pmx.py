import random
import rand_subset

# This function performs Partially Mapped Crossover (PMX)
def pmx(parent1, parent2):

    # Get a continuous subset from p1, then perform PMX on offspring1. No limit on initial subset size, but we start at 1 to ensure
    # that some crossover does actually occur.
    subset_size = random.randrange(1, len(parent1))
    offspring_subset = rand_subset.rand_subset(parent1, subset_size) # The subset that will be placed into the offspring.
    # Get starting and ending indices of subset so we can place it in the offspring.
    start_index = parent1.index(offspring_subset[0])
    end_index = parent1.index(offspring_subset[subset_size-1])
    # Initialize offspring
    offspring = [False]*len(parent1)

    # Assign the initial subset
    index_to_add = start_index
    # If the subset wraps around
    if end_index < start_index:
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
        for i in offspring_subset:
            offspring[index_to_add] = i
            index_to_add += 1

    value_added = True
    i = start_index # Going through the elements of parent2, starting at start_index.
    # Continue looping so long as a value gets added to the offspring.
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
                    # Make copy of i so we keep a constant progression of values of i.
                    index = i
                    free_index_found = False
                    # Continue searching until we find a free index in the offspring.
                    while not free_index_found:
                        # Get the location in parent2 where the value in offspring[i] is.
                        next_location = parent2.index(offspring[index])
                        # Check if that location is free in the offspring.
                        # Location is free, add value.
                        if offspring[next_location] == False:
                            offspring[next_location] = parent2[i]
                            free_index_found = True

                        # The location is already filled in the offspring. The next location we check is the location in parent2
                        # where this value in the offspring is.
                        else:
                            index = next_location
                                 
            # Move to next index
            i += 1
            # Since we started at start_index, if we hit the 'end' of parent2, we still need to go from index 0 to start_index-1.
            if i == len(parent2):
                i = 0

    return offspring

if __name__ ==  "__main__":
    print(pmx([1,2,3],[4,5,1]))