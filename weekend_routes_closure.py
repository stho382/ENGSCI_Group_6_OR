import math
import numpy as np
from pulp import *
import os
from itertools import combinations_with_replacement
from itertools import combinations

# Get array of stores
stores = np.genfromtxt("" + os.getcwd() + os.sep + "Data" + os.sep + "WoolworthsTravelDurations.csv", dtype = str, delimiter= ',', skip_footer= 66)
stores = stores[1:54]

all_stores = np.genfromtxt("" + os.getcwd() + os.sep + "Data" + os.sep + "WoolworthsTravelDurations.csv", dtype = str, delimiter= ',', skip_footer= 66)
all_stores = all_stores[1:67]

# Distances between stores
distances = np.genfromtxt("" + os.getcwd() + os.sep + "Data" + os.sep + "WoolworthsDistances.csv", delimiter= ',', skip_header=1, usecols=list(range(1,67)))

for i in reversed(range(53,len(distances))):
    distances = np.delete(distances, i, 0)
    distances = np.delete(distances, i, 1)

# Travel duration between each store
travel_durations = np.genfromtxt("" + os.getcwd() + os.sep + "Data" + os.sep + "WoolworthsTravelDurations.csv", delimiter= ',', skip_header=1, usecols=list(range(1,67)))
travel_durations = np.delete(travel_durations, 55, 0)
travel_durations = np.delete(travel_durations, 55, 1)

# Travel duration from distribution centre
distribution_time = np.genfromtxt("" + os.getcwd() + os.sep + "Data" + os.sep + "WoolworthsTravelDurations.csv", delimiter= ',', skip_header=56, skip_footer=10, usecols=list(range(1,67)))
distribution_time = np.delete(distribution_time, 55, 0)

# Array of stores in each region
CentralNorth_stores_Weekend = np.genfromtxt("" + os.getcwd() + os.sep + "Data" + os.sep + "LocationCentralNorthWeekend.csv", dtype = str, delimiter= ',', skip_header=1, usecols=0)
CentralSouth_stores_Weekend = np.genfromtxt("" + os.getcwd() + os.sep + "Data" + os.sep + "LocationCentralSouthWeekend.csv", dtype = str, delimiter= ',', skip_header=1, usecols=0)
East_stores_Weekend = np.genfromtxt("" + os.getcwd() + os.sep + "Data" + os.sep + "LocationEastRegionWeekend.csv", dtype = str, delimiter= ',', skip_header=1, usecols=0)
North_stores_Weekend = np.genfromtxt("" + os.getcwd() + os.sep + "Data" + os.sep + "LocationNorthRegion.csv", dtype = str, delimiter= ',', skip_header=1, usecols=0)
West_stores_Weekend = np.genfromtxt("" + os.getcwd() + os.sep + "Data" + os.sep + "LocationWestRegionWeekend.csv", dtype = str, delimiter= ',', skip_header=1, usecols=0)
South_stores_Weekend = np.genfromtxt("" + os.getcwd() + os.sep + "Data" + os.sep + "LocationSouthRegionWeekend.csv", dtype = str, delimiter= ',', skip_header=1, usecols=0)

# Find median demands of each day for every store in Central North
CentralNorth_WeekendDemands = np.genfromtxt("" + os.getcwd() + os.sep + "Data" + os.sep + "LocationCentralNorthWeekend.csv", delimiter= ',', skip_header=1, usecols=2)

# Find median demands of each day for every store in Central South
CentralSouth_WeekendDemands = np.genfromtxt("" + os.getcwd() + os.sep + "Data" + os.sep + "LocationCentralSouthWeekend.csv", delimiter= ',', skip_header=1, usecols=2)

# Find median demands of each day for every store in North
North_WeekendDemands = np.genfromtxt("" + os.getcwd() + os.sep + "Data" + os.sep + "LocationNorthRegionWeekend.csv", delimiter= ',', skip_header=1, usecols=2)

# Find median demands of each day for every store in South
South_WeekendDemands = np.genfromtxt("" + os.getcwd() + os.sep + "Data" + os.sep + "LocationSouthRegionWeekend.csv", delimiter= ',', skip_header=1, usecols=2)

# Find median demands of each day for every store in West
West_WeekendDemands = np.genfromtxt("" + os.getcwd() + os.sep + "Data" + os.sep + "LocationWestRegionWeekend.csv", delimiter= ',', skip_header=1, usecols=2)

# Find median demands of each day for every store in East
East_WeekendDemands = np.genfromtxt("" + os.getcwd() + os.sep + "Data" + os.sep + "LocationEastRegionWeekend.csv", delimiter= ',', skip_header=1, usecols=2)

# Median demands
demands = np.genfromtxt("" + os.getcwd() + os.sep + "Data" + os.sep + "median_demand.csv", delimiter= ',', skip_header=1, usecols=2)

for i in reversed(range(53,len(demands))):
    demands = np.delete(demands, i, 0)

enlarge_stores = []
close_stores = []
merge_stores = []

# Loop through stores
for i in range(len(distances)):
    for j in range(len(distances)):

        # Searching for stores that are within 1500 metres of one another and with demand of less than 7.5 pallets
        if distances[i][j] > 0 and distances[i][j] < 3000 and demands[i] < 9 and demands[j] < 9:
            temp = [stores[i], stores[j]]
            temp_reverse = [stores[j], stores[i]]

            # Check if stores are not the same
            if (temp_reverse not in merge_stores):

                if demands[i] > demands[j]:
                    # Increase demand of store i
                    demands[i] += (demands[j] * 0.5)
                    # Append stores to respect arrays
                    enlarge_stores.append(stores[i])
                    close_stores.append(stores[j])
                    merge_stores.append(temp)
                    
                if demands[j] > demands[i]:
                    # Increase demand of store j 
                    demands[j] += (demands[i] * 0.5)
                    # Append stores to respect arrays
                    enlarge_stores.append(stores[j])
                    close_stores.append(stores[i])
                    merge_stores.append(temp)


num1 = 0
num2 = 0
num3 = 0
num4 = 0
num5 = 0
num6 = 0

for i in range(len(CentralNorth_stores_Weekend)):

    if (num1 == 0):
        for j in range(len(close_stores)):
            if CentralNorth_stores_Weekend[i] == close_stores[j]:
                CentralNorth_stores_Weekend = np.delete(CentralNorth_stores_Weekend, i, 0)
                CentralNorth_WeekendDemands = np.delete(CentralNorth_WeekendDemands, i, 0)
                num1 = 1

for i in range(len(CentralSouth_stores_Weekend)):

    if (num2 == 0):
        for j in range(len(close_stores)):
            if CentralSouth_stores_Weekend[i] == close_stores[j]:
                CentralSouth_stores_Weekend = np.delete(CentralSouth_stores_Weekend, i, 0)
                CentralSouth_WeekendDemands = np.delete(CentralSouth_WeekendDemands, i, 0)
                num2 = 1            

for i in range(len(North_stores_Weekend)):
    if (num3 == 0):
        for j in range(len(close_stores)):
            if North_stores_Weekend[i] == close_stores[j]:
                North_stores_Weekend = np.delete(North_stores_Weekend, i, 0)
                North_WeekendDemands = np.delete(North_WeekendDemands, i, 0)
                num3 = 1

for i in range(len(South_stores_Weekend)):
    if (num4 == 0):
        for j in range(len(close_stores)):
            if South_stores_Weekend[i] == close_stores[j]:
                South_stores_Weekend = np.delete(South_stores_Weekend, i, 0)
                South_WeekendDemands = np.delete(South_WeekendDemands, i, 0)
                num4 = 1


for i in range(len(West_stores_Weekend)):
    if (num5 == 0):
        for j in range(len(close_stores)):
            if West_stores_Weekend[i] == close_stores[j]:
                West_stores_Weekend = np.delete(West_stores_Weekend, i, 0)
                West_WeekendDemands = np.delete(West_WeekendDemands, i, 0)
                num5 = 1 

for i in range(len(East_stores_Weekend)):
    if (num6 == 0):
        for j in range(len(close_stores)):
            if East_stores_Weekend[i] == close_stores[j]:
                East_stores_Weekend = np.delete(East_stores_Weekend, i, 0)
                East_WeekendDemands = np.delete(East_WeekendDemands, i, 0)
                num6 = 1

for i in reversed(range(len(stores))):
    for j in range(len(close_stores)):
        if (stores[i] == close_stores[j]):
            stores = np.delete(stores, i, 0)
            travel_durations = np.delete(travel_durations, i, 0)
            travel_durations = np.delete(travel_durations, i, 1)
            distribution_time = np.delete(distribution_time, i, 0)



demand_threshold = 27
time_threshold = 60 * 4 * 2 * 60

Routes_Weekend = []
Time_Weekend = []

CentralNorthRoutes_Weekend = []
CentralSouthRoutes_Weekend = []
NorthRoutes_Weekend = []
SouthRoutes_Weekend = []
WestRoutes_Weekend = []
EastRoutes_Weekend = []

CentralNorth_Routes2_Weekend = (list(combinations(CentralNorth_stores_Weekend, 2)))
CentralNorth_Routes3_Weekend = (list(combinations(CentralNorth_stores_Weekend, 3)))
CentralNorth_Routes4_Weekend = (list(combinations(CentralNorth_stores_Weekend, 4)))
CentralNorth_Routes5_Weekend = (list(combinations(CentralNorth_stores_Weekend, 5)))
CentralNorth_Routes6_Weekend = (list(combinations(CentralNorth_stores_Weekend, 6)))

for i in range(len(CentralNorth_Routes2_Weekend)):
    store1 = CentralNorth_Routes2_Weekend[i][0]
    store2 = CentralNorth_Routes2_Weekend[i][1]
    demand_weekend = 0
    time_weekend = 0

    for j in range(len(CentralNorth_stores_Weekend)):
        if store1 == CentralNorth_stores_Weekend[j]:
            demand_weekend += CentralNorth_WeekendDemands[j]
            time_weekend += CentralNorth_WeekendDemands[j] * 450

    for k in range(len(CentralNorth_stores_Weekend)):
        if store2 == CentralNorth_stores_Weekend[k]:
            demand_weekend += CentralNorth_WeekendDemands[k]
            time_weekend += CentralNorth_WeekendDemands[k] * 450

    for store in range(len(stores)):
        if store1 == stores[store]:
            time_weekend += distribution_time[store]
        if store2 == stores[store]:
            time_weekend += distribution_time[store]

    for store_row in range(len(stores)):
        if store1 == stores[store_row]:
            for store_col in range(len(stores)):
                if store2 == stores[store_col]:
                    time_weekend += travel_durations[store_row][store_col]
        
    if (demand_weekend < demand_threshold and time_weekend <= time_threshold):
        CentralNorthRoutes_Weekend.append(CentralNorth_Routes2_Weekend[i])
        Routes_Weekend.append(CentralNorth_Routes2_Weekend[i])
        Time_Weekend.append(time_weekend/60/60)

