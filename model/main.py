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
    hardcode = 0

    pop1 = [45, 43, 2, 77, 1, 75, 77, 42, 39]
    sorted_pop = ms.sort(pop1)
    print(sorted_pop)

    tester = [1,2,3,4,5,6,7,8,9]
    for _ in range(5):
        mut = mt.mutate(tester)
        print(tester, "-->", mut)
main()