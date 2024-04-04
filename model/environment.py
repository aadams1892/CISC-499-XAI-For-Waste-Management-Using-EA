import random
import numpy as np
from enum import IntEnum
import csv

class BinInfo:

    def __init__(self, bin_file, dict_file):
        self.bins = list(csv.reader(open(bin_file, newline='')))
        self.headers = self.bins.pop(0) # Skips csv header
        for row in self.bins:
            if row[0] == "N":
                row[0] = 0
            elif row[0] == 'NE':
                row[0] = 1
            elif row[0] == 'E':
                row[0] = 2
            elif row[0] == 'SE':
                row[0] = 3
            elif row[0] == 'S':
                row[0] = 4
            elif row[0] == 'SW':
                row[0] = 5
            elif row[0] == 'W':
                row[0] = 6
            else:
                row[0] = 7
            row[-1] = float(row[-1])
            row[-2] = float(row[-2])
        reader = list(csv.DictReader(open(dict_file)))
        self.dist = [] # List of dictionaries, each representing distance of other bins from current one.
        for row in reader:
            self.dist.append({int(k):float(v) for k, v in row.items() if v != '' and float(v) != 0})

    def get_roads(self, state):
        # Returns tuple containing the 2 street names associated with 
        # a given state/bin. (All bins are located on street corners)
        return (self.bins[state][-4], self.bins[state][-3])

    def get_coord(self, state):
        # Returns latitude longitude tuple.
        return (self.bins[state][-2], self.bins[state][-1])
    
    def get_dist(self, state1, state2):
        # Returns the distance from state1 to state 2.
        try:
            return (self.dist[state1][state2])
        except KeyError:
            return 9999           
    def get_closest(self, state):
        # Returns the closest bin from 'state'.
        values = list(self.dist[state].values())
        pos = values.index(min(values))
        keys = list(self.dist[state].keys())
        return keys[pos]
    
    def get_actions(self, state):
        # Returns list of keys associated with the current state.
        # Each represents a state that can be moved to.
        return list(self.dist[state].keys())

if __name__ ==  "__main__":
    bin_map = BinInfo('../datasets/BinLocations.csv', '../datasets/BinDistances.csv')

    print("BIN 0:")
    print(bin_map.get_roads(0))
    print(bin_map.get_coord(0))
    print("Closest bin:", bin_map.get_closest(0))
    print("Distance   :", round(bin_map.get_dist(0,10),4), "km")
    print(bin_map.get_actions(0))
    print(bin_map.get_dist(0,7))