for i in range(len(CentralNorth_Routes3_Weekend)):
    store1 = CentralNorth_Routes3_Weekend[i][0]
    store2 = CentralNorth_Routes3_Weekend[i][1]
    store3 = CentralNorth_Routes3_Weekend[i][2]
    demand_weekend = 0
    time_weekend = 0

    for j in range(len(CentralNorth_stores_Weekend)):
        if store1 == CentralNorth_stores_Weekend[j]:
            demand_weekend += CentralNorth_WeekendDemands[j]
            time_weekend += CentralNorth_WeekendDemands[j] * 450

    for k in range(len(CentralNorth_stores_Weekend)):
        if store2 == CentralNorth_stores_Weekend[k]:
            demand_weekend += CentralNorth_WeekendDemands[k]
            time_weekend += CentralNorth_WeekendDemands[k] * 450

    for l in range(len(CentralNorth_stores_Weekend)):
        if store3 == CentralNorth_stores_Weekend[l]:
            demand_weekend += CentralNorth_WeekendDemands[l]
            time_weekend += CentralNorth_WeekendDemands[l] * 450

    for store in range(len(stores)):
        if store1 == stores[store]:
            time_weekend += distribution_time[store]            
        if store3 == stores[store]:
            time_weekend += distribution_time[store]

    for store_row in range(len(stores)):
        if store1 == stores[store_row]:
            for store_col in range(len(stores)):
                if store2 == stores[store_col]:
                    time_weekend += travel_durations[store_row][store_col]

    for store_row in range(len(stores)):
        if store2 == stores[store_row]:
            for store_col in range(len(stores)):
                if store3 == stores[store_col]:
                    time_weekend += travel_durations[store_row][store_col]

    if (demand_weekend < demand_threshold and time_weekend <= time_threshold):
        CentralNorthRoutes_Weekend.append(CentralNorth_Routes3_Weekend[i])
        Routes_Weekend.append(CentralNorth_Routes3_Weekend[i])
        Time_Weekend.append(time_weekend/60/60)

for i in range(len(CentralNorth_Routes4_Weekend)):
    store1 = CentralNorth_Routes4_Weekend[i][0]
    store2 = CentralNorth_Routes4_Weekend[i][1]
    store3 = CentralNorth_Routes4_Weekend[i][2]
    store4 = CentralNorth_Routes4_Weekend[i][3]
    demand_weekend = 0
    time_weekend = 0

    for j in range(len(CentralNorth_stores_Weekend)):
        if store1 == CentralNorth_stores_Weekend[j]:
            demand_weekend += CentralNorth_WeekendDemands[j]
            time_weekend += CentralNorth_WeekendDemands[j] * 450

    for k in range(len(CentralNorth_stores_Weekend)):
        if store2 == CentralNorth_stores_Weekend[k]:
            demand_weekend += CentralNorth_WeekendDemands[k]
            time_weekend += CentralNorth_WeekendDemands[k] * 450

    for l in range(len(CentralNorth_stores_Weekend)):
        if store3 == CentralNorth_stores_Weekend[l]:
            demand_weekend += CentralNorth_WeekendDemands[l]
            time_weekend += CentralNorth_WeekendDemands[l] * 450

    for m in range(len(CentralNorth_stores_Weekend)):
        if store4 == CentralNorth_stores_Weekend[m]:
            demand_weekend += CentralNorth_WeekendDemands[m]
            time_weekend += CentralNorth_WeekendDemands[m] * 450

    for store in range(len(stores)):
        if store1 == stores[store]:
            time_weekend += distribution_time[store]
        if store4 == stores[store]:
            time_weekend += distribution_time[store]

    for store_row in range(len(stores)):
        if store1 == stores[store_row]:
            for store_col in range(len(stores)):
                if store2 == stores[store_col]:
                    time_weekend += travel_durations[store_row][store_col]

    for store_row in range(len(stores)):
        if store2 == stores[store_row]:
            for store_col in range(len(stores)):
                if store3 == stores[store_col]:
                    time_weekend += travel_durations[store_row][store_col]

    for store_row in range(len(stores)):
        if store3 == stores[store_row]:
            for store_col in range(len(stores)):
                if store4 == stores[store_col]:
                    time_weekend += travel_durations[store_row][store_col]

    if (demand_weekend < demand_threshold and time_weekend <= time_threshold):
        CentralNorthRoutes_Weekend.append(CentralNorth_Routes4_Weekend[i])
        Routes_Weekend.append(CentralNorth_Routes4_Weekend[i])
        Time_Weekend.append(time_weekend/60/60)

for i in range(len(CentralNorth_Routes5_Weekend)):
    store1 = CentralNorth_Routes5_Weekend[i][0]
    store2 = CentralNorth_Routes5_Weekend[i][1]
    store3 = CentralNorth_Routes5_Weekend[i][2]
    store4 = CentralNorth_Routes5_Weekend[i][3]
    store5 = CentralNorth_Routes5_Weekend[i][4]

    demand_weekend = 0
    time_weekend = 0

    for j in range(len(CentralNorth_stores_Weekend)):
        if store1 == CentralNorth_stores_Weekend[j]:
            demand_weekend += CentralNorth_WeekendDemands[j]
            time_weekend += CentralNorth_WeekendDemands[j] * 450

    for k in range(len(CentralNorth_stores_Weekend)):
        if store2 == CentralNorth_stores_Weekend[k]:
            demand_weekend += CentralNorth_WeekendDemands[k]
            time_weekend += CentralNorth_WeekendDemands[k] * 450

    for l in range(len(CentralNorth_stores_Weekend)):
        if store3 == CentralNorth_stores_Weekend[l]:
            demand_weekend += CentralNorth_WeekendDemands[l]
            time_weekend += CentralNorth_WeekendDemands[l] * 450

    for m in range(len(CentralNorth_stores_Weekend)):
        if store4 == CentralNorth_stores_Weekend[m]:
            demand_weekend += CentralNorth_WeekendDemands[m]
            time_weekend += CentralNorth_WeekendDemands[m] * 450

    for n in range(len(CentralNorth_stores_Weekend)):
        if store5 == CentralNorth_stores_Weekend[n]:
            demand_weekend += CentralNorth_WeekendDemands[n]
            time_weekend += CentralNorth_WeekendDemands[n] * 450

    for store in range(len(stores)):
        if store1 == stores[store]:
            time_weekend += distribution_time[store]
        if store5 == stores[store]:
            time_weekend += distribution_time[store]

    for store_row in range(len(stores)):
        if store1 == stores[store_row]:
            for store_col in range(len(stores)):
                if store2 == stores[store_col]:
                    time_weekend += travel_durations[store_row][store_col]

    for store_row in range(len(stores)):
        if store2 == stores[store_row]:
            for store_col in range(len(stores)):
                if store3 == stores[store_col]:
                    time_weekend += travel_durations[store_row][store_col]

    for store_row in range(len(stores)):
        if store3 == stores[store_row]:
            for store_col in range(len(stores)):
                if store4 == stores[store_col]:
                    time_weekend += travel_durations[store_row][store_col]

    for store_row in range(len(stores)):
        if store4 == stores[store_row]:
            for store_col in range(len(stores)):
                if store5 == stores[store_col]:
                    time_weekend += travel_durations[store_row][store_col]

    if (demand_weekend < demand_threshold and time_weekend <= time_threshold):
        CentralNorthRoutes_Weekend.append(CentralNorth_Routes5_Weekend[i])
        Routes_Weekend.append(CentralNorth_Routes5_Weekend[i])
        Time_Weekend.append(time_weekend/60/60)

for i in range(len(CentralNorth_Routes6_Weekend)):
    store1 = CentralNorth_Routes6_Weekend[i][0]
    store2 = CentralNorth_Routes6_Weekend[i][1]
    store3 = CentralNorth_Routes6_Weekend[i][2]
    store4 = CentralNorth_Routes6_Weekend[i][3]
    store5 = CentralNorth_Routes6_Weekend[i][4]
    store6 = CentralNorth_Routes6_Weekend[i][5]

    demand_weekend = 0
    time_weekend = 0

    for j in range(len(CentralNorth_stores_Weekend)):
        if store1 == CentralNorth_stores_Weekend[j]:
            demand_weekend += CentralNorth_WeekendDemands[j]
            time_weekend += CentralNorth_WeekendDemands[j] * 450

    for k in range(len(CentralNorth_stores_Weekend)):
        if store2 == CentralNorth_stores_Weekend[k]:
            demand_weekend += CentralNorth_WeekendDemands[k]
            time_weekend += CentralNorth_WeekendDemands[k] * 450

    for l in range(len(CentralNorth_stores_Weekend)):
        if store3 == CentralNorth_stores_Weekend[l]:
            demand_weekend += CentralNorth_WeekendDemands[l]
            time_weekend += CentralNorth_WeekendDemands[l] * 450

    for m in range(len(CentralNorth_stores_Weekend)):
        if store4 == CentralNorth_stores_Weekend[m]:
            demand_weekend += CentralNorth_WeekendDemands[m]
            time_weekend += CentralNorth_WeekendDemands[m] * 450

    for n in range(len(CentralNorth_stores_Weekend)):
        if store5 == CentralNorth_stores_Weekend[n]:
            demand_weekend += CentralNorth_WeekendDemands[n]
            time_weekend += CentralNorth_WeekendDemands[n] * 450

    for o in range(len(CentralNorth_stores_Weekend)):
        if store6 == CentralNorth_stores_Weekend[o]:
            demand_weekend += CentralNorth_WeekendDemands[o]
            time_weekend += CentralNorth_WeekendDemands[o] * 450

    for store in range(len(stores)):
        if store1 == stores[store]:
            time_weekend += distribution_time[store]
        if store5 == stores[store]:
            time_weekend += distribution_time[store]

    for store_row in range(len(stores)):
        if store1 == stores[store_row]:
            for store_col in range(len(stores)):
                if store2 == stores[store_col]:
                    time_weekend += travel_durations[store_row][store_col]

    for store_row in range(len(stores)):
        if store2 == stores[store_row]:
            for store_col in range(len(stores)):
                if store3 == stores[store_col]:
                    time_weekend += travel_durations[store_row][store_col]

    for store_row in range(len(stores)):
        if store3 == stores[store_row]:
            for store_col in range(len(stores)):
                if store4 == stores[store_col]:
                    time_weekend += travel_durations[store_row][store_col]

    for store_row in range(len(stores)):
        if store4 == stores[store_row]:
            for store_col in range(len(stores)):
                if store5 == stores[store_col]:
                    time_weekend += travel_durations[store_row][store_col]

    for store_row in range(len(stores)):
        if store5 == stores[store_row]:
            for store_col in range(len(stores)):
                if store6 == stores[store_col]:
                    time_weekend += travel_durations[store_row][store_col]

    if (demand_weekend < demand_threshold and time_weekend <= time_threshold):
        CentralNorthRoutes_Weekend.append(CentralNorth_Routes6_Weekend[i])
        Routes_Weekend.append(CentralNorth_Routes6_Weekend[i])
        Time_Weekend.append(time_weekend/60/60)

