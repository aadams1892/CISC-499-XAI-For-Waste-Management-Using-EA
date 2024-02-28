# Sorting  algorithm implementing mergesort.
def sort(population):
    # If we have more than a single value, we keep recursively calling
    if len(population) > 1:
        pop = []
        mid = len(population)//2 # Middle point of population

        # Recursively call merge_sort on the left subarray. This will continuously split up the left half of the population
        # until the parameter passed into this function call has only 2 individuals. In this call, the left_subarray and
        # right_subarray will then have a single element. The next this function is called on the single element, nothing will
        # happen since we are in the if conditional of the length being greater than 1. This is to say that this line will
        # cause recursive calls until len(left_subarray) = 1.
        left_subarray = sort(population[:mid])

        # Same as above for the right subarray
        right_subarray = sort(population[mid:])

        # Below is the actual sorting. We will go through left_subarray and right_subarray and continuously merge them.
        # It will start with both having only a single element and work up until they are actually half of the population.
        i = 0
        j = 0
        # Loop through until we reach the end of one of the subarrays
        while i < len(left_subarray) and j < len(right_subarray):
            # If the element in the left subarray is less than the element we are on in the right subarray.
            if left_subarray[i] < right_subarray[j]:
                pop.append(left_subarray[i])
                i += 1
            # The element in the right subarray is less or equal.
            else:
                pop.append(right_subarray[j])
                j += 1

        # The while loop ends only once we have reached the end of the one of the arrays. If this happens, it means the
        # values remaining in the subarray that we have not reached the end of are all greater than pop. Additionally, the
        # remaining values are also already sorted by nature of the recursive calls.
        # Check for remaining values in the left subarray.
        while i < len(left_subarray):
            pop.append(left_subarray[i])
            i += 1
                    
        # Check for remaining values in the right subarray.
        while j < len(right_subarray):
            pop.append(right_subarray[j])
            j += 1

    # If the population is just a single element, it is already sorted so return it as is.
    else:
        pop = population

    return pop