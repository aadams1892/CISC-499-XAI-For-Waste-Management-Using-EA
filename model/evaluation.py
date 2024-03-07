def fitness(individual, bin_info):

    # Computes fitness using individual length, and total distance 

    length = len(individual)
    dist = 0
    for bin in range(len(individual)-1):
        dist += bin_info.get_dist(individual[bin], individual[bin+1]) # Distance between consecutive bins.
    fit = length - dist
    if(fit < 0): fit = 0
    return fit


if __name__ ==  "__main__":
    import environment
    bin_info = environment.BinInfo('../datasets/BinLocations.csv', '../datasets/BinDistances.csv')
    bin_count = len(bin_info.bins)
    print(fitness([0,2,3],bin_info,bin_count))

