import math
import numpy as np
from itertools import combinations_with_replacement
from itertools import combinations

# Get array of stores
stores = np.genfromtxt('WoolworthsTravelDurations.csv', dtype = str, delimiter= ',', skip_footer= 66)
stores = stores[1:67]
stores = np.delete(stores, 55, 0)


# Array of stores in each region
CentralNorth_stores = np.genfromtxt('LocationCentralNorth.csv', dtype = str, delimiter= ',', skip_header=1, usecols=0)
CentralSouth_stores = np.genfromtxt('LocationCentralSouth.csv', dtype = str, delimiter= ',', skip_header=1, usecols=0)
East_stores = np.genfromtxt('LocationEastRegion.csv', dtype = str, delimiter= ',', skip_header=1, usecols=0)
North_stores = np.genfromtxt('LocationNorthRegion.csv', dtype = str, delimiter= ',', skip_header=1, usecols=0)
West_stores = np.genfromtxt('LocationWestRegion.csv', dtype = str, delimiter= ',', skip_header=1, usecols=0)
South_stores = np.genfromtxt('LocationSouthRegion.csv', dtype = str, delimiter= ',', skip_header=1, usecols=0)


# Find median demands of each day for every store in Central North
CentralNorth_WeekdayDemands = np.genfromtxt('LocationCentralNorth.csv', delimiter= ',', skip_header=1, usecols=1)
CentralNorth_WeekendDemands = np.genfromtxt('LocationCentralNorth.csv', delimiter= ',', skip_header=1, usecols=2)

# Find median demands of each day for every store in Central South
CentralSouth_WeekdayDemands = np.genfromtxt('LocationCentralSouth.csv', delimiter= ',', skip_header=1, usecols=1)
CentralSouth_WeekendDemands = np.genfromtxt('LocationCentralSouth.csv', delimiter= ',', skip_header=1, usecols=2)

# Find median demands of each day for every store in North
North_WeekdayDemands = np.genfromtxt('LocationNorthRegion.csv', delimiter= ',', skip_header=1, usecols=1)
North_WeekendDemands = np.genfromtxt('LocationNorthRegion.csv', delimiter= ',', skip_header=1, usecols=2)

# Find median demands of each day for every store in South
South_WeekdayDemands = np.genfromtxt('LocationSouthRegion.csv', delimiter= ',', skip_header=1, usecols=1)
South_WeekendDemands = np.genfromtxt('LocationSouthRegion.csv', delimiter= ',', skip_header=1, usecols=2)

# Find median demands of each day for every store in West
West_WeekdayDemands = np.genfromtxt('LocationWestRegion.csv', delimiter= ',', skip_header=1, usecols=1)
West_WeekendDemands = np.genfromtxt('LocationWestRegion.csv', delimiter= ',', skip_header=1, usecols=2)

# Find median demands of each day for every store in East
EastRegion_WeekdayDemands = np.genfromtxt('LocationEastRegion.csv', delimiter= ',', skip_header=1, usecols=1)
EastRegion_WeekendDemands = np.genfromtxt('LocationEastRegion.csv', delimiter= ',', skip_header=1, usecols=2)

demand_threshold = 26
viable_allRoutes = []
viable_CentralNorthRoutes = []
viable_CentralSouthRoutes = []
viable_NorthRoutes = []
viable_SouthRoutes = []
viable_WestRoutes = []
viable_EastRoutes = []

CentralNorth_Routes3 = (list(combinations(CentralNorth_stores, 3)))
CentralNorth_Routes4 = (list(combinations(CentralNorth_stores, 4)))
CentralNorth_Routes5 = (list(combinations(CentralNorth_stores, 5)))

for i in range(len(CentralNorth_Routes3)):
    stores = CentralNorth_Routes3[i]
    store1 = stores[0]
    store2 = stores[1]
    store3 = stores[2]
    demand = 0

    for j in range(len(CentralNorth_stores)):
        if store1 == CentralNorth_stores[j]:
            demand += CentralNorth_WeekdayDemands[j]

    for k in range(len(CentralNorth_stores)):
        if store2 == CentralNorth_stores[k]:
            demand += CentralNorth_WeekdayDemands[k]
    
    for h in range(len(CentralNorth_stores)):
        if store3 == CentralNorth_stores[h]:
            demand += CentralNorth_WeekdayDemands[h]

    if (demand < demand_threshold):
        viable_CentralNorthRoutes.append(CentralNorth_Routes3[i])
        viable_allRoutes.append(CentralNorth_Routes3[i])



for i in range(len(CentralNorth_Routes3)):
    stores = CentralNorth_Routes3[i]
    store1 = stores[0]
    store2 = stores[1]
    store3 = stores[2]
    demand = 0

    for j in range(len(CentralNorth_stores)):
        if store1 == CentralNorth_stores[j]:
            demand += CentralNorth_WeekdayDemands[j]

    for k in range(len(CentralNorth_stores)):
        if store2 == CentralNorth_stores[k]:
            demand += CentralNorth_WeekdayDemands[k]
    
    for h in range(len(CentralNorth_stores)):
        if store3 == CentralNorth_stores[h]:
            demand += CentralNorth_WeekdayDemands[h]

    if (demand < demand_threshold):
        viable_CentralNorthRoutes.append(CentralNorth_Routes3[i])
        viable_allRoutes.append(CentralNorth_Routes3[i])


CentralSouth_Routes3 = (list(combinations(CentralSouth_stores, 3)))
CentralSouth_Routes4 = (list(combinations(CentralSouth_stores, 4)))
CentralSouth_Routes5 = (list(combinations(CentralSouth_stores, 5)))

North_Routes3 = (list(combinations(North_stores, 3)))
North_Routes4 = (list(combinations(North_stores, 4)))
North_Routes5 = (list(combinations(North_stores, 5)))

South_Routes3 = (list(combinations(South_stores, 3)))
South_Routes4 = (list(combinations(South_stores, 4)))
South_Routes5 = (list(combinations(South_stores, 5)))

West_Routes3 = (list(combinations(West_stores, 3)))
West_Routes4 = (list(combinations(West_stores, 4)))
West_Routes5 = (list(combinations(West_stores, 5)))

East_Routes3 = (list(combinations(East_stores, 3)))
East_Routes4 = (list(combinations(East_stores, 4)))
East_Routes5 = (list(combinations(East_stores, 5)))
