import random

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