# Central South stores
CentralSouth_Routes2_Weekend = (list(combinations(CentralSouth_stores_Weekend, 2)))
CentralSouth_Routes3_Weekend = (list(combinations(CentralSouth_stores_Weekend, 3)))
CentralSouth_Routes4_Weekend = (list(combinations(CentralSouth_stores_Weekend, 4)))
CentralSouth_Routes5_Weekend = (list(combinations(CentralSouth_stores_Weekend, 5)))
CentralSouth_Routes6_Weekend = (list(combinations(CentralSouth_stores_Weekend, 6)))

for i in range(len(CentralSouth_Routes2_Weekend)):
    store1 = CentralSouth_Routes2_Weekend[i][0]
    store2 = CentralSouth_Routes2_Weekend[i][1]
    demand_weekend = 0
    time_weekend = 0

    for j in range(len(CentralSouth_stores_Weekend)):
        if store1 == CentralSouth_stores_Weekend[j]:
            demand_weekend += CentralSouth_WeekendDemands[j]
            time_weekend += CentralSouth_WeekendDemands[j] * 450

    for k in range(len(CentralSouth_stores_Weekend)):
        if store2 == CentralSouth_stores_Weekend[k]:
            demand_weekend += CentralSouth_WeekendDemands[k]
            time_weekend += CentralSouth_WeekendDemands[k] * 450

    for store in range(len(stores)):
        if store1 == stores[store]:
            time_weekend += distribution_time[store]
        if store2 == stores[store]:
            time_weekend += distribution_time[store]

    for store_row in range(len(stores)):
        if store1 == stores[store_row]:
            for store_col in range(len(stores)):
                if store2 == stores[store_col]:
                    time_weekend += travel_durations[store_row][store_col]

    if (demand_weekend < demand_threshold and time_weekend <= time_threshold):
        CentralSouthRoutes_Weekend.append(CentralSouth_Routes2_Weekend[i])
        Routes_Weekend.append(CentralSouth_Routes2_Weekend[i])
        Time_Weekend.append(time_weekend/60/60)

for i in range(len(CentralSouth_Routes3_Weekend)):
    store1 = CentralSouth_Routes3_Weekend[i][0]
    store2 = CentralSouth_Routes3_Weekend[i][1]
    store3 = CentralSouth_Routes3_Weekend[i][2]
    demand_weekend = 0
    time_weekend = 0

    for j in range(len(CentralSouth_stores_Weekend)):
        if store1 == CentralSouth_stores_Weekend[j]:
            demand_weekend += CentralSouth_WeekendDemands[j]
            time_weekend += CentralSouth_WeekendDemands[j] * 450

    for k in range(len(CentralSouth_stores_Weekend)):
        if store2 == CentralSouth_stores_Weekend[k]:
            demand_weekend += CentralSouth_WeekendDemands[k]
            time_weekend += CentralSouth_WeekendDemands[k] * 450

    for l in range(len(CentralSouth_stores_Weekend)):
        if store3 == CentralSouth_stores_Weekend[l]:
            demand_weekend += CentralSouth_WeekendDemands[l]
            time_weekend += CentralSouth_WeekendDemands[l] * 450

    for store in range(len(stores)):
        if store1 == stores[store]:
            time_weekend += distribution_time[store]
        if store3 == stores[store]:
            time_weekend += distribution_time[store]

    for store_row in range(len(stores)):
        if store1 == stores[store_row]:
            for store_col in range(len(stores)):
                if store2 == stores[store_col]:
                    time_weekend += travel_durations[store_row][store_col]

    for store_row in range(len(stores)):
        if store2 == stores[store_row]:
            for store_col in range(len(stores)):
                if store3 == stores[store_col]:
                    time_weekend += travel_durations[store_row][store_col]

    if (demand_weekend < demand_threshold and time_weekend <= time_threshold):
        CentralSouthRoutes_Weekend.append(CentralSouth_Routes3_Weekend[i])
        Routes_Weekend.append(CentralSouth_Routes3_Weekend[i])
        Time_Weekend.append(time_weekend/60/60)

for i in range(len(CentralSouth_Routes4_Weekend)):
    
    store1 = CentralSouth_Routes4_Weekend[i][0]
    store2 = CentralSouth_Routes4_Weekend[i][1]
    store3 = CentralSouth_Routes4_Weekend[i][2]
    store4 = CentralSouth_Routes4_Weekend[i][3]
    demand_weekend = 0
    time_weekend = 0

    for j in range(len(CentralSouth_stores_Weekend)):
        if store1 == CentralSouth_stores_Weekend[j]:
            demand_weekend += CentralSouth_WeekendDemands[j]
            time_weekend += CentralSouth_WeekendDemands[j] * 450

    for k in range(len(CentralSouth_stores_Weekend)):
        if store2 == CentralSouth_stores_Weekend[k]:
            demand_weekend += CentralSouth_WeekendDemands[k]
            time_weekend += CentralSouth_WeekendDemands[k] * 450

    for l in range(len(CentralSouth_stores_Weekend)):
        if store3 == CentralSouth_stores_Weekend[l]:
            demand_weekend += CentralSouth_WeekendDemands[l]
            time_weekend += CentralSouth_WeekendDemands[l] * 450

    for m in range(len(CentralSouth_stores_Weekend)):
        if store4 == CentralSouth_stores_Weekend[m]:
            demand_weekend += CentralSouth_WeekendDemands[m]
            time_weekend += CentralSouth_WeekendDemands[m] * 450

    for store in range(len(stores)):
        if store1 == stores[store]:
            time_weekend += distribution_time[store]
        if store4 == stores[store]:
            time_weekend += distribution_time[store]

    for store_row in range(len(stores)):
        if store1 == stores[store_row]:
            for store_col in range(len(stores)):
                if store2 == stores[store_col]:
                    time_weekend += travel_durations[store_row][store_col]

    for store_row in range(len(stores)):
        if store2 == stores[store_row]:
            for store_col in range(len(stores)):
                if store3 == stores[store_col]:
                    time_weekend += travel_durations[store_row][store_col]

    for store_row in range(len(stores)):
        if store3 == stores[store_row]:
            for store_col in range(len(stores)):
                if store4 == stores[store_col]:
                    time_weekend += travel_durations[store_row][store_col]

    if (demand_weekend < demand_threshold and time_weekend <= time_threshold):
        CentralSouthRoutes_Weekend.append(CentralSouth_Routes4_Weekend[i])
        Routes_Weekend.append(CentralSouth_Routes4_Weekend[i])
        Time_Weekend.append(time_weekend/60/60)

for i in range(len(CentralSouth_Routes5_Weekend)):
    store1 = CentralSouth_Routes5_Weekend[i][0]
    store2 = CentralSouth_Routes5_Weekend[i][1]
    store3 = CentralSouth_Routes5_Weekend[i][2]
    store4 = CentralSouth_Routes5_Weekend[i][3]
    store5 = CentralSouth_Routes5_Weekend[i][4]

    demand_weekend = 0
    time_weekend = 0

    for j in range(len(CentralSouth_stores_Weekend)):
        if store1 == CentralSouth_stores_Weekend[j]:
            demand_weekend += CentralSouth_WeekendDemands[j]
            time_weekend += CentralSouth_WeekendDemands[j] * 450

    for k in range(len(CentralSouth_stores_Weekend)):
        if store2 == CentralSouth_stores_Weekend[k]:
            demand_weekend += CentralSouth_WeekendDemands[k]
            time_weekend += CentralSouth_WeekendDemands[k] * 450

    for l in range(len(CentralSouth_stores_Weekend)):
        if store3 == CentralSouth_stores_Weekend[l]:
            demand_weekend += CentralSouth_WeekendDemands[l]
            time_weekend += CentralSouth_WeekendDemands[l] * 450

    for m in range(len(CentralSouth_stores_Weekend)):
        if store4 == CentralSouth_stores_Weekend[m]:
            demand_weekend += CentralSouth_WeekendDemands[m]
            time_weekend += CentralSouth_WeekendDemands[m] * 450

    for n in range(len(CentralSouth_stores_Weekend)):
        if store5 == CentralSouth_stores_Weekend[n]:
            demand_weekend += CentralSouth_WeekendDemands[n]
            time_weekend += CentralSouth_WeekendDemands[n] * 450

    for store in range(len(stores)):
        if store1 == stores[store]:
            time_weekend += distribution_time[store]
        if store5 == stores[store]:
            time_weekend += distribution_time[store]

    for store_row in range(len(stores)):
        if store1 == stores[store_row]:
            for store_col in range(len(stores)):
                if store2 == stores[store_col]:
                    time_weekend += travel_durations[store_row][store_col]

    for store_row in range(len(stores)):
        if store2 == stores[store_row]:
            for store_col in range(len(stores)):
                if store3 == stores[store_col]:
                    time_weekend += travel_durations[store_row][store_col]

    for store_row in range(len(stores)):
        if store3 == stores[store_row]:
            for store_col in range(len(stores)):
                if store4 == stores[store_col]:
                    time_weekend += travel_durations[store_row][store_col]

    for store_row in range(len(stores)):
        if store4 == stores[store_row]:
            for store_col in range(len(stores)):
                if store5 == stores[store_col]:
                    time_weekend += travel_durations[store_row][store_col]

    if (demand_weekend < demand_threshold and time_weekend <= time_threshold):
        CentralSouthRoutes_Weekend.append(CentralSouth_Routes5_Weekend[i])
        Routes_Weekend.append(CentralSouth_Routes5_Weekend[i])
        Time_Weekend.append(time_weekend/60/60)

