import random
import initialization
import evaluation as ev
import parent_selection as ps
import crossover as co
import mutation as mt
import survivor_selection as ss
import merge_sort as ms

# Main
def main():
    mutate_test = 0
    sort_test = 0
    crossover_test = 1

    if sort_test:
        pop1 = [45, 43, 2, 77, 1, 75, 77, 42, 39]
        sorted_pop = ms(pop1)
        print(sorted_pop)

    if mutate_test:
        tester = [1,2,3,4,5,6,7,8,9]
        for _ in range(5):
            mutation = mt(tester)
            print(tester, "-->", mutation)

    if crossover_test:
        co([1,2,3], [5,7,9])
main()
