import random

# This function perform mutation on an individual
def mutate(indiv):
    mutation_rate = 0.15 # The probability that mutation will occur. Otherwise, no mutation will occur.
    # Mutate the individual according to inversion mutation.
    mutation_occurs = random.random() # Random chance that mutation will occur.

    # Mutation, 85% chance of occurring.
    if mutation_occurs > mutation_rate:
        inversion_start = random.randrange(len(indiv))
        inversion_end = random.randrange(len(indiv))
        # print("Inversion start:", inversion_start, "Inversion end:", inversion_end)
        # If inversion end is less than inversion start, we will need to wrap around. Might be implemented later.
        if inversion_end < inversion_start:
            inversion_subset1 = indiv[inversion_start:]
            inversion_subset2 = indiv[:inversion_end]
            inversion_subset = inversion_subset1 + inversion_subset2
            # print("Subset:", inversion_subset)
            inversion_subset.reverse() # Reverse the subset.
            # print("Inverted subset:", inversion_subset)
            index_split = inversion_start - inversion_end - 1 # The index which we will split the inversion_subset to add the values.

            # print(inversion_subset[index_split:], "+", indiv[inversion_end:inversion_start], "+", inversion_subset[:index_split])
            # Replace original individual with inverted subset.
            # Take the first index_split elements of the inversion_subset, since these will be the 'last' elements of the inversion.
            # We then take the part of the individual that was not mutated.
            # We then take the last index_split elements from the mutated subset, since these were the 'first' elements in the
            # inverted subset.
            mutated_indiv = inversion_subset[index_split:] + indiv[inversion_end:inversion_start] + inversion_subset[:index_split]

        else:
            # No wrap around
            inversion_subset = indiv[inversion_start:inversion_end]
            inversion_subset.reverse() # Reverse subset
            # Mutated individual
            mutated_indiv = indiv[:inversion_start] + inversion_subset + indiv[inversion_end:]

    # No mutation, directly copy individual.
    else:
        mutated_indiv = indiv
    return mutated_indiv