for i in range(len(CentralSouth_Routes6_Weekend)):
    store1 = CentralSouth_Routes6_Weekend[i][0]
    store2 = CentralSouth_Routes6_Weekend[i][1]
    store3 = CentralSouth_Routes6_Weekend[i][2]
    store4 = CentralSouth_Routes6_Weekend[i][3]
    store5 = CentralSouth_Routes6_Weekend[i][4]
    store6 = CentralSouth_Routes6_Weekend[i][5]

    demand_weekend = 0
    time_weekend = 0

    for j in range(len(CentralSouth_stores_Weekend)):
        if store1 == CentralSouth_stores_Weekend[j]:
            demand_weekend += CentralSouth_WeekendDemands[j]
            time_weekend += CentralSouth_WeekendDemands[j] * 450

    for k in range(len(CentralSouth_stores_Weekend)):
        if store2 == CentralSouth_stores_Weekend[k]:
            demand_weekend += CentralSouth_WeekendDemands[k]
            time_weekend += CentralSouth_WeekendDemands[k] * 450

    for l in range(len(CentralSouth_stores_Weekend)):
        if store3 == CentralSouth_stores_Weekend[l]:
            demand_weekend += CentralSouth_WeekendDemands[l]
            time_weekend += CentralSouth_WeekendDemands[l] * 450

    for m in range(len(CentralSouth_stores_Weekend)):
        if store4 == CentralSouth_stores_Weekend[m]:
            demand_weekend += CentralSouth_WeekendDemands[m]
            time_weekend += CentralSouth_WeekendDemands[m] * 450

    for n in range(len(CentralSouth_stores_Weekend)):
        if store5 == CentralSouth_stores_Weekend[n]:
            demand_weekend += CentralSouth_WeekendDemands[n]
            time_weekend += CentralSouth_WeekendDemands[n] * 450

    for o in range(len(CentralSouth_stores_Weekend)):
        if store6 == CentralSouth_stores_Weekend[o]:
            demand_weekend += CentralSouth_WeekendDemands[o]
            time_weekend += CentralSouth_WeekendDemands[o] * 450

    for store in range(len(stores)):
        if store1 == stores[store]:
            time_weekend += distribution_time[store]
        if store5 == stores[store]:
            time_weekend += distribution_time[store]

    for store_row in range(len(stores)):
        if store1 == stores[store_row]:
            for store_col in range(len(stores)):
                if store2 == stores[store_col]:
                    time_weekend += travel_durations[store_row][store_col]

    for store_row in range(len(stores)):
        if store2 == stores[store_row]:
            for store_col in range(len(stores)):
                if store3 == stores[store_col]:
                    time_weekend += travel_durations[store_row][store_col]

    for store_row in range(len(stores)):
        if store3 == stores[store_row]:
            for store_col in range(len(stores)):
                if store4 == stores[store_col]:
                    time_weekend += travel_durations[store_row][store_col]

    for store_row in range(len(stores)):
        if store4 == stores[store_row]:
            for store_col in range(len(stores)):
                if store5 == stores[store_col]:
                    time_weekend += travel_durations[store_row][store_col]

    for store_row in range(len(stores)):
        if store5 == stores[store_row]:
            for store_col in range(len(stores)):
                if store6 == stores[store_col]:
                    time_weekend += travel_durations[store_row][store_col]

    if (demand_weekend < demand_threshold and time_weekend <= time_threshold):
        CentralSouthRoutes_Weekend.append(CentralSouth_Routes6_Weekend[i])
        Routes_Weekend.append(CentralSouth_Routes6_Weekend[i])
        Time_Weekend.append(time_weekend/60/60)

North_Routes2_Weekend = (list(combinations(North_stores_Weekend, 2)))
North_Routes3_Weekend = (list(combinations(North_stores_Weekend, 3)))
North_Routes4_Weekend = (list(combinations(North_stores_Weekend, 4)))
North_Routes5_Weekend = (list(combinations(North_stores_Weekend, 5)))
North_Routes6_Weekend = (list(combinations(North_stores_Weekend, 6)))

for i in range(len(North_Routes2_Weekend)):
    store1 = North_Routes2_Weekend[i][0]
    store2 = North_Routes2_Weekend[i][1]
    demand_weekend = 0
    time_weekend = 0

    for j in range(len(North_stores_Weekend)):
        if store1 == North_stores_Weekend[j]:
            demand_weekend += North_WeekendDemands[j]
            time_weekend += North_WeekendDemands[j] * 450

    for k in range(len(North_stores_Weekend)):
        if store2 == North_stores_Weekend[k]:
            demand_weekend += North_WeekendDemands[k]
            time_weekend += North_WeekendDemands[k] * 450

    for store in range(len(stores)):
        if store1 == stores[store]:
            time_weekend += distribution_time[store]
        if store2 == stores[store]:
            time_weekend += distribution_time[store]

    for store_row in range(len(stores)):
        if store1 == stores[store_row]:
            for store_col in range(len(stores)):
                if store2 == stores[store_col]:
                    time_weekend += travel_durations[store_row][store_col]

    if (demand_weekend < demand_threshold and time_weekend <= time_threshold):
        NorthRoutes_Weekend.append(North_Routes2_Weekend[i])
        Routes_Weekend.append(North_Routes2_Weekend[i])
        Time_Weekend.append(time_weekend/60/60)

for i in range(len(North_Routes3_Weekend)):
    store1 = North_Routes3_Weekend[i][0]
    store2 = North_Routes3_Weekend[i][1]
    store3 = North_Routes3_Weekend[i][2]
    demand_weekend = 0
    time_weekend = 0

    for j in range(len(North_stores_Weekend)):
        if store1 == North_stores_Weekend[j]:
            demand_weekend += North_WeekendDemands[j]
            time_weekend += North_WeekendDemands[j] * 450

    for k in range(len(North_stores_Weekend)):
        if store2 == North_stores_Weekend[k]:
            demand_weekend += North_WeekendDemands[k]
            time_weekend += North_WeekendDemands[k] * 450

    for l in range(len(North_stores_Weekend)):
        if store3 == North_stores_Weekend[l]:
            demand_weekend += North_WeekendDemands[l]
            time_weekend += North_WeekendDemands[l] * 450

    for store in range(len(stores)):
        if store1 == stores[store]:
            time_weekend += distribution_time[store]
        if store3 == stores[store]:
            time_weekend += distribution_time[store]

    for store_row in range(len(stores)):
        if store1 == stores[store_row]:
            for store_col in range(len(stores)):
                if store2 == stores[store_col]:
                    time_weekend += travel_durations[store_row][store_col]

    for store_row in range(len(stores)):
        if store2 == stores[store_row]:
            for store_col in range(len(stores)):
                if store3 == stores[store_col]:
                    time_weekend += travel_durations[store_row][store_col]

    if (demand_weekend < demand_threshold and time_weekend <= time_threshold):
        NorthRoutes_Weekend.append(North_Routes3_Weekend[i])
        Routes_Weekend.append(North_Routes3_Weekend[i])
        Time_Weekend.append(time_weekend/60/60)

for i in range(len(North_Routes4_Weekend)):
    store1 = North_Routes4_Weekend[i][0]
    store2 = North_Routes4_Weekend[i][1]
    store3 = North_Routes4_Weekend[i][2]
    store4 = North_Routes4_Weekend[i][3]
    demand_weekend = 0
    time_weekend = 0

    for j in range(len(North_stores_Weekend)):
        if store1 == North_stores_Weekend[j]:
            demand_weekend += North_WeekendDemands[j]
            time_weekend += North_WeekendDemands[j] * 450

    for k in range(len(North_stores_Weekend)):
        if store2 == North_stores_Weekend[k]:
            demand_weekend += North_WeekendDemands[k]
            time_weekend += North_WeekendDemands[k] * 450

    for l in range(len(North_stores_Weekend)):
        if store3 == North_stores_Weekend[l]:
            demand_weekend += North_WeekendDemands[l]
            time_weekend += North_WeekendDemands[l] * 450

    for m in range(len(North_stores_Weekend)):
        if store4 == North_stores_Weekend[m]:
            demand_weekend += North_WeekendDemands[m]
            time_weekend += North_WeekendDemands[m] * 450

    for store in range(len(stores)):
        if store1 == stores[store]:
            time_weekend += distribution_time[store]
        if store4 == stores[store]:
            time_weekend += distribution_time[store]

    for store_row in range(len(stores)):
        if store1 == stores[store_row]:
            for store_col in range(len(stores)):
                if store2 == stores[store_col]:
                    time_weekend += travel_durations[store_row][store_col]

    for store_row in range(len(stores)):
        if store2 == stores[store_row]:
            for store_col in range(len(stores)):
                if store3 == stores[store_col]:
                    time_weekend += travel_durations[store_row][store_col]

    for store_row in range(len(stores)):
        if store3 == stores[store_row]:
            for store_col in range(len(stores)):
                if store4 == stores[store_col]:
                    time_weekend += travel_durations[store_row][store_col]

    if (demand_weekend < demand_threshold and time_weekend <= time_threshold):
        NorthRoutes_Weekend.append(North_Routes4_Weekend[i])
        Routes_Weekend.append(North_Routes4_Weekend[i])
        Time_Weekend.append(time_weekend/60/60)

