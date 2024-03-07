import random

# Performs Inversion Mutation on an individual
def inv_mut(indiv, rate):
    mutation_rate = rate # Best value found to be around 0.3
    mutation_occurs = random.random() 

    if mutation_rate > mutation_occurs:
        # Indices randomly chosen such that they cannot equal each other.
        inversion_start = random.choice([i for i in range(len(indiv))])
        inversion_end = random.choice([i for i in range(len(indiv)) if (i != inversion_start)])
        # Ensures inversion_start is a smaller idx than inversion_end
        if (inversion_start > inversion_end): 
            inversion_start, inversion_end = inversion_end, inversion_start
        
        # Creates subset from inversion_start to inversion_end (inclusive)
        inversion_subset = indiv[inversion_start:inversion_end+1]
        inversion_subset.reverse()
        return indiv[:inversion_start] + inversion_subset + indiv[inversion_end+1:]

    # Mutation is not performed
    else:
        return indiv
    
if __name__ ==  "__main__":
    print("[1, 2, 3, 4, 5, 6] --> ", inv_mut([1,2,3,4,5,6], 1))