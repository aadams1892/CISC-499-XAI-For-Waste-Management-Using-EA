import random

import initialization
import evaluation
import parent_selection
import crossover
import survivor_selection
import environment
import mutation

# - Finalize crossover (pmx)
# - Do survivor selection
# - Test for bugs
# - Fine tune hyperparameters

def main():

    random.seed()

    pop_size = 100
    mating_pool_size = 20 # Must be even
    tournament_size = 4
    crossover_rate = 0
    mut_rate = 0.3
    max_gen = 100

    bin_info = environment.BinInfo('../datasets/BinLocations.csv', '../datasets/BinDistances.csv')
    bin_count = len(bin_info.bins)

    # Initialization
    population = initialization.pop_init(pop_size, bin_info, bin_count)
    fitness = [] # Fitness ranges from 0 to bin_count
    for i in population:
        fitness.append(evaluation.fitness(i, bin_info))
    gen = 0

    # Main Evolutionary Loop
    while (gen < max_gen):

        parents = parent_selection.tournament_select(population, fitness, mating_pool_size, tournament_size)
        random.shuffle(parents)
        offspring = []
        offspring_fitness = []
        
        i=0
        while len(offspring) < mating_pool_size:
            # Generates 2 new offspring using PMX
            off = crossover.crossover_main(population[parents[i]], population[parents[i+1]], crossover_rate)
            
            # Performs inversion mutation on offspring
            off[0] = mutation.inv_mut(off[0],mut_rate)
            off[1] = mutation.inv_mut(off[1],mut_rate)
           
            offspring.append(off[0])
            offspring.append(off[1])
            offspring_fitness.append(evaluation.fitness(off[0],bin_info))
            offspring_fitness.append(evaluation.fitness(off[1],bin_info))
            i += 2

        population, fitness = survivor_selection.mu_plus_lambda(population, fitness, offspring, offspring_fitness)
        print("gen: ",gen," - max fit: ",max(fitness)," - pop size: ", len(population))
        gen += 1
main()


