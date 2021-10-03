import math
import numpy as np
from itertools import combinations_with_replacement
from itertools import combinations

# Get array of stores
stores = np.genfromtxt('WoolworthsTravelDurations.csv', dtype = str, delimiter= ',', skip_footer= 66)
stores = stores[1:67]
stores = np.delete(stores, 55, 0)

# Array of stores in central north region
CentralNorth_stores = np.genfromtxt('LocationCentralNorth.csv', dtype = str, delimiter= ',', skip_header=1, usecols=0)

# Array of stores in central north region
CentralSouth_stores = np.genfromtxt('LocationCentralSouth.csv', dtype = str, delimiter= ',', skip_header=1, usecols=0)

# Array of stores in central north region
North_stores = np.genfromtxt('LocationNorthRegion.csv', dtype = str, delimiter= ',', skip_header=1, usecols=0)

# Array of stores in central north region
South_stores = np.genfromtxt('LocationSouthRegion.csv', dtype = str, delimiter= ',', skip_header=1, usecols=0)

# Array of stores in central north region
West_stores = np.genfromtxt('LocationWestRegion.csv', dtype = str, delimiter= ',', skip_header=1, usecols=0)

# Array of stores in central north region
East_stores = np.genfromtxt('LocationEastRegion.csv', dtype = str, delimiter= ',', skip_header=1, usecols=0)

# Find median demands of each day for every store in Central North
CentralNorth_WeekdayDemands = np.genfromtxt('LocationCentralNorth.csv', dtype = str, delimiter= ',', skip_header=1, usecols=1)
CentralNorth_WeekendDemands = np.genfromtxt('LocationCentralNorth.csv', dtype = str, delimiter= ',', skip_header=1, usecols=2)

# Find median demands of each day for every store in Central South
CentralSouth_WeekdayDemands = np.genfromtxt('LocationCentralSouth.csv', dtype = str, delimiter= ',', skip_header=1, usecols=1)
CentralSouth_WeekendDemands = np.genfromtxt('LocationCentralSouth.csv', dtype = str, delimiter= ',', skip_header=1, usecols=2)

# Find median demands of each day for every store in North
North_WeekdayDemands = np.genfromtxt('LocationNorthRegion.csv', dtype = str, delimiter= ',', skip_header=1, usecols=1)
North_WeekendDemands = np.genfromtxt('LocationNorthRegion.csv', dtype = str, delimiter= ',', skip_header=1, usecols=2)

# Find median demands of each day for every store in South
South_WeekdayDemands = np.genfromtxt('LocationSouthRegion.csv', dtype = str, delimiter= ',', skip_header=1, usecols=1)
South_WeekendDemands = np.genfromtxt('LocationSouthRegion.csv', dtype = str, delimiter= ',', skip_header=1, usecols=2)

# Find median demands of each day for every store in West
West_WeekdayDemands = np.genfromtxt('LocationWestRegion.csv', dtype = str, delimiter= ',', skip_header=1, usecols=1)
West_WeekendDemands = np.genfromtxt('LocationWestRegion.csv', dtype = str, delimiter= ',', skip_header=1, usecols=2)

# Find median demands of each day for every store in East
EastRegion_WeekdayDemands = np.genfromtxt('LocationEastRegion.csv', dtype = str, delimiter= ',', skip_header=1, usecols=1)
EastRegion_WeekendDemands = np.genfromtxt('LocationEastRegion.csv', dtype = str, delimiter= ',', skip_header=1, usecols=2)


#l = len(list(combinations(LocationCentralNorth_stores, 3)))
CentralNorth_Routes = (list(combinations(CentralNorth_stores, 3)))
print(CentralNorth_Routes)
