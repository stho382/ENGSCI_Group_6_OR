import math
import numpy as np
from itertools import combinations_with_replacement
from itertools import combinations

# Get array of stores
stores = np.genfromtxt('WoolworthsTravelDurations.csv', dtype = str, delimiter= ',', skip_footer= 66)
stores = stores[1:67]
stores = np.delete(stores, 55, 0)


# Array of stores in each region
LocationCentralNorth_stores = np.genfromtxt('LocationCentralNorth.csv', dtype = str, delimiter= ',', skip_header=1, usecols=0)
LocationCentralSouth_stores = np.genfromtxt('LocationCentralSouth.csv', dtype = str, delimiter= ',', skip_header=1, usecols=0)
LocationEast_stores = np.genfromtxt('LocationEastRegion.csv', dtype = str, delimiter= ',', skip_header=1, usecols=0)
LocationNorth_stores = np.genfromtxt('LocationNorthRegion.csv', dtype = str, delimiter= ',', skip_header=1, usecols=0)
LocationWest_stores = np.genfromtxt('LocationWestRegion.csv', dtype = str, delimiter= ',', skip_header=1, usecols=0)
LocationSouth_stores = np.genfromtxt('LocationSouthRegion.csv', dtype = str, delimiter= ',', skip_header=1, usecols=0)


#generate list of routes for each region 
CentralNorth_Routes = (list(combinations(LocationCentralNorth_stores, 3)))
print(CentralNorth_Routes)

