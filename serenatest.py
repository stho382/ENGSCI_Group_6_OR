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
    
    for l in range(len(CentralNorth_stores)):
        if store3 == CentralNorth_stores[l]:
            demand += CentralNorth_WeekdayDemands[l]

    if (demand < demand_threshold):
        viable_CentralNorthRoutes.append(CentralNorth_Routes3[i])
        viable_allRoutes.append(CentralNorth_Routes3[i])

for i in range(len(CentralNorth_Routes4)):
    stores = CentralNorth_Routes4[i]
    store1 = stores[0]
    store2 = stores[1]
    store3 = stores[2]
    store4 = stores[3]
    demand = 0

    for j in range(len(CentralNorth_stores)):
        if store1 == CentralNorth_stores[j]:
            demand += CentralNorth_WeekdayDemands[j]

    for k in range(len(CentralNorth_stores)):
        if store2 == CentralNorth_stores[k]:
            demand += CentralNorth_WeekdayDemands[k]
    
    for l in range(len(CentralNorth_stores)):
        if store3 == CentralNorth_stores[l]:
            demand += CentralNorth_WeekdayDemands[l]

    for m in range(len(CentralNorth_stores)):
        if store3 == CentralNorth_stores[m]:
            demand += CentralNorth_WeekdayDemands[m]

    if (demand < demand_threshold):
        viable_CentralNorthRoutes.append(CentralNorth_Routes4[i])
        viable_allRoutes.append(CentralNorth_Routes4[i])

for i in range(len(CentralNorth_Routes5)):
    stores = CentralNorth_Routes5[i]
    store1 = stores[0]
    store2 = stores[1]
    store3 = stores[2]
    store4 = stores[3]
    store5 = stores[4]
    demand = 0

    for j in range(len(CentralNorth_stores)):
        if store1 == CentralNorth_stores[j]:
            demand += CentralNorth_WeekdayDemands[j]

    for k in range(len(CentralNorth_stores)):
        if store2 == CentralNorth_stores[k]:
            demand += CentralNorth_WeekdayDemands[k]
    
    for l in range(len(CentralNorth_stores)):
        if store3 == CentralNorth_stores[l]:
            demand += CentralNorth_WeekdayDemands[l]

    for m in range(len(CentralNorth_stores)):
        if store3 == CentralNorth_stores[m]:
            demand += CentralNorth_WeekdayDemands[m]

    for n in range(len(CentralNorth_stores)):
        if store3 == CentralNorth_stores[n]:
            demand += CentralNorth_WeekdayDemands[n]

    if (demand < demand_threshold):
        viable_CentralNorthRoutes.append(CentralNorth_Routes5[i])
        viable_allRoutes.append(CentralNorth_Routes5[i])

CentralSouth_Routes3 = (list(combinations(CentralSouth_stores, 3)))
for i in range(len(CentralSouth_Routes3)):
    stores = CentralSouth_Routes3[i]
    store1 = stores[0]
    store2 = stores[1]
    store3 = stores[2]
    demand = 0

    for j in range(len(CentralSouth_stores)):
        if store1 == CentralSouth_stores[j]:
            demand += CentralSouth_WeekdayDemands[j]

    for k in range(len(CentralSouth_stores)):
        if store2 == CentralSouth_stores[k]:
            demand += CentralSouth_WeekdayDemands[k]
    
    for l in range(len(CentralSouth_stores)):
        if store3 == CentralSouth_stores[l]:
            demand += CentralSouth_WeekdayDemands[l]

    if (demand < demand_threshold):
        viable_CentralSouthRoutes.append(CentralSouth_Routes3[i])
        viable_allRoutes.append(CentralSouth_Routes3[i])

CentralSouth_Routes4 = (list(combinations(CentralSouth_stores, 4)))
for i in range(len(CentralSouth_Routes4)):
    stores = CentralSouth_Routes4[i]
    store1 = stores[0]
    store2 = stores[1]
    store3 = stores[2]
    store4 = stores[3]
    demand = 0

    for j in range(len(CentralSouth_stores)):
        if store1 == CentralSouth_stores[j]:
            demand += CentralSouth_WeekdayDemands[j]

    for k in range(len(CentralSouth_stores)):
        if store2 == CentralSouth_stores[k]:
            demand += CentralSouth_WeekdayDemands[k]
    
    for l in range(len(CentralSouth_stores)):
        if store3 == CentralSouth_stores[l]:
            demand += CentralSouth_WeekdayDemands[l]
    
    for m in range(len(CentralSouth_stores)):
        if store3 == CentralSouth_stores[m]:
            demand += CentralSouth_WeekdayDemands[m]

    if (demand < demand_threshold):
        viable_CentralSouthRoutes.append(CentralSouth_Routes4[i])
        viable_allRoutes.append(CentralSouth_Routes4[i])

