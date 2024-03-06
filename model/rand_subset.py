# Return a continuous subset of an individual of size subset_size.
def rand_subset(indiv, subset_size):
    subset_point = random.randrange(len(indiv))
    subset = []

# I CAN OPTIMIZE THIS MORE BY INITIALIZING SUBSET TO BE SUBSET_SIZE ZEROS AND THEN ASSIGNING.

    # If the subset_point selected is greater than the length of the population with itself subtracted,
    # then the ending index of the subset would be out of range. Therefore, we will need to wrap around
    # the population.
    if subset_point >= len(indiv)-subset_size:
        index_to_add = subset_point
        while len(subset) < subset_size:
            try:
                # Add next element to the subset
                subset.append(indiv[index_to_add])
                index_to_add += 1
            except:
                # Wrap around
                index_to_add -= len(indiv)

    # No need to wrap around
    else:
        subset = indiv[subset_point:subset_point+subset_size]

    return subset
