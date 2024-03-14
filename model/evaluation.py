def fitness(individual, bin_info):

    # Computes fitness using individual length, and total distance 

    dist = 0
    for bin in range(len(individual)-1):
        dist += bin_info.get_dist(individual[bin], individual[bin+1]) # Distance between consecutive bins.
    if (dist > 0):
        fit = 10000/dist
    else:
        fit = 0
    return fit


if __name__ ==  "__main__":
    import environment
    bin_info = environment.BinInfo('../datasets/BinLocations.csv', '../datasets/BinDistances.csv')
    bin_count = len(bin_info.bins)
    print(fitness([0,2,3,4,5,6],bin_info))