CentralSouth_Routes5 = (list(combinations(CentralSouth_stores, 5)))
for i in range(len(CentralSouth_Routes5)):
    stores = CentralSouth_Routes5[i]
    store1 = stores[0]
    store2 = stores[1]
    store3 = stores[2]
    store4 = stores[3]
    store5 = stores[4]
    demand = 0

    for j in range(len(CentralSouth_stores)):
        if store1 == CentralSouth_stores[j]:
            demand += CentralSouth_WeekdayDemands[j]

    for k in range(len(CentralSouth_stores)):
        if store2 == CentralSouth_stores[k]:
            demand += CentralSouth_WeekdayDemands[k]
    
    for l in range(len(CentralSouth_stores)):
        if store3 == CentralSouth_stores[l]:
            demand += CentralSouth_WeekdayDemands[l]
    
    for m in range(len(CentralSouth_stores)):
        if store3 == CentralSouth_stores[m]:
            demand += CentralSouth_WeekdayDemands[m]
            
    for n in range(len(CentralSouth_stores)):
        if store3 == CentralSouth_stores[n]:
            demand += CentralSouth_WeekdayDemands[n]

    if (demand < demand_threshold):
        viable_CentralSouthRoutes.append(CentralSouth_Routes5[i])
        viable_allRoutes.append(CentralSouth_Routes5[i])

North_Routes3 = (list(combinations(North_stores, 3)))
North_Routes4 = (list(combinations(North_stores, 4)))
North_Routes5 = (list(combinations(North_stores, 5)))

for i in range(len(North_Routes3)):
    stores = North_Routes3[i]
    store1 = stores[0]
    store2 = stores[1]
    store3 = stores[2]
    demand = 0

    for j in range(len(North_stores)):
        if store1 == North_stores[j]:
            demand += North_WeekdayDemands[j]

    for k in range(len(North_stores)):
        if store2 == North_stores[k]:
            demand += North_WeekdayDemands[k]
    
    for l in range(len(North_stores)):
        if store3 == North_stores[l]:
            demand += North_WeekdayDemands[l]

    if (demand < demand_threshold):
        viable_NorthRoutes.append(North_Routes3[i])
        viable_allRoutes.append(North_Routes3[i])


South_Routes3 = (list(combinations(South_stores, 3)))
for i in range(len(South_Routes3)):
    stores = South_Routes3[i]
    store1 = stores[0]
    store2 = stores[1]
    store3 = stores[2]
    demand = 0

    for j in range(len(South_stores)):
        if store1 == South_stores[j]:
            demand += South_WeekdayDemands[j]

    for k in range(len(South_stores)):
        if store2 == South_stores[k]:
            demand += South_WeekdayDemands[k]
    
    for l in range(len(South_stores)):
        if store3 == South_stores[l]:
            demand += South_WeekdayDemands[l]

    if (demand < demand_threshold):
        viable_SouthRoutes.append(South_Routes3[i])
        viable_allRoutes.append(South_Routes3[i])

South_Routes4 = (list(combinations(South_stores, 4)))
for i in range(len(South_Routes4)):
    stores = South_Routes4[i]
    store1 = stores[0]
    store2 = stores[1]
    store3 = stores[2]
    store4 = stores[3]
    demand = 0

    for j in range(len(South_stores)):
        if store1 == South_stores[j]:
            demand += South_WeekdayDemands[j]

    for k in range(len(South_stores)):
        if store2 == South_stores[k]:
            demand += South_WeekdayDemands[k]
    
    for l in range(len(South_stores)):
        if store3 == South_stores[l]:
            demand += South_WeekdayDemands[l]
    
    for m in range(len(South_stores)):
        if store4 == South_stores[m]:
            demand += South_WeekdayDemands[m]

    if (demand < demand_threshold):
        viable_SouthRoutes.append(South_Routes4[i])
        viable_allRoutes.append(South_Routes4[i])