for i in range(len(North_Routes5_Weekend)):
    store1 = North_Routes5_Weekend[i][0]
    store2 = North_Routes5_Weekend[i][1]
    store3 = North_Routes5_Weekend[i][2]
    store4 = North_Routes5_Weekend[i][3]
    store5 = North_Routes5_Weekend[i][4]

    demand_weekend = 0
    time_weekend = 0

    for j in range(len(North_stores_Weekend)):
        if store1 == North_stores_Weekend[j]:
            demand_weekend += North_WeekendDemands[j]
            time_weekend += North_WeekendDemands[j] * 450

    for k in range(len(North_stores_Weekend)):
        if store2 == North_stores_Weekend[k]:
            demand_weekend += North_WeekendDemands[k]
            time_weekend += North_WeekendDemands[k] * 450

    for l in range(len(North_stores_Weekend)):
        if store3 == North_stores_Weekend[l]:
            demand_weekend += North_WeekendDemands[l]
            time_weekend += North_WeekendDemands[l] * 450

    for m in range(len(North_stores_Weekend)):
        if store4 == North_stores_Weekend[m]:
            demand_weekend += North_WeekendDemands[m]
            time_weekend += North_WeekendDemands[m] * 450

    for n in range(len(North_stores_Weekend)):
        if store4 == North_stores_Weekend[n]:
            demand_weekend += North_WeekendDemands[n]
            time_weekend += North_WeekendDemands[n] * 450
            
    for store in range(len(stores)):
        if store1 == stores[store]:
            time_weekend += distribution_time[store]
        if store5 == stores[store]:
            time_weekend += distribution_time[store]

    for store_row in range(len(stores)):
        if store1 == stores[store_row]:
            for store_col in range(len(stores)):
                if store2 == stores[store_col]:
                    time_weekend += travel_durations[store_row][store_col]

    for store_row in range(len(stores)):
        if store2 == stores[store_row]:
            for store_col in range(len(stores)):
                if store3 == stores[store_col]:
                    time_weekend += travel_durations[store_row][store_col]

    for store_row in range(len(stores)):
        if store3 == stores[store_row]:
            for store_col in range(len(stores)):
                if store4 == stores[store_col]:
                    time_weekend += travel_durations[store_row][store_col]

    for store_row in range(len(stores)):
        if store4 == stores[store_row]:
            for store_col in range(len(stores)):
                if store5 == stores[store_col]:
                    time_weekend += travel_durations[store_row][store_col]

    if (demand_weekend < demand_threshold and time_weekend <= time_threshold):
        NorthRoutes_Weekend.append(North_Routes5_Weekend[i])
        Routes_Weekend.append(North_Routes5_Weekend[i])
        Time_Weekend.append(time_weekend/60/60)

for i in range(len(North_Routes6_Weekend)):
    store1 = North_Routes6_Weekend[i][0]
    store2 = North_Routes6_Weekend[i][1]
    store3 = North_Routes6_Weekend[i][2]
    store4 = North_Routes6_Weekend[i][3]
    store5 = North_Routes6_Weekend[i][4]
    store6 = North_Routes6_Weekend[i][5]

    demand_weekend = 0
    time_weekend = 0

    for j in range(len(North_stores_Weekend)):
        if store1 == North_stores_Weekend[j]:
            demand_weekend += North_WeekendDemands[j]
            time_weekend += North_WeekendDemands[j] * 450

    for k in range(len(North_stores_Weekend)):
        if store2 == North_stores_Weekend[k]:
            demand_weekend += North_WeekendDemands[k]
            time_weekend += North_WeekendDemands[k] * 450

    for l in range(len(North_stores_Weekend)):
        if store3 == North_stores_Weekend[l]:
            demand_weekend += North_WeekendDemands[l]
            time_weekend += North_WeekendDemands[l] * 450

    for m in range(len(North_stores_Weekend)):
        if store4 == North_stores_Weekend[m]:
            demand_weekend += North_WeekendDemands[m]
            time_weekend += North_WeekendDemands[m] * 450

    for n in range(len(North_stores_Weekend)):
        if store5 == North_stores_Weekend[n]:
            demand_weekend += North_WeekendDemands[n]
            time_weekend += North_WeekendDemands[n] * 450

    for o in range(len(North_stores_Weekend)):
        if store6 == North_stores_Weekend[o]:
            demand_weekend += North_WeekendDemands[o]
            time_weekend += North_WeekendDemands[o] * 450

    for store in range(len(stores)):
        if store1 == stores[store]:
            time_weekend += distribution_time[store]
        if store5 == stores[store]:
            time_weekend += distribution_time[store]

    for store_row in range(len(stores)):
        if store1 == stores[store_row]:
            for store_col in range(len(stores)):
                if store2 == stores[store_col]:
                    time_weekend += travel_durations[store_row][store_col]

    for store_row in range(len(stores)):
        if store2 == stores[store_row]:
            for store_col in range(len(stores)):
                if store3 == stores[store_col]:
                    time_weekend += travel_durations[store_row][store_col]

    for store_row in range(len(stores)):
        if store3 == stores[store_row]:
            for store_col in range(len(stores)):
                if store4 == stores[store_col]:
                    time_weekend += travel_durations[store_row][store_col]

    for store_row in range(len(stores)):
        if store4 == stores[store_row]:
            for store_col in range(len(stores)):
                if store5 == stores[store_col]:
                    time_weekend += travel_durations[store_row][store_col]

    for store_row in range(len(stores)):
        if store5 == stores[store_row]:
            for store_col in range(len(stores)):
                if store6 == stores[store_col]:
                    time_weekend += travel_durations[store_row][store_col]

    if (demand_weekend < demand_threshold and time_weekend <= time_threshold):
        NorthRoutes_Weekend.append(North_Routes6_Weekend[i])
        Routes_Weekend.append(North_Routes6_Weekend[i])
        Time_Weekend.append(time_weekend/60/60)

South_Routes2_Weekend = (list(combinations(South_stores_Weekend, 2)))
South_Routes3_Weekend = (list(combinations(South_stores_Weekend, 3)))
South_Routes4_Weekend = (list(combinations(South_stores_Weekend, 4)))
South_Routes5_Weekend = (list(combinations(South_stores_Weekend, 5)))
South_Routes6_Weekend = (list(combinations(South_stores_Weekend, 6)))

for i in range(len(South_Routes2_Weekend)):
    store1 = South_Routes2_Weekend[i][0]
    store2 = South_Routes2_Weekend[i][1]
    demand_weekend = 0
    time_weekend = 0

    for j in range(len(South_stores_Weekend)):
        if store1 == South_stores_Weekend[j]:
            demand_weekend += South_WeekendDemands[j]
            time_weekend += South_WeekendDemands[j] * 450

    for k in range(len(South_stores_Weekend)):
        if store2 == South_stores_Weekend[k]:
            demand_weekend += South_WeekendDemands[k]
            time_weekend += South_WeekendDemands[k] * 450

    for store in range(len(stores)):
        if store1 == stores[store]:
            time_weekend += distribution_time[store]
        if store2 == stores[store]:
            time_weekend += distribution_time[store]

    for store_row in range(len(stores)):
        if store1 == stores[store_row]:
            for store_col in range(len(stores)):
                if store2 == stores[store_col]:
                    time_weekend += travel_durations[store_row][store_col]

    if (demand_weekend < demand_threshold and time_weekend <= time_threshold):
        SouthRoutes_Weekend.append(South_Routes2_Weekend[i])
        Routes_Weekend.append(South_Routes2_Weekend[i])
        Time_Weekend.append(time_weekend/60/60)

for i in range(len(South_Routes3_Weekend)):
    store1 = South_Routes3_Weekend[i][0]
    store2 = South_Routes3_Weekend[i][1]
    store3 = South_Routes3_Weekend[i][2]
    demand_weekend = 0
    time_weekend = 0

    for j in range(len(South_stores_Weekend)):
        if store1 == South_stores_Weekend[j]:
            demand_weekend += South_WeekendDemands[j]
            time_weekend += South_WeekendDemands[j] * 450

    for k in range(len(South_stores_Weekend)):
        if store2 == South_stores_Weekend[k]:
            demand_weekend += South_WeekendDemands[k]
            time_weekend += South_WeekendDemands[k] * 450

    for l in range(len(South_stores_Weekend)):
        if store3 == South_stores_Weekend[l]:
            demand_weekend += South_WeekendDemands[l]
            time_weekend += South_WeekendDemands[l] * 450

    for store in range(len(stores)):
        if store1 == stores[store]:
            time_weekend += distribution_time[store]
        if store3 == stores[store]:
            time_weekend += distribution_time[store]

    for store_row in range(len(stores)):
        if store1 == stores[store_row]:
            for store_col in range(len(stores)):
                if store2 == stores[store_col]:
                    time_weekend += travel_durations[store_row][store_col]

    for store_row in range(len(stores)):
        if store2 == stores[store_row]:
            for store_col in range(len(stores)):
                if store3 == stores[store_col]:
                    time_weekend += travel_durations[store_row][store_col]

    if (demand_weekend < demand_threshold and time_weekend <= time_threshold):
        SouthRoutes_Weekend.append(South_Routes3_Weekend[i])
        Routes_Weekend.append(South_Routes3_Weekend[i])
        Time_Weekend.append(time_weekend/60/60)

for i in range(len(South_Routes4_Weekend)):
    store1 = South_Routes4_Weekend[i][0]
    store2 = South_Routes4_Weekend[i][1]
    store3 = South_Routes4_Weekend[i][2]
    store4 = South_Routes4_Weekend[i][3]
    demand_weekend = 0
    time_weekend = 0

    for j in range(len(South_stores_Weekend)):
        if store1 == South_stores_Weekend[j]:
            demand_weekend += South_WeekendDemands[j]
            time_weekend += South_WeekendDemands[j] * 450

    for k in range(len(South_stores_Weekend)):
        if store2 == South_stores_Weekend[k]:
            demand_weekend += South_WeekendDemands[k]
            time_weekend += South_WeekendDemands[k] * 450

    for l in range(len(South_stores_Weekend)):
        if store3 == South_stores_Weekend[l]:
            demand_weekend += South_WeekendDemands[l]
            time_weekend += South_WeekendDemands[l] * 450

    for m in range(len(South_stores_Weekend)):
        if store4 == South_stores_Weekend[m]:
            demand_weekend += South_WeekendDemands[m]
            time_weekend += South_WeekendDemands[m] * 450

    for store in range(len(stores)):
        if store1 == stores[store]:
            time_weekend += distribution_time[store]
        if store4 == stores[store]:
            time_weekend += distribution_time[store]

    for store_row in range(len(stores)):
        if store1 == stores[store_row]:
            for store_col in range(len(stores)):
                if store2 == stores[store_col]:
                    time_weekend += travel_durations[store_row][store_col]

    for store_row in range(len(stores)):
        if store2 == stores[store_row]:
            for store_col in range(len(stores)):
                if store3 == stores[store_col]:
                    time_weekend += travel_durations[store_row][store_col]

    for store_row in range(len(stores)):
        if store3 == stores[store_row]:
            for store_col in range(len(stores)):
                if store4 == stores[store_col]:
                    time_weekend += travel_durations[store_row][store_col]

    if (demand_weekend < demand_threshold and time_weekend <= time_threshold):
        SouthRoutes_Weekend.append(South_Routes4_Weekend[i])
        Routes_Weekend.append(South_Routes4_Weekend[i])
        Time_Weekend.append(time_weekend/60/60)

