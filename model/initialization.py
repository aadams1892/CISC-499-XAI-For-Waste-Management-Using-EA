import numpy as np

def pop_init(pop_size, bin_info, bin_count):
    population = []
    while len(population) < pop_size:
        # Each individual is represented by a list of bin indices
        indiv = []
        indiv = list(np.random.permutation(bin_count))
        indiv.remove(0)
        indiv.insert(0,0)
        population.append(indiv)

    return population

if __name__ ==  "__main__":
    import environment as en
    bin_info = en.BinInfo('../datasets/BinLocations.csv', '../datasets/BinDistances.csv')
    bin_count = len(bin_info.bins)
    print(pop_init(5,bin_info,bin_count))