South_Routes5 = (list(combinations(South_stores, 5)))
for i in range(len(South_Routes5)):
    stores = South_Routes5[i]
    store1 = stores[0]
    store2 = stores[1]
    store3 = stores[2]
    store4 = stores[3]
    store5 = stores[4]
    demand = 0

    for j in range(len(South_stores)):
        if store1 == CentralSouth_stores[j]:
            demand += CentralSouth_WeekdayDemands[j]

    for k in range(len(South_stores)):
        if store2 == South_stores[k]:
            demand += South_WeekdayDemands[k]
    
    for l in range(len(South_stores)):
        if store3 == South_stores[l]:
            demand += South_WeekdayDemands[l]
    
    for m in range(len(South_stores)):
        if store4 == South_stores[m]:
            demand += South_WeekdayDemands[m]
            
    for n in range(len(South_stores)):
        if store5 == South_stores[n]:
            demand += South_WeekdayDemands[n]

    if (demand < demand_threshold):
        viable_SouthRoutes.append(South_Routes5[i])
        viable_allRoutes.append(South_Routes5[i])

West_Routes3 = (list(combinations(West_stores, 3)))

West_Routes4 = (list(combinations(West_stores, 4)))
West_Routes5 = (list(combinations(West_stores, 5)))

East_Routes3 = (list(combinations(East_stores, 3)))
East_Routes4 = (list(combinations(East_stores, 4)))
East_Routes5 = (list(combinations(East_stores, 5)))

for i in range(len(East_Routes3)):
    stores = East_Routes3[i]
    store1 = stores[0]
    store2 = stores[1]
    store3 = stores[2]
    demand = 0

    for j in range(len(East_stores)):
        if store1 == East_stores[j]:
            demand += EastRegion_WeekdayDemands[j]

    for k in range(len(East_stores)):
        if store2 == East_stores[k]:
            demand += EastRegion_WeekdayDemands[k]
    
    for l in range(len(East_stores)):
        if store3 == East_stores[l]:
            demand += EastRegion_WeekdayDemands[l]

    if (demand < demand_threshold):
        viable_EastRoutes.append(East_Routes3[i])
        viable_allRoutes.append(East_Routes3[i])

for i in range(len(East_Routes4)):
    stores = East_Routes4[i]
    store1 = stores[0]
    store2 = stores[1]
    store3 = stores[2]
    store4 = stores[3]
    demand = 0

    for j in range(len(East_stores)):
        if store1 == East_stores[j]:
            demand += EastRegion_WeekdayDemands[j]

    for k in range(len(East_stores)):
        if store2 == East_stores[k]:
            demand += EastRegion_WeekdayDemands[k]
    
    for l in range(len(East_stores)):
        if store3 == East_stores[l]:
            demand += EastRegion_WeekdayDemands[l]

    for m in range(len(East_stores)):
        if store3 == East_stores[m]:
            demand += EastRegion_WeekdayDemands[m]

    if (demand < demand_threshold):
        viable_EastRoutes.append(East_Routes4[i])
        viable_allRoutes.append(East_Routes4[i])

for i in range(len(East_Routes5)):
    stores = East_Routes5[i]
    store1 = stores[0]
    store2 = stores[1]
    store3 = stores[2]
    store4 = stores[3]
    store5 = stores[4]
    demand = 0

    for j in range(len(East_stores)):
        if store1 == East_stores[j]:
            demand += EastRegion_WeekdayDemands[j]

    for k in range(len(East_stores)):
        if store2 == East_stores[k]:
            demand += EastRegion_WeekdayDemands[k]
    
    for l in range(len(East_stores)):
        if store3 == East_stores[l]:
            demand += EastRegion_WeekdayDemands[l]

    for m in range(len(East_stores)):
        if store3 == East_stores[m]:
            demand += EastRegion_WeekdayDemands[m]

    for n in range(len(East_stores)):
        if store3 == East_stores[n]:
            demand += EastRegion_WeekdayDemands[n]

    if (demand < demand_threshold):
        viable_EastRoutes.append(East_Routes5[i])
        viable_allRoutes.append(East_Routes5[i])