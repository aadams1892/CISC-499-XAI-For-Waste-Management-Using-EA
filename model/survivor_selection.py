import merge_sort

# Performs mu plus lambda survivor selection. Returns new population and new fitness
def mu_plus_lambda(population, fitness, offspring, offspring_fitness):
    merged_pop = population + offspring
    merged_fit = fitness + offspring_fitness
    # Finds sorted population and fitness of merged population
    new_pop, new_fit = merge_sort.sort(merged_pop, merged_fit)
    # Returns as many individuals as were in the original population, starting with the most fit
    return new_pop[:len(population)], new_fit[:len(population)]