for i in range(len(South_Routes5_Weekend)):
    store1 = South_Routes5_Weekend[i][0]
    store2 = South_Routes5_Weekend[i][1]
    store3 = South_Routes5_Weekend[i][2]
    store4 = South_Routes5_Weekend[i][3]
    store5 = South_Routes5_Weekend[i][4]

    demand_weekend = 0
    time_weekend = 0

    for j in range(len(South_stores_Weekend)):
        if store1 == South_stores_Weekend[j]:
            demand_weekend += South_WeekendDemands[j]
            time_weekend += South_WeekendDemands[j] * 450

    for k in range(len(South_stores_Weekend)):
        if store2 == South_stores_Weekend[k]:
            demand_weekend += South_WeekendDemands[k]
            time_weekend += South_WeekendDemands[k] * 450

    for l in range(len(South_stores_Weekend)):
        if store3 == South_stores_Weekend[l]:
            demand_weekend += South_WeekendDemands[l]
            time_weekend += South_WeekendDemands[l] * 450

    for m in range(len(South_stores_Weekend)):
        if store4 == South_stores_Weekend[m]:
            demand_weekend += South_WeekendDemands[m]
            time_weekend += South_WeekendDemands[m] * 450

    for n in range(len(South_stores_Weekend)):
        if store5 == South_stores_Weekend[n]:
            demand_weekend += South_WeekendDemands[n]
            time_weekend += South_WeekendDemands[n] * 450

    for store in range(len(stores)):
        if store1 == stores[store]:
            time_weekend += distribution_time[store]
        if store5 == stores[store]:
            time_weekend += distribution_time[store]

    for store_row in range(len(stores)):
        if store1 == stores[store_row]:
            for store_col in range(len(stores)):
                if store2 == stores[store_col]:
                    time_weekend += travel_durations[store_row][store_col]

    for store_row in range(len(stores)):
        if store2 == stores[store_row]:
            for store_col in range(len(stores)):
                if store3 == stores[store_col]:
                    time_weekend += travel_durations[store_row][store_col]

    for store_row in range(len(stores)):
        if store3 == stores[store_row]:
            for store_col in range(len(stores)):
                if store4 == stores[store_col]:
                    time_weekend += travel_durations[store_row][store_col]

    for store_row in range(len(stores)):
        if store4 == stores[store_row]:
            for store_col in range(len(stores)):
                if store5 == stores[store_col]:
                    time_weekend += travel_durations[store_row][store_col]

    if (demand_weekend < demand_threshold and time_weekend <= time_threshold):
        SouthRoutes_Weekend.append(South_Routes5_Weekend[i])
        Routes_Weekend.append(South_Routes5_Weekend[i])
        Time_Weekend.append(time_weekend/60/60)

for i in range(len(South_Routes6_Weekend)):
    store1 = South_Routes6_Weekend[i][0]
    store2 = South_Routes6_Weekend[i][1]
    store3 = South_Routes6_Weekend[i][2]
    store4 = South_Routes6_Weekend[i][3]
    store5 = South_Routes6_Weekend[i][4]
    store6 = South_Routes6_Weekend[i][5]

    demand_weekend = 0
    time_weekend = 0

    for j in range(len(South_stores_Weekend)):
        if store1 == South_stores_Weekend[j]:
            demand_weekend += South_WeekendDemands[j]
            time_weekend += South_WeekendDemands[j] * 450

    for k in range(len(South_stores_Weekend)):
        if store2 == South_stores_Weekend[k]:
            demand_weekend += South_WeekendDemands[k]
            time_weekend += South_WeekendDemands[k] * 450

    for l in range(len(South_stores_Weekend)):
        if store3 == South_stores_Weekend[l]:
            demand_weekend += South_WeekendDemands[l]
            time_weekend += South_WeekendDemands[l] * 450

    for m in range(len(South_stores_Weekend)):
        if store4 == South_stores_Weekend[m]:
            demand_weekend += South_WeekendDemands[m]
            time_weekend += South_WeekendDemands[m] * 450

    for n in range(len(South_stores_Weekend)):
        if store5 == South_stores_Weekend[n]:
            demand_weekend += South_WeekendDemands[n]
            time_weekend += South_WeekendDemands[n] * 450

    for o in range(len(South_stores_Weekend)):
        if store6 == South_stores_Weekend[o]:
            demand_weekend += South_WeekendDemands[o]
            time_weekend += South_WeekendDemands[o] * 450

    for store in range(len(stores)):
        if store1 == stores[store]:
            time_weekend += distribution_time[store]
        if store5 == stores[store]:
            time_weekend += distribution_time[store]

    for store_row in range(len(stores)):
        if store1 == stores[store_row]:
            for store_col in range(len(stores)):
                if store2 == stores[store_col]:
                    time_weekend += travel_durations[store_row][store_col]

    for store_row in range(len(stores)):
        if store2 == stores[store_row]:
            for store_col in range(len(stores)):
                if store3 == stores[store_col]:
                    time_weekend += travel_durations[store_row][store_col]

    for store_row in range(len(stores)):
        if store3 == stores[store_row]:
            for store_col in range(len(stores)):
                if store4 == stores[store_col]:
                    time_weekend += travel_durations[store_row][store_col]

    for store_row in range(len(stores)):
        if store4 == stores[store_row]:
            for store_col in range(len(stores)):
                if store5 == stores[store_col]:
                    time_weekend += travel_durations[store_row][store_col]

    for store_row in range(len(stores)):
        if store5 == stores[store_row]:
            for store_col in range(len(stores)):
                if store6 == stores[store_col]:
                    time_weekend += travel_durations[store_row][store_col]

    if (demand_weekend < demand_threshold and time_weekend <= time_threshold):
        SouthRoutes_Weekend.append(South_Routes6_Weekend[i])
        Routes_Weekend.append(South_Routes6_Weekend[i])
        Time_Weekend.append(time_weekend/60/60)

West_Routes2_Weekend = (list(combinations(West_stores_Weekend, 2)))
West_Routes3_Weekend = (list(combinations(West_stores_Weekend, 3)))
West_Routes4_Weekend = (list(combinations(West_stores_Weekend, 4)))
West_Routes5_Weekend = (list(combinations(West_stores_Weekend, 5)))
West_Routes6_Weekend = (list(combinations(West_stores_Weekend, 6)))

for i in range(len(West_Routes2_Weekend)):
    store1 = West_Routes2_Weekend[i][0]
    store2 = West_Routes2_Weekend[i][1]
    demand_weekend = 0
    time_weekend = 0

    for j in range(len(West_stores_Weekend)):
        if store1 == West_stores_Weekend[j]:
            demand_weekend += West_WeekendDemands[j]
            time_weekend += West_WeekendDemands[j] * 450

    for k in range(len(West_stores_Weekend)):
        if store2 == West_stores_Weekend[k]:
            demand_weekend += West_WeekendDemands[k]
            time_weekend += West_WeekendDemands[k] * 450

    for store in range(len(stores)):
        if store1 == stores[store]:
            time_weekend += distribution_time[store]
        if store2 == stores[store]:
            time_weekend += distribution_time[store]

    for store_row in range(len(stores)):
        if store1 == stores[store_row]:
            for store_col in range(len(stores)):
                if store2 == stores[store_col]:
                    time_weekend += travel_durations[store_row][store_col]

    if (demand_weekend < demand_threshold and time_weekend <= time_threshold):
        WestRoutes_Weekend.append(West_Routes2_Weekend[i])
        Routes_Weekend.append(West_Routes2_Weekend[i])
        Time_Weekend.append(time_weekend/60/60)

for i in range(len(West_Routes3_Weekend)):
    store1 = West_Routes3_Weekend[i][0]
    store2 = West_Routes3_Weekend[i][1]
    store3 = West_Routes3_Weekend[i][2]
    demand_weekend = 0
    time_weekend = 0

    for j in range(len(West_stores_Weekend)):
        if store1 == West_stores_Weekend[j]:
            demand_weekend += West_WeekendDemands[j]
            time_weekend += West_WeekendDemands[j] * 450

    for k in range(len(West_stores_Weekend)):
        if store2 == West_stores_Weekend[k]:
            demand_weekend += West_WeekendDemands[k]
            time_weekend += West_WeekendDemands[k] * 450

    for l in range(len(West_stores_Weekend)):
        if store3 == West_stores_Weekend[l]:
            demand_weekend += West_WeekendDemands[l]
            time_weekend += West_WeekendDemands[l] * 450

    for store in range(len(stores)):
        if store1 == stores[store]:
            time_weekend += distribution_time[store]
        if store3 == stores[store]:
            time_weekend += distribution_time[store]

    for store_row in range(len(stores)):
        if store1 == stores[store_row]:
            for store_col in range(len(stores)):
                if store2 == stores[store_col]:
                    time_weekend += travel_durations[store_row][store_col]

    for store_row in range(len(stores)):
        if store2 == stores[store_row]:
            for store_col in range(len(stores)):
                if store3 == stores[store_col]:
                    time_weekend += travel_durations[store_row][store_col]

    if (demand_weekend < demand_threshold and time_weekend <= time_threshold):
        WestRoutes_Weekend.append(West_Routes3_Weekend[i])
        Routes_Weekend.append(West_Routes3_Weekend[i])
        Time_Weekend.append(time_weekend/60/60)

