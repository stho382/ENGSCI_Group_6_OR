import math
import numpy as np

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

time_threshold = 60 * 4 * 2 * 30 
demand_threshold = 26

routes = []
hours = []

time = 0
demand = 0

for i in range(len(stores)):
    smallest_route_visited = []
    smallest_route_visited.append(i)

    for ii in range():
        next_store = 0
        time = 0
        demand = 0
        route_list = []
        nodes_list = []

        duration_store = travel_durations[i]
        time = distribution_time[i] + (7.5*60*demands)
        route_list.append(stores[i])
        nodes_list.append(i)
        demand += demands[i]

        visited = False
        thisSmallest = False

        for j in range(len(duration_store)):
            thisSmallest = j in smallest_route_visited
            if (thisSmallest == True):
                duration_store[j] = 0




            if ((time < time_threshold) & (demand < demand_threshold)):
                back_home = distribution_time[next_store]
                time -= distribution_time[next_store]
                route_list.append(stores[next_store])
                duration_store = travel_durations[next_store]
            else:
                time -= duration_store[next_store] + (7.5 * 60 * demands[next_store] + distribution_time[next_store])
                time += back_home
                back_home = 0

    time = time / (60*60)
    time = (math.ceil(time*4)) / 4
    routes.append(route_list)
    hours.append(time)

