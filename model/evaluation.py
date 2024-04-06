def fitness(individual, bin_info, eval_type):

    # Computes fitness using individual length, and total distance 

    dist = 0
    for bin in range(len(individual)-1):
        # Depending on how much the truck must turn, distance in scaled accordingly.
        turn = 1
        if(eval_type == 1):
            if (abs(bin_info.bins[bin][0] - bin_info.bins[bin+1][0]) == 1):
                turn = 1.25
            elif (abs(bin_info.bins[bin][0] - bin_info.bins[bin+1][0]) == 2):
                turn = 1.5
            elif (abs(bin_info.bins[bin][0] - bin_info.bins[bin+1][0]) == 3): 
                turn = 1.75
            elif (abs(bin_info.bins[bin][0] - bin_info.bins[bin+1][0]) == 4):
                turn = 2
        dist += bin_info.get_dist(individual[bin], individual[bin+1]) * turn 

    if (dist > 0):
        fit = len(individual)/dist
    else:
        fit = 0
    return fit


if __name__ ==  "__main__":
    import environment
    bin_info = environment.BinInfo('../datasets/BinLocations.csv', '../datasets/BinDistances.csv')
    bin_count = len(bin_info.bins)
    print(fitness([0,2,3,4,5,6],bin_info))

