import random
import numpy as np
from enum import IntEnum
import csv

class BinInfo:

    def __init__(self, bin_file, dict_file):
        self.bins = list(csv.reader(open(bin_file, newline='')))
        self.bins.pop(0) # Skips csv header

        reader = list(csv.DictReader(open(dict_file)))
        self.dist = [] # List of dictionaries, each representing distance of other bins from current one.
        for row in reader:
            self.dist.append({int(k):float(v) for k, v in row.items() if v != '' and float(v) != 0})

    def get_roads(self, state):
        # Returns tuple containing the 2 street names associated with 
        # a given state/bin. (All bins are located on street corners)
        return (self.bins[state][2], self.bins[state][3])

    def get_coord(self, state):
        # Returns latitude longitude tuple.
        return (self.bins[state][4], self.bins[state][5])
    
    def get_dist(self, state1, state2):
        # Returns the distance from state1 to state 2.
        try:
            return (self.dist[state1][state2])
        except KeyError:
            return 999
            
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