for i in range(len(West_Routes4_Weekend)):
    store1 = West_Routes4_Weekend[i][0]
    store2 = West_Routes4_Weekend[i][1]
    store3 = West_Routes4_Weekend[i][2]
    store4 = West_Routes4_Weekend[i][3]
    demand_weekend = 0
    time_weekend = 0

    for j in range(len(West_stores_Weekend)):
        if store1 == West_stores_Weekend[j]:
            demand_weekend += West_WeekendDemands[j]
            time_weekend += West_WeekendDemands[j] * 450

    for k in range(len(West_stores_Weekend)):
        if store2 == West_stores_Weekend[k]:
            demand_weekend += West_WeekendDemands[k]
            time_weekend += West_WeekendDemands[k] * 450

    for l in range(len(West_stores_Weekend)):
        if store3 == West_stores_Weekend[l]:
            demand_weekend += West_WeekendDemands[l]
            time_weekend += West_WeekendDemands[l] * 450

    for m in range(len(West_stores_Weekend)):
        if store4 == West_stores_Weekend[m]:
            demand_weekend += West_WeekendDemands[m]
            time_weekend += West_WeekendDemands[m] * 450

    for store in range(len(stores)):
        if store1 == stores[store]:
            time_weekend += distribution_time[store]
        if store4 == stores[store]:
            time_weekend += distribution_time[store]

    for store_row in range(len(stores)):
        if store1 == stores[store_row]:
            for store_col in range(len(stores)):
                if store2 == stores[store_col]:
                    time_weekend += travel_durations[store_row][store_col]

    for store_row in range(len(stores)):
        if store2 == stores[store_row]:
            for store_col in range(len(stores)):
                if store3 == stores[store_col]:
                    time_weekend += travel_durations[store_row][store_col]

    for store_row in range(len(stores)):
        if store3 == stores[store_row]:
            for store_col in range(len(stores)):
                if store4 == stores[store_col]:
                    time_weekend += travel_durations[store_row][store_col]

    if (demand_weekend < demand_threshold and time_weekend <= time_threshold):
        WestRoutes_Weekend.append(West_Routes4_Weekend[i])
        Routes_Weekend.append(West_Routes4_Weekend[i])
        Time_Weekend.append(time_weekend/60/60)

for i in range(len(West_Routes5_Weekend)):
    store1 = West_Routes5_Weekend[i][0]
    store2 = West_Routes5_Weekend[i][1]
    store3 = West_Routes5_Weekend[i][2]
    store4 = West_Routes5_Weekend[i][3]
    store5 = West_Routes5_Weekend[i][4]

    demand_weekend = 0
    time_weekend = 0

    for j in range(len(West_stores_Weekend)):
        if store1 == West_stores_Weekend[j]:
            demand_weekend += West_WeekendDemands[j]
            time_weekend += West_WeekendDemands[j] * 450

    for k in range(len(West_stores_Weekend)):
        if store2 == West_stores_Weekend[k]:
            demand_weekend += West_WeekendDemands[k]
            time_weekend += West_WeekendDemands[k] * 450

    for l in range(len(West_stores_Weekend)):
        if store3 == West_stores_Weekend[l]:
            demand_weekend += West_WeekendDemands[l]
            time_weekend += West_WeekendDemands[l] * 450

    for m in range(len(West_stores_Weekend)):
        if store4 == West_stores_Weekend[m]:
            demand_weekend += West_WeekendDemands[m]
            time_weekend += West_WeekendDemands[m] * 450

    for n in range(len(West_stores_Weekend)):
        if store5 == West_stores_Weekend[n]:
            demand_weekend += West_WeekendDemands[n]
            time_weekend += West_WeekendDemands[n] * 450

    for store in range(len(stores)):
        if store1 == stores[store]:
            time_weekend += distribution_time[store]
        if store5 == stores[store]:
            time_weekend += distribution_time[store]

    for store_row in range(len(stores)):
        if store1 == stores[store_row]:
            for store_col in range(len(stores)):
                if store2 == stores[store_col]:
                    time_weekend += travel_durations[store_row][store_col]

    for store_row in range(len(stores)):
        if store2 == stores[store_row]:
            for store_col in range(len(stores)):
                if store3 == stores[store_col]:
                    time_weekend += travel_durations[store_row][store_col]

    for store_row in range(len(stores)):
        if store3 == stores[store_row]:
            for store_col in range(len(stores)):
                if store4 == stores[store_col]:
                    time_weekend += travel_durations[store_row][store_col]

    for store_row in range(len(stores)):
        if store4 == stores[store_row]:
            for store_col in range(len(stores)):
                if store5 == stores[store_col]:
                    time_weekend += travel_durations[store_row][store_col]

    if (demand_weekend < demand_threshold and time_weekend <= time_threshold):
        WestRoutes_Weekend.append(West_Routes5_Weekend[i])
        Routes_Weekend.append(West_Routes5_Weekend[i])
        Time_Weekend.append(time_weekend/60/60)

for i in range(len(West_Routes6_Weekend)):
    store1 = West_Routes6_Weekend[i][0]
    store2 = West_Routes6_Weekend[i][1]
    store3 = West_Routes6_Weekend[i][2]
    store4 = West_Routes6_Weekend[i][3]
    store5 = West_Routes6_Weekend[i][4]
    store6 = West_Routes6_Weekend[i][5]

    demand_weekend = 0
    time_weekend = 0

    for j in range(len(West_stores_Weekend)):
        if store1 == West_stores_Weekend[j]:
            demand_weekend += West_WeekendDemands[j]
            time_weekend += West_WeekendDemands[j] * 450

    for k in range(len(West_stores_Weekend)):
        if store2 == West_stores_Weekend[k]:
            demand_weekend += West_WeekendDemands[k]
            time_weekend += West_WeekendDemands[k] * 450

    for l in range(len(West_stores_Weekend)):
        if store3 == West_stores_Weekend[l]:
            demand_weekend += West_WeekendDemands[l]
            time_weekend += West_WeekendDemands[l] * 450

    for m in range(len(West_stores_Weekend)):
        if store4 == West_stores_Weekend[m]:
            demand_weekend += West_WeekendDemands[m]
            time_weekend += West_WeekendDemands[m] * 450

    for n in range(len(West_stores_Weekend)):
        if store5 == West_stores_Weekend[n]:
            demand_weekend += West_WeekendDemands[n]
            time_weekend += West_WeekendDemands[n] * 450

    for o in range(len(West_stores_Weekend)):
        if store6 == West_stores_Weekend[o]:
            demand_weekend += West_WeekendDemands[o]
            time_weekend += West_WeekendDemands[o] * 450

    for store in range(len(stores)):
        if store1 == stores[store]:
            time_weekend += distribution_time[store]
        if store5 == stores[store]:
            time_weekend += distribution_time[store]

    for store_row in range(len(stores)):
        if store1 == stores[store_row]:
            for store_col in range(len(stores)):
                if store2 == stores[store_col]:
                    time_weekend += travel_durations[store_row][store_col]

    for store_row in range(len(stores)):
        if store2 == stores[store_row]:
            for store_col in range(len(stores)):
                if store3 == stores[store_col]:
                    time_weekend += travel_durations[store_row][store_col]

    for store_row in range(len(stores)):
        if store3 == stores[store_row]:
            for store_col in range(len(stores)):
                if store4 == stores[store_col]:
                    time_weekend += travel_durations[store_row][store_col]

    for store_row in range(len(stores)):
        if store4 == stores[store_row]:
            for store_col in range(len(stores)):
                if store5 == stores[store_col]:
                    time_weekend += travel_durations[store_row][store_col]

    for store_row in range(len(stores)):
        if store5 == stores[store_row]:
            for store_col in range(len(stores)):
                if store6 == stores[store_col]:
                    time_weekend += travel_durations[store_row][store_col]

    if (demand_weekend < demand_threshold and time_weekend <= time_threshold):
        WestRoutes_Weekend.append(West_Routes6_Weekend[i])
        Routes_Weekend.append(West_Routes6_Weekend[i])
        Time_Weekend.append(time_weekend/60/60)

East_Routes2_Weekend = (list(combinations(East_stores_Weekend, 2)))
East_Routes3_Weekend = (list(combinations(East_stores_Weekend, 3)))
East_Routes4_Weekend = (list(combinations(East_stores_Weekend, 4)))
East_Routes5_Weekend = (list(combinations(East_stores_Weekend, 5)))
East_Routes6_Weekend = (list(combinations(East_stores_Weekend, 6)))

for i in range(len(East_Routes2_Weekend)):
    store1 = East_Routes2_Weekend[i][0]
    store2 = East_Routes2_Weekend[i][1]
    demand_weekend = 0
    time_weekend = 0

    for j in range(len(East_stores_Weekend)):
        if store1 == East_stores_Weekend[j]:
            demand_weekend += East_WeekendDemands[j]
            time_weekend += East_WeekendDemands[j] * 450

    for k in range(len(East_stores_Weekend)):
        if store2 == East_stores_Weekend[k]:
            demand_weekend += East_WeekendDemands[k]
            time_weekend += East_WeekendDemands[k] * 450

    for store in range(len(stores)):
        if store1 == stores[store]:
            time_weekend += distribution_time[store]
        if store2 == stores[store]:
            time_weekend += distribution_time[store]

    for store_row in range(len(stores)):
        if store1 == stores[store_row]:
            for store_col in range(len(stores)):
                if store2 == stores[store_col]:
                    time_weekend += travel_durations[store_row][store_col]

    if (demand_weekend < demand_threshold and time_weekend <= time_threshold):
        EastRoutes_Weekend.append(East_Routes2_Weekend[i])
        Routes_Weekend.append(East_Routes2_Weekend[i])
        Time_Weekend.append(time_weekend/60/60)

for i in range(len(East_Routes3_Weekend)):
    store1 = East_Routes3_Weekend[i][0]
    store2 = East_Routes3_Weekend[i][1]
    store3 = East_Routes3_Weekend[i][2]
    demand_weekend = 0
    time_weekend = 0

    for j in range(len(East_stores_Weekend)):
        if store1 == East_stores_Weekend[j]:
            demand_weekend += East_WeekendDemands[j]
            time_weekend += East_WeekendDemands[j] * 450

    for k in range(len(East_stores_Weekend)):
        if store2 == East_stores_Weekend[k]:
            demand_weekend += East_WeekendDemands[k]
            time_weekend += East_WeekendDemands[k] * 450

    for l in range(len(East_stores_Weekend)):
        if store3 == East_stores_Weekend[l]:
            demand_weekend += East_WeekendDemands[l]
            time_weekend += East_WeekendDemands[l] * 450

    for store in range(len(stores)):
        if store1 == stores[store]:
            time_weekend += distribution_time[store]
        if store3 == stores[store]:
            time_weekend += distribution_time[store]

    for store_row in range(len(stores)):
        if store1 == stores[store_row]:
            for store_col in range(len(stores)):
                if store2 == stores[store_col]:
                    time_weekend += travel_durations[store_row][store_col]

    for store_row in range(len(stores)):
        if store2 == stores[store_row]:
            for store_col in range(len(stores)):
                if store3 == stores[store_col]:
                    time_weekend += travel_durations[store_row][store_col]

    if (demand_weekend < demand_threshold and time_weekend <= time_threshold):
        EastRoutes_Weekend.append(East_Routes3_Weekend[i])
        Routes_Weekend.append(East_Routes3_Weekend[i])
        Time_Weekend.append(time_weekend/60/60)

