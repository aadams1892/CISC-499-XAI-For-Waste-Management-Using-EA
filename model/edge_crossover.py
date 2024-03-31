import random

DEBUG = 0
# This function performs Edge Crossover.
def crossover(parent1, parent2):
    
    # edge table represented as a dictionary
    edge_table = {}
    # Construct the edge table for the two parents
    # First, populate the edge list with the genes of parent1
    for g in range(len(parent1)):
        
        try: value = [parent1[g-1], parent1[g+1]] # Value to add to the gene key
        # Except statement since the only time the above assignment would not work is if we are at the last index of the parent, at
        # which point switching g+1 becomes 0.
        except: value = [parent1[g-1], parent1[0]]
        edge_table[parent1[g]] = value

    # Second, add the genes of parent2 to the gene lists from parent1
    for g in range(len(parent2)):

        try: value = [parent2[g-1], parent2[g+1]] # Value to add to the gene key
        except: value = [parent2[g-1], parent2[0]]
        # Add the edges to the value for the gene to the list
        for v in value:
            edge_table[parent2[g]].append(v)

    #current_element = random.choice(list(edge_table.keys())) # Randomly select the first gene to add to the offspring
    current_element = 1
    offspring = [current_element] # The offspring

    if DEBUG:
        print("Edge table is:", edge_table)

    # Edge crossover loop
    while len(offspring) < len(parent1):

        common_edges = []
        # Remove all instances of current_element from the edge table
        for k, edgelist in edge_table.items():
            if current_element in edgelist:
                # In each other's lists - common edge
                if k in edge_table[current_element]:
                    common_edges.append(k)

                # Remove all instances of current_element from the edge list
                new_edgelist = []
                for i in edgelist:
                    if i != current_element:
                        new_edgelist.append(i)
                # Set value in edge_table having removed all instances of current_element
                edge_table[k] = new_edgelist

        if DEBUG:
            print("Common edges:", common_edges)

        # Get the edge list for every element in the edge list of the current element
        next_element_list = []
        for k in edge_table[current_element]:
            next_element_list.append([k, edge_table[k]])

        # Remove current element from edgelist
        edge_table.pop(current_element)

        # Select the next gene to add to the offspring accoridng to the edge crossover algorithm.
        # Priority: 1. Common edge, 2. Shortest list, 3. Random  

        # If there are elements in next_element_list, go through the process of selecting one. If there are not, then there must
        # only be 1 element left in edge_table, so add it to the offspring.
        if len(next_element_list):

            # If there are common edges
            if len(common_edges):
                # If only 1 common edge, it is the next element to add to the offspring
                if len(common_edges) == 1:
                    current_element = common_edges[0]
                # If multiple, pick randomly
                else:
                    next_element = random.randint(0, len(common_edges)-1)
                    current_element = common_edges[next_element]

            # No common edges, select the next element to add to the offspring by picking the key in next_element_list that has the
            # shortest list
            else:
                # Initialize the shortest list to the first element
                shortest_list = [next_element_list[0][0]]

                for edgelist in next_element_list[1:]:
                    # If the length of this element's edge list is the same as the current shortest length found, add it to
                    # the list of shortest list lengths.
                    # Note that we can always check the length of the first element in shortest_list since if there are multiple entries
                    # already, they will all have the same length.
                    if len(edgelist[1]) == len(edge_table[shortest_list[0]]):
                        shortest_list.append(edgelist[0])

                    # if the length of this element's edge list is less than the shortest list length found, replace all of shortest_list
                    # with the element list's key.
                    elif len(edgelist[1]) < len(edge_table[shortest_list[0]]):
                        shortest_list = [edgelist[0]]

                # If there is only a single key in shortest_list, that key is the next element to add to the offspring
                if len(shortest_list) == 1:
                    current_element = shortest_list[0]

                # If there are multiple keys in shortest_list, then we pick randomly.
                elif len(shortest_list) > 1:
                    next_element = random.randint(0, len(shortest_list)-1)
                    current_element = shortest_list[next_element]
        # next_element_list is empty, pick the last remaining element in edge_table to be the last element added to the offspring
        else:
            last_key = list(edge_table)
            current_element = last_key[0]

        # Add newly selected element to the offspring
        offspring.append(current_element)

        if DEBUG:
            print("Offspring:", offspring)
            print("\n")

    return offspring


if __name__ ==  "__main__":

    # p1 = [1,2,3,4,5,6,7,8,9]
    #p2 = [9,3,7,8,2,6,5,1,4]
    #print(crossover(p1,p2))
    for _ in range(10):
        p1, p2 = random.sample([1,2,3,4,5,6,7], 7), random.sample([1,2,3,4,5,6,7], 7)
        offspring = crossover(p1,p2)
        print(p1, "+", p2, "-->", offspring)
        print("\n")

    