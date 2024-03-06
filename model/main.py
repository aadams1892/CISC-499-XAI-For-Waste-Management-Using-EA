import random

import initialization
import evaluation as ev
import parent_selection as ps
import crossover as co
import mutation as mt
import survivor_selection as ss
import merge_sort as ms
import environment as en

# todo list:
# - Finalize crossover (pmx)
# - Do survivor selection
# - Test for bugs
# - Fine tune hyperparameters

def main():

    random.seed()

    pop_size = 100
    mating_pool_size = 50 # Must be even
    tournament_size = 4
    crossover_rate = 0.8
    mut_rate = 0.3
    max_gen = 100

    bin_info = en.BinInfo('../datasets/BinLocations.csv', '../datasets/BinDistances.csv')
    bin_count = len(bin_info.bins)

    # Initialization
    population = initialization.pop_init(pop_size, bin_info, bin_count)
    fitness = [] # Fitness ranges from 0 to bin_count
    for i in population:
        fitness.append(ev.fitness(i, bin_info, bin_count))
        if(len(i) == 1): print(i)
    gen = 0

    # Main Evolutionary Loop
    while (gen < max_gen):
        parents = ps.tournament_select(population, fitness, mating_pool_size, tournament_size)
        offspring = []
        offspring_fitness = []
        i=0

        while len(offspring) < mating_pool_size:
            # Mutates 2 offspring created in crossover before adding to offspring list.
            off = co.crossover(population[parents[i]], population[parents[i+1]], crossover_rate)
            
            off[0] = mt.mutate(offspring[0], mut_rate)
            off[1] = mt.mutate(offspring[1], mut_rate)
            
            offspring.append(off[0])
            offspring.append(off[1])
            offspring_fitness.append(ev.fitness(off[0],bin_info,bin_count))
            offspring_fitness.append(ev.fitness(off[1],bin_info,bin_count))
            i += 2

        population = ss.survivor_select(population, fitness, offspring, offspring_fitness)
        gen += 1
main()


