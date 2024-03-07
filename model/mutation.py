import random

# Performs Inversion Mutation on an individual
def inv_mut(indiv, rate):
    mutation_rate = rate # Best value found to be around 0.3
    mutation_occurs = random.random() 

    if mutation_rate > mutation_occurs:
        # Indices randomly chosen such that they cannot equal each other.
        inversion_start = random.choice([i for i in range(len(indiv))])
        inversion_end = random.choice([i for i in range(len(indiv)) if (i != inversion_start)])
        if inversion_end < inversion_start:
            inversion_subset1 = indiv[inversion_start:]
            inversion_subset2 = indiv[:inversion_end+1]
            inversion_subset = inversion_subset1 + inversion_subset2
            
            inversion_subset.reverse() # Reverse the subset.
            index_split = len(indiv) - inversion_start

            # Replace original individual with inverted subset.
            # Take the first index_split elements of the inversion_subset, since these will be the 'last' elements of the inversion.
            # We then take the part of the individual that was not mutated.
            # We then take the last index_split elements from the mutated subset, since these were the 'first' elements in the
            # inverted subset.
            mutated_indiv = inversion_subset[index_split:] + indiv[inversion_end+1:inversion_start] + inversion_subset[:index_split]

        else:
            # No wrap around
            inversion_subset = indiv[inversion_start:inversion_end+1]
            inversion_subset.reverse()
            mutated_indiv = indiv[:inversion_start] + inversion_subset + indiv[inversion_end+1:]

    # No mutation, directly copy individual.
    else:
        mutated_indiv = indiv

    return mutated_indiv

if __name__ ==  "__main__":
    print("[1, 2, 3, 4, 5, 6] --> ", inv_mut([1,2,3,4,5,6], 1))