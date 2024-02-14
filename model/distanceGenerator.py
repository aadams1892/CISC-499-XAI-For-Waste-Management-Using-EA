from geopy import distance
from geopy.geocoders import Nominatim
import pgeocode
import csv
import numpy as np

data = list(csv.reader(open('BrooklynSampleData.csv', newline='')))
dist_mat = []
row_count = len(data) - 1
for row in data[1:]:
    dist_array = []
    for row2 in data[1:]:
        dist_array.append(distance.distance((row[-2],row[-1]),(row2[-2],row2[-1])).km)
    dist_mat.append(dist_array)
    print(row_count, " rows left!")
    row_count -= 1
dist_mat=np.array(dist_mat)
dist_mat = np.around(dist_mat, 2)
np.savetxt('sample_dist_mat.csv', dist_mat, delimiter=',')