for i in range(len(East_Routes4_Weekend)):
    store1 = East_Routes4_Weekend[i][0]
    store2 = East_Routes4_Weekend[i][1]
    store3 = East_Routes4_Weekend[i][2]
    store4 = East_Routes4_Weekend[i][3]
    demand_weekend = 0
    time_weekend = 0

    for j in range(len(East_stores_Weekend)):
        if store1 == East_stores_Weekend[j]:
            demand_weekend += East_WeekendDemands[j]
            time_weekend += East_WeekendDemands[j] * 450

    for k in range(len(East_stores_Weekend)):
        if store2 == East_stores_Weekend[k]:
            demand_weekend += East_WeekendDemands[k]
            time_weekend += East_WeekendDemands[k] * 450

    for l in range(len(East_stores_Weekend)):
        if store3 == East_stores_Weekend[l]:
            demand_weekend += East_WeekendDemands[l]
            time_weekend += East_WeekendDemands[l] * 450

    for m in range(len(East_stores_Weekend)):
        if store4 == East_stores_Weekend[m]:
            demand_weekend += East_WeekendDemands[m]
            time_weekend += East_WeekendDemands[m] * 450

    for store in range(len(stores)):
        if store1 == stores[store]:
            time_weekend += distribution_time[store]
        if store4 == stores[store]:
            time_weekend += distribution_time[store]

    for store_row in range(len(stores)):
        if store1 == stores[store_row]:
            for store_col in range(len(stores)):
                if store2 == stores[store_col]:
                    time_weekend += travel_durations[store_row][store_col]

    for store_row in range(len(stores)):
        if store2 == stores[store_row]:
            for store_col in range(len(stores)):
                if store3 == stores[store_col]:
                    time_weekend += travel_durations[store_row][store_col]

    for store_row in range(len(stores)):
        if store3 == stores[store_row]:
            for store_col in range(len(stores)):
                if store4 == stores[store_col]:
                    time_weekend += travel_durations[store_row][store_col]

    if (demand_weekend < demand_threshold and time_weekend <= time_threshold):
        EastRoutes_Weekend.append(East_Routes4_Weekend[i])
        Routes_Weekend.append(East_Routes4_Weekend[i])
        Time_Weekend.append(time_weekend/60/60)

for i in range(len(East_Routes5_Weekend)):
    store1 = East_Routes5_Weekend[i][0]
    store2 = East_Routes5_Weekend[i][1]
    store3 = East_Routes5_Weekend[i][2]
    store4 = East_Routes5_Weekend[i][3]
    store5 = East_Routes5_Weekend[i][4]

    demand_weekend = 0
    time_weekend = 0

    for j in range(len(East_stores_Weekend)):
        if store1 == East_stores_Weekend[j]:
            demand_weekend += East_WeekendDemands[j]
            time_weekend += East_WeekendDemands[j] * 450

    for k in range(len(East_stores_Weekend)):
        if store2 == East_stores_Weekend[k]:
            demand_weekend += East_WeekendDemands[k]
            time_weekend += East_WeekendDemands[k] * 450

    for l in range(len(East_stores_Weekend)):
        if store3 == East_stores_Weekend[l]:
            demand_weekend += East_WeekendDemands[l]
            time_weekend += East_WeekendDemands[l] * 450

    for m in range(len(East_stores_Weekend)):
        if store4 == East_stores_Weekend[m]:
            demand_weekend += East_WeekendDemands[m]
            time_weekend += East_WeekendDemands[m] * 450

    for n in range(len(East_stores_Weekend)):
        if store5 == East_stores_Weekend[n]:
            demand_weekend += East_WeekendDemands[n]
            time_weekend += East_WeekendDemands[n] * 450

    for store in range(len(stores)):
        if store1 == stores[store]:
            time_weekend += distribution_time[store]
        if store5 == stores[store]:
            time_weekend += distribution_time[store]

    for store_row in range(len(stores)):
        if store1 == stores[store_row]:
            for store_col in range(len(stores)):
                if store2 == stores[store_col]:
                    time_weekend += travel_durations[store_row][store_col]

    for store_row in range(len(stores)):
        if store2 == stores[store_row]:
            for store_col in range(len(stores)):
                if store3 == stores[store_col]:
                    time_weekend += travel_durations[store_row][store_col]

    for store_row in range(len(stores)):
        if store3 == stores[store_row]:
            for store_col in range(len(stores)):
                if store4 == stores[store_col]:
                    time_weekend += travel_durations[store_row][store_col]

    for store_row in range(len(stores)):
        if store4 == stores[store_row]:
            for store_col in range(len(stores)):
                if store5 == stores[store_col]:
                    time_weekend += travel_durations[store_row][store_col]

    if (demand_weekend < demand_threshold and time_weekend <= time_threshold):
        EastRoutes_Weekend.append(East_Routes5_Weekend[i])
        Routes_Weekend.append(East_Routes5_Weekend[i])
        Time_Weekend.append(time_weekend/60/60)

for i in range(len(East_Routes6_Weekend)):
    store1 = East_Routes6_Weekend[i][0]
    store2 = East_Routes6_Weekend[i][1]
    store3 = East_Routes6_Weekend[i][2]
    store4 = East_Routes6_Weekend[i][3]
    store5 = East_Routes6_Weekend[i][4]
    store6 = East_Routes6_Weekend[i][5]

    demand_weekend = 0
    time_weekend = 0

    for j in range(len(East_stores_Weekend)):
        if store1 == East_stores_Weekend[j]:
            demand_weekend += East_WeekendDemands[j]
            time_weekend += East_WeekendDemands[j] * 450

    for k in range(len(East_stores_Weekend)):
        if store2 == East_stores_Weekend[k]:
            demand_weekend += East_WeekendDemands[k]
            time_weekend += East_WeekendDemands[k] * 450

    for l in range(len(East_stores_Weekend)):
        if store3 == East_stores_Weekend[l]:
            demand_weekend += East_WeekendDemands[l]
            time_weekend += East_WeekendDemands[l] * 450

    for m in range(len(East_stores_Weekend)):
        if store4 == East_stores_Weekend[m]:
            demand_weekend += East_WeekendDemands[m]
            time_weekend += East_WeekendDemands[m] * 450

    for n in range(len(East_stores_Weekend)):
        if store5 == East_stores_Weekend[n]:
            demand_weekend += East_WeekendDemands[n]
            time_weekend += East_WeekendDemands[n] * 450

    for o in range(len(East_stores_Weekend)):
        if store6 == East_stores_Weekend[o]:
            demand_weekend += East_WeekendDemands[o]
            time_weekend += East_WeekendDemands[o] * 450

    for store in range(len(stores)):
        if store1 == stores[store]:
            time_weekend += distribution_time[store]
        if store5 == stores[store]:
            time_weekend += distribution_time[store]

    for store_row in range(len(stores)):
        if store1 == stores[store_row]:
            for store_col in range(len(stores)):
                if store2 == stores[store_col]:
                    time_weekend += travel_durations[store_row][store_col]

    for store_row in range(len(stores)):
        if store2 == stores[store_row]:
            for store_col in range(len(stores)):
                if store3 == stores[store_col]:
                    time_weekend += travel_durations[store_row][store_col]

    for store_row in range(len(stores)):
        if store3 == stores[store_row]:
            for store_col in range(len(stores)):
                if store4 == stores[store_col]:
                    time_weekend += travel_durations[store_row][store_col]

    for store_row in range(len(stores)):
        if store4 == stores[store_row]:
            for store_col in range(len(stores)):
                if store5 == stores[store_col]:
                    time_weekend += travel_durations[store_row][store_col]

    for store_row in range(len(stores)):
        if store5 == stores[store_row]:
            for store_col in range(len(stores)):
                if store6 == stores[store_col]:
                    time_weekend += travel_durations[store_row][store_col]

    if (demand_weekend < demand_threshold and time_weekend <= time_threshold):
        EastRoutes_Weekend.append(East_Routes6_Weekend[i])
        Routes_Weekend.append(East_Routes6_Weekend[i])
        Time_Weekend.append(time_weekend/60/60)

max_routes = 60

# Listing the possible number of routes
weekend_possible_routes = [i for i in range(0,len(Routes_Weekend))]

# Setting up the number of variables needed
WeekendRoute_vars = LpVariable.dicts("Weekend_Route", weekend_possible_routes, 0, None, 'Integer')

# Setting up the minimisation objective function
prob_weekend = LpProblem("Woolworths NZ VRP weekend", LpMinimize)

# Objective function
prob_weekend += lpSum([225 * WeekendRoute_vars[route] * Time_Weekend[route] if Time_Weekend[route] < 4 else 275 * WeekendRoute_vars[route] * Time_Weekend[route] for route in weekend_possible_routes])

# Adding the constraints
prob_weekend += lpSum([WeekendRoute_vars[route] for route in weekend_possible_routes]) <= max_routes

for store in stores:
    prob_weekend += lpSum([WeekendRoute_vars[route] for route in weekend_possible_routes if store in Routes_Weekend[route]]) == 1

# Writing the LP to a file
prob_weekend.writeLP("" + os.getcwd() + os.sep + "LP_files" + os.sep + "WoolworthsVRP_weekend_closure.lp")

# Solving the LP
prob_weekend.solve(PULP_CBC_CMD(msg=0))

weekend_status = LpStatus[prob_weekend.status]
least_cost_weekends = value(prob_weekend.objective)

optimalRoutes_weekend = []
num_weekend = 0
for v in prob_weekend.variables():
    if v.varValue == 1:
        optimalRoutes_weekend.append(v.name)
        num_weekend += 1
