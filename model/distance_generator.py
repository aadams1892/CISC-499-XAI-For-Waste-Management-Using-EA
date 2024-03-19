from geopy import distance
from geopy.geocoders import Nominatim
import pgeocode
import csv
import numpy as np

# Used to generate dictionaries for each bin representing its distance from
# other bins. Needs to be modified so that each dict only contains 4 entries
# representing the closest bin in each direction from the current one.
data = list(csv.reader(open('../datasets/BinLocations - Small.csv', newline='')))
dictionary_list = []
for row in data[1:]:
    dist = {}
    idx = 0
    for row2 in data[1:]:
        if(row[-3] == row2[-3] or row[-4] == row2[-4]):
            dist[idx] = distance.distance((row[-2],row[-1]),(row2[-2],row2[-1])).km
        idx += 1
    dictionary_list.append(dist)

with open('../datasets/BinDistances - Small.csv', 'w', newline='') as dict_output:
    writer = csv.DictWriter(dict_output, list(range(len(data) - 1)))
    writer.writeheader()
    writer.writerows(dictionary_list)