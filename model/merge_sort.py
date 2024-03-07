# Implements merge sort based on fitness of individuals.
def sort(population, fitness):
    # If population and fitness are not equal in length, the sort will fail.
    if len(population) > 1 and len(population) == len(fitness):
        pop = []
        fit = []
        mid = len(population)//2 # Middle point of population

        # Recursively call merge_sort on the left subarrays. This will continuously split up the left half of the population and fitness
        # until the parameter passed into this function call has only 2 individuals. In this call, the left_pop/left_fit and
        # right_pop/right_fit will then have a single element. The next this function is called on the single element, nothing will
        # happen since we are in the if conditional of the length being greater than 1. This is to say that this line will
        # cause recursive calls until len(left_pop) = 1.
        left_pop, left_fit = sort(population[:mid], fitness[:mid])

        # Same as above for the right subarray
        right_pop, right_fit = sort(population[mid:], fitness[mid:])

        # Below is the actual sorting. We will go through left_fit and right_fit and continuously merge them.
        # It will start with both having only a single element and work up until they are actually half of the population.
        i = 0
        j = 0
        # Loop through until we reach the end of one of the subarrays
        while i < len(left_fit) and j < len(right_fit):
            # If the element in the left fitness subarray is less than the element we are on in the right subarray.
            if left_fit[i] < right_fit[j]:
                pop.append(left_pop[i])
                fit.append(left_fit[i])
                i += 1
            # The element in the right subarray is less or equal.
            else:
                pop.append(right_pop[j])
                fit.append(right_fit[j])
                j += 1

        # The while loop ends only once we have reached the end of the one of the arrays. If this happens, it means the
        # values remaining in the subarrays that we have not reached the end of are all greater than pop. Additionally, the
        # remaining values are also already sorted by nature of the recursive calls.
        # Check for remaining values in a left subarray.
        while i < len(left_fit):
            pop.append(left_pop[i])
            fit.append(left_fit[i])
            i += 1
                    
        # Check for remaining values in a right subarray.
        while j < len(right_fit):
            pop.append(right_pop[j])
            fit.append(right_fit[j])
            j += 1

    # If the population is just a single element, it is already sorted so return it as is.
    else:
        pop = population
        fit = fitness

    return pop, fit