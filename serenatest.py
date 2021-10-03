import math
import numpy as np
from itertools import combinations_with_replacement
from itertools import combinations

# Get array of stores
stores = np.genfromtxt('WoolworthsTravelDurations.csv', dtype = str, delimiter= ',', skip_footer= 66)
stores = stores[1:67]
stores = np.delete(stores, 55, 0)

# Array of stores in central north region
LocationCentralNorth_stores = np.genfromtxt('LocationCentralNorth.csv', dtype = str, delimiter= ',', skip_header=1, usecols=0)

# Find median demands of each day for every store
LocationCentralNorth_demands_monday = np.genfromtxt('LocationCentralNorth.csv', dtype = str, delimiter= ',', skip_header=1, usecols=1)
LocationCentralNorth_demands_tuesday = np.genfromtxt('LocationCentralNorth.csv', dtype = str, delimiter= ',', skip_header=1, usecols=2)
LocationCentralNorth_demands_wednesday = np.genfromtxt('LocationCentralNorth.csv', dtype = str, delimiter= ',', skip_header=1, usecols=3)
LocationCentralNorth_demands_thursday = np.genfromtxt('LocationCentralNorth.csv', dtype = str, delimiter= ',', skip_header=1, usecols=4)
LocationCentralNorth_demands_friday = np.genfromtxt('LocationCentralNorth.csv', dtype = str, delimiter= ',', skip_header=1, usecols=5)
LocationCentralNorth_demands_saturday = np.genfromtxt('LocationCentralNorth.csv', dtype = str, delimiter= ',', skip_header=1, usecols=6)

# Time from each store to each store
travel_durations = np.genfromtxt('WoolworthsTravelDurations.csv', dtype = str, delimiter= ',', skip_header= 1, usecols= list(range(1,67)))

# Remove distribution centre
travel_durations = np.delete(travel_durations, 55, 0)

# Time from distribution centre to every store
distribution_time = np.genfromtxt('WoolworthsTravelDurations.csv', dtype = str, delimiter= ',', skip_header= 56, skip_footer=10, usecols= list(range(1,67)))

# Remove distribution centre
distribution_time = np.delete(distribution_time, 55, 0)


#l = len(list(combinations(LocationCentralNorth_stores, 3)))
CentralNorthRoutes = (list(combinations(LocationCentralNorth_stores, 3)))
print(CentralNorthRoutes)
