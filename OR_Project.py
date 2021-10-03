import math
import numpy as np

# Get array of stores
stores = np.genfromtxt('WoolworthsTravelDurations.csv', dtype = str, delimiter= ',', skip_footer= 66)
stores = stores[1:67]
stores = np.delete(stores, 55, 0)

# Array of stores in central north region
CentralNorth_stores = np.genfromtxt('LocationCentralNorth.csv', dtype = str, delimiter= ',', skip_header=1, usecols=0)

# Find median demands for weekdays for every store
CentralNorth_WeekdayDemands = np.genfromtxt('LocationCentralNorth.csv', delimiter= ',', skip_header=1, usecols=1)
'''
# Time from each store to each store
travel_durations = np.genfromtxt('WoolworthsTravelDurations.csv', dtype = str, delimiter= ',', skip_header= 1, usecols= list(range(1,67)))

# Remove distribution centre
travel_durations = np.delete(travel_durations, 55, 0)

# Time from distribution centre to every store
distribution_time = np.genfromtxt('WoolworthsTravelDurations.csv', dtype = str, delimiter= ',', skip_header= 56, skip_footer=10, usecols= list(range(1,67)))

# Remove distribution centre
distribution_time = np.delete(distribution_time, 55, 0)
'''

#time_threshold = 60 * 4 * 2 * 30 
demand_threshold = 26

routes = []
#hours = []

#time = 0
demand = 0

for i in range(len(CentralNorth_stores)):
    smallest_route_visited = []
    smallest_route_visited.append(i)

    for j in range(len(CentralNorth_stores)):
        next_store = 0
        demand = CentralNorth_WeekdayDemands[i]
        route_list = []
        nodes_list = []

        route_list.append(CentralNorth_stores[i])

        visited = False
        thisSmallest = False

        while (demand < demand_threshold):
            if i != j:
                route_list