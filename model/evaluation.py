def fitness(population):

    # In this function, we will need to use the traffic congestion data as part of the calculation for fitness.

    # For now, this is a placeholder function.
    penalty = 0
    max_penalty = 0
    for indiv in population:
        for i in range(len(indiv)):
            penalty += indiv[i+1] - indiv[i] # Distance between consecutive points
        
    return penalty