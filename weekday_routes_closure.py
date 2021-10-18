import math
import numpy as np
from pulp import *
import os
from itertools import combinations_with_replacement
from itertools import combinations

# Get array of stores
stores = np.genfromtxt("" + os.getcwd() + os.sep + "Data" + os.sep + "WoolworthsTravelDurations.csv", dtype = str, delimiter= ',', skip_footer= 66)
stores = stores[1:67]
stores = np.delete(stores, 55, 0)

all_stores = np.genfromtxt("" + os.getcwd() + os.sep + "Data" + os.sep + "WoolworthsTravelDurations.csv", dtype = str, delimiter= ',', skip_footer= 66)
all_stores = all_stores[1:67]

# Distances between stores
distances = np.genfromtxt("" + os.getcwd() + os.sep + "Data" + os.sep + "WoolworthsDistances.csv", delimiter= ',', skip_header=1, usecols=list(range(1,67)))
distances = np.delete(distances, 55, 0)
distances = np.delete(distances, 55, 1)

# Travel duration between each store
travel_durations = np.genfromtxt("" + os.getcwd() + os.sep + "Data" + os.sep + "WoolworthsTravelDurations.csv", delimiter= ',', skip_header=1, usecols=list(range(1,67)))
travel_durations = np.delete(travel_durations, 55, 0)
travel_durations = np.delete(travel_durations, 55, 1)

# Travel duration from distribution centre
distribution_time = np.genfromtxt("" + os.getcwd() + os.sep + "Data" + os.sep + "WoolworthsTravelDurations.csv", delimiter= ',', skip_header=56, skip_footer=10, usecols=list(range(1,67)))
distribution_time = np.delete(distribution_time, 55, 0)

# Array of stores in each region
CentralNorth_stores = np.genfromtxt("" + os.getcwd() + os.sep + "Data" + os.sep + "LocationCentralNorth.csv", dtype = str, delimiter= ',', skip_header=1, usecols=0)
CentralSouth_stores = np.genfromtxt("" + os.getcwd() + os.sep + "Data" + os.sep + "LocationCentralSouth.csv", dtype = str, delimiter= ',', skip_header=1, usecols=0)
East_stores = np.genfromtxt("" + os.getcwd() + os.sep + "Data" + os.sep + "LocationEastRegion.csv", dtype = str, delimiter= ',', skip_header=1, usecols=0)
North_stores = np.genfromtxt("" + os.getcwd() + os.sep + "Data" + os.sep + "LocationNorthRegion.csv", dtype = str, delimiter= ',', skip_header=1, usecols=0)
West_stores = np.genfromtxt("" + os.getcwd() + os.sep + "Data" + os.sep + "LocationWestRegion.csv", dtype = str, delimiter= ',', skip_header=1, usecols=0)
South_stores = np.genfromtxt("" + os.getcwd() + os.sep + "Data" + os.sep + "LocationSouthRegion.csv", dtype = str, delimiter= ',', skip_header=1, usecols=0)

# Find median demands of each day for every store in Central North
CentralNorth_WeekdayDemands = np.genfromtxt("" + os.getcwd() + os.sep + "Data" + os.sep + "LocationCentralNorth.csv", delimiter= ',', skip_header=1, usecols=1)

# Find median demands of each day for every store in Central South
CentralSouth_WeekdayDemands = np.genfromtxt("" + os.getcwd() + os.sep + "Data" + os.sep + "LocationCentralSouth.csv", delimiter= ',', skip_header=1, usecols=1)

# Find median demands of each day for every store in North
North_WeekdayDemands = np.genfromtxt("" + os.getcwd() + os.sep + "Data" + os.sep + "LocationNorthRegion.csv", delimiter= ',', skip_header=1, usecols=1)

# Find median demands of each day for every store in South
South_WeekdayDemands = np.genfromtxt("" + os.getcwd() + os.sep + "Data" + os.sep + "LocationSouthRegion.csv", delimiter= ',', skip_header=1, usecols=1)

# Find median demands of each day for every store in West
West_WeekdayDemands = np.genfromtxt("" + os.getcwd() + os.sep + "Data" + os.sep + "LocationWestRegion.csv", delimiter= ',', skip_header=1, usecols=1)

# Find median demands of each day for every store in East
East_WeekdayDemands = np.genfromtxt("" + os.getcwd() + os.sep + "Data" + os.sep + "LocationEastRegion.csv", delimiter= ',', skip_header=1, usecols=1)

# Median demands
demands = np.genfromtxt("" + os.getcwd() + os.sep + "Data" + os.sep + "median_demand.csv", delimiter= ',', skip_header=1, usecols=1)

enlarge_stores = []
close_stores = []
merge_stores = []

# Loop through stores
for i in range(len(distances)):
    for j in range(len(distances)):

        # Searching for stores that are within 1500 metres of one another and with demand of less than 7.5 pallets
        if distances[i][j] > 0 and distances[i][j] < 1500 and demands[i] < 7.5 and demands[j] < 7.5:
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

# Aviemore Drive
East_WeekdayDemands[5] = demands[13]
East_stores = np.delete(East_stores, 6, 0)
East_WeekdayDemands = np.delete(East_WeekdayDemands, 6, 0)

# Kelston
CentralSouth_WeekdayDemands[9] = demands[16]
CentralSouth_stores = np.delete(CentralSouth_stores, 8, 0)
CentralSouth_WeekdayDemands = np.delete(CentralSouth_WeekdayDemands, 8, 0)

# Metro Albert Street
CentralNorth_WeekdayDemands[11] = demands[53]
CentralNorth_stores = np.delete(CentralNorth_stores, 10, 0)
CentralNorth_WeekdayDemands = np.delete(CentralNorth_WeekdayDemands, 10, 0)

# SV Papakura
South_WeekdayDemands[1] = demands[37]
South_stores = np.delete(South_stores, 0, 0)
South_WeekdayDemands = np.delete(South_WeekdayDemands, 0, 0)

for i in reversed(range(len(stores))):
    for j in range(len(close_stores)):
        if (stores[i] == close_stores[j]):
            stores = np.delete(stores, i, 0)
            travel_durations = np.delete(travel_durations, i, 0)
            travel_durations = np.delete(travel_durations, i, 1)
            distribution_time = np.delete(distribution_time, i, 0)

for i in reversed(range(len(all_stores))):
    for j in range(len(close_stores)):
        if (all_stores[i] == close_stores[j]):
            all_stores = np.delete(all_stores, i, 0)

demand_threshold = 27
time_threshold = 60 * 4 * 2 * 60

Routes_Weekday = []
Time_Weekday = []

CentralNorthRoutes_Weekday = []
CentralSouthRoutes_Weekday = []
NorthRoutes_Weekday = []
SouthRoutes_Weekday = []
WestRoutes_Weekday = []
EastRoutes_Weekday = []

CentralNorth_Routes2 = (list(combinations(CentralNorth_stores, 2)))
CentralNorth_Routes3 = (list(combinations(CentralNorth_stores, 3)))
CentralNorth_Routes4 = (list(combinations(CentralNorth_stores, 4)))
CentralNorth_Routes5 = (list(combinations(CentralNorth_stores, 5)))
CentralNorth_Routes6 = (list(combinations(CentralNorth_stores, 6)))

for i in range(len(CentralNorth_Routes2)):
    store1 = CentralNorth_Routes2[i][0]
    store2 = CentralNorth_Routes2[i][1]
    demand_weekday = 0
    time_weekday = 0

    for j in range(len(CentralNorth_stores)):
        if store1 == CentralNorth_stores[j]:
            demand_weekday += CentralNorth_WeekdayDemands[j]
            time_weekday += CentralNorth_WeekdayDemands[j] * 450

    for k in range(len(CentralNorth_stores)):
        if store2 == CentralNorth_stores[k]:
            demand_weekday += CentralNorth_WeekdayDemands[k]
            time_weekday += CentralNorth_WeekdayDemands[k] * 450

    for store in range(len(stores)):
        if store1 == stores[store]:
            time_weekday += distribution_time[store]
        if store2 == stores[store]:
            time_weekday += distribution_time[store]

    for store_row in range(len(stores)):
        if store1 == stores[store_row]:
            for store_col in range(len(stores)):
                if store2 == stores[store_col]:
                    time_weekday += travel_durations[store_row][store_col]

    if (demand_weekday < demand_threshold and time_weekday <= time_threshold):
        CentralNorthRoutes_Weekday.append(CentralNorth_Routes2[i])
        Routes_Weekday.append(CentralNorth_Routes2[i])
        Time_Weekday.append(time_weekday/60/60)

for i in range(len(CentralNorth_Routes3)):
    store1 = CentralNorth_Routes3[i][0]
    store2 = CentralNorth_Routes3[i][1]
    store3 = CentralNorth_Routes3[i][2]
    demand_weekday = 0
    time_weekday = 0

    for j in range(len(CentralNorth_stores)):
        if store1 == CentralNorth_stores[j]:
            demand_weekday += CentralNorth_WeekdayDemands[j]
            time_weekday += CentralNorth_WeekdayDemands[j] * 450

    for k in range(len(CentralNorth_stores)):
        if store2 == CentralNorth_stores[k]:
            demand_weekday += CentralNorth_WeekdayDemands[k]
            time_weekday += CentralNorth_WeekdayDemands[k] * 450

    for l in range(len(CentralNorth_stores)):
        if store3 == CentralNorth_stores[l]:
            demand_weekday += CentralNorth_WeekdayDemands[l]
            time_weekday += CentralNorth_WeekdayDemands[l] * 450

    for store in range(len(stores)):
        if store1 == stores[store]:
            time_weekday += distribution_time[store]
        if store3 == stores[store]:
            time_weekday += distribution_time[store]

    for store_row in range(len(stores)):
        if store1 == stores[store_row]:
            for store_col in range(len(stores)):
                if store2 == stores[store_col]:
                    time_weekday += travel_durations[store_row][store_col]

    for store_row in range(len(stores)):
        if store2 == stores[store_row]:
            for store_col in range(len(stores)):
                if store3 == stores[store_col]:
                    time_weekday += travel_durations[store_row][store_col]

    if (demand_weekday < demand_threshold and time_weekday <= time_threshold):
        CentralNorthRoutes_Weekday.append(CentralNorth_Routes3[i])
        Routes_Weekday.append(CentralNorth_Routes3[i])
        Time_Weekday.append(time_weekday/60/60)

for i in range(len(CentralNorth_Routes4)):
    store1 = CentralNorth_Routes4[i][0]
    store2 = CentralNorth_Routes4[i][1]
    store3 = CentralNorth_Routes4[i][2]
    store4 = CentralNorth_Routes4[i][3]
    demand_weekday = 0
    time_weekday = 0

    for j in range(len(CentralNorth_stores)):
        if store1 == CentralNorth_stores[j]:
            demand_weekday += CentralNorth_WeekdayDemands[j]
            time_weekday += CentralNorth_WeekdayDemands[j] * 450

    for k in range(len(CentralNorth_stores)):
        if store2 == CentralNorth_stores[k]:
            demand_weekday += CentralNorth_WeekdayDemands[k]
            time_weekday += CentralNorth_WeekdayDemands[k] * 450

    for l in range(len(CentralNorth_stores)):
        if store3 == CentralNorth_stores[l]:
            demand_weekday += CentralNorth_WeekdayDemands[l]
            time_weekday += CentralNorth_WeekdayDemands[l] * 450

    for m in range(len(CentralNorth_stores)):
        if store4 == CentralNorth_stores[m]:
            demand_weekday += CentralNorth_WeekdayDemands[m]
            time_weekday += CentralNorth_WeekdayDemands[m] * 450

    for store in range(len(stores)):
        if store1 == stores[store]:
            time_weekday += distribution_time[store]
        if store4 == stores[store]:
            time_weekday += distribution_time[store]

    for store_row in range(len(stores)):
        if store1 == stores[store_row]:
            for store_col in range(len(stores)):
                if store2 == stores[store_col]:
                    time_weekday += travel_durations[store_row][store_col]

    for store_row in range(len(stores)):
        if store2 == stores[store_row]:
            for store_col in range(len(stores)):
                if store3 == stores[store_col]:
                    time_weekday += travel_durations[store_row][store_col]

    for store_row in range(len(stores)):
        if store3 == stores[store_row]:
            for store_col in range(len(stores)):
                if store4 == stores[store_col]:
                    time_weekday += travel_durations[store_row][store_col]

    if (demand_weekday < demand_threshold and time_weekday <= time_threshold):
        CentralNorthRoutes_Weekday.append(CentralNorth_Routes4[i])
        Routes_Weekday.append(CentralNorth_Routes4[i])
        Time_Weekday.append(time_weekday/60/60)

for i in range(len(CentralNorth_Routes5)):
    store1 = CentralNorth_Routes5[i][0]
    store2 = CentralNorth_Routes5[i][1]
    store3 = CentralNorth_Routes5[i][2]
    store4 = CentralNorth_Routes5[i][3]
    store5 = CentralNorth_Routes5[i][4]

    demand_weekday = 0
    time_weekday = 0

    for j in range(len(CentralNorth_stores)):
        if store1 == CentralNorth_stores[j]:
            demand_weekday += CentralNorth_WeekdayDemands[j]
            time_weekday += CentralNorth_WeekdayDemands[j] * 450

    for k in range(len(CentralNorth_stores)):
        if store2 == CentralNorth_stores[k]:
            demand_weekday += CentralNorth_WeekdayDemands[k]
            time_weekday += CentralNorth_WeekdayDemands[k] * 450

    for l in range(len(CentralNorth_stores)):
        if store3 == CentralNorth_stores[l]:
            demand_weekday += CentralNorth_WeekdayDemands[l]
            time_weekday += CentralNorth_WeekdayDemands[l] * 450

    for m in range(len(CentralNorth_stores)):
        if store4 == CentralNorth_stores[m]:
            demand_weekday += CentralNorth_WeekdayDemands[m]
            time_weekday += CentralNorth_WeekdayDemands[m] * 450

    for n in range(len(CentralNorth_stores)):
        if store5 == CentralNorth_stores[n]:
            demand_weekday += CentralNorth_WeekdayDemands[n]
            time_weekday += CentralNorth_WeekdayDemands[n] * 450

    for store in range(len(stores)):
        if store1 == stores[store]:
            time_weekday += distribution_time[store]
        if store5 == stores[store]:
            time_weekday += distribution_time[store]

    for store_row in range(len(stores)):
        if store1 == stores[store_row]:
            for store_col in range(len(stores)):
                if store2 == stores[store_col]:
                    time_weekday += travel_durations[store_row][store_col]

    for store_row in range(len(stores)):
        if store2 == stores[store_row]:
            for store_col in range(len(stores)):
                if store3 == stores[store_col]:
                    time_weekday += travel_durations[store_row][store_col]

    for store_row in range(len(stores)):
        if store3 == stores[store_row]:
            for store_col in range(len(stores)):
                if store4 == stores[store_col]:
                    time_weekday += travel_durations[store_row][store_col]

    for store_row in range(len(stores)):
        if store4 == stores[store_row]:
            for store_col in range(len(stores)):
                if store5 == stores[store_col]:
                    time_weekday += travel_durations[store_row][store_col]

    if (demand_weekday < demand_threshold and time_weekday <= time_threshold):
        CentralNorthRoutes_Weekday.append(CentralNorth_Routes5[i])
        Routes_Weekday.append(CentralNorth_Routes5[i])
        Time_Weekday.append(time_weekday/60/60)

for i in range(len(CentralNorth_Routes6)):
    store1 = CentralNorth_Routes6[i][0]
    store2 = CentralNorth_Routes6[i][1]
    store3 = CentralNorth_Routes6[i][2]
    store4 = CentralNorth_Routes6[i][3]
    store5 = CentralNorth_Routes6[i][4]
    store6 = CentralNorth_Routes6[i][5]

    demand_weekday = 0
    time_weekday = 0

    for j in range(len(CentralNorth_stores)):
        if store1 == CentralNorth_stores[j]:
            demand_weekday += CentralNorth_WeekdayDemands[j]
            time_weekday += CentralNorth_WeekdayDemands[j] * 450

    for k in range(len(CentralNorth_stores)):
        if store2 == CentralNorth_stores[k]:
            demand_weekday += CentralNorth_WeekdayDemands[k]
            time_weekday += CentralNorth_WeekdayDemands[k] * 450

    for l in range(len(CentralNorth_stores)):
        if store3 == CentralNorth_stores[l]:
            demand_weekday += CentralNorth_WeekdayDemands[l]
            time_weekday += CentralNorth_WeekdayDemands[l] * 450

    for m in range(len(CentralNorth_stores)):
        if store4 == CentralNorth_stores[m]:
            demand_weekday += CentralNorth_WeekdayDemands[m]
            time_weekday += CentralNorth_WeekdayDemands[m] * 450

    for n in range(len(CentralNorth_stores)):
        if store5 == CentralNorth_stores[n]:
            demand_weekday += CentralNorth_WeekdayDemands[n]
            time_weekday += CentralNorth_WeekdayDemands[n] * 450

    for o in range(len(CentralNorth_stores)):
        if store6 == CentralNorth_stores[o]:
            demand_weekday += CentralNorth_WeekdayDemands[o]
            time_weekday += CentralNorth_WeekdayDemands[o] * 450

    for store in range(len(stores)):
        if store1 == stores[store]:
            time_weekday += distribution_time[store]
        if store5 == stores[store]:
            time_weekday += distribution_time[store]

    for store_row in range(len(stores)):
        if store1 == stores[store_row]:
            for store_col in range(len(stores)):
                if store2 == stores[store_col]:
                    time_weekday += travel_durations[store_row][store_col]

    for store_row in range(len(stores)):
        if store2 == stores[store_row]:
            for store_col in range(len(stores)):
                if store3 == stores[store_col]:
                    time_weekday += travel_durations[store_row][store_col]

    for store_row in range(len(stores)):
        if store3 == stores[store_row]:
            for store_col in range(len(stores)):
                if store4 == stores[store_col]:
                    time_weekday += travel_durations[store_row][store_col]

    for store_row in range(len(stores)):
        if store4 == stores[store_row]:
            for store_col in range(len(stores)):
                if store5 == stores[store_col]:
                    time_weekday += travel_durations[store_row][store_col]

    for store_row in range(len(stores)):
        if store5 == stores[store_row]:
            for store_col in range(len(stores)):
                if store6 == stores[store_col]:
                    time_weekday += travel_durations[store_row][store_col]

    if (demand_weekday < demand_threshold and time_weekday <= time_threshold):
        CentralNorthRoutes_Weekday.append(CentralNorth_Routes6[i])
        Routes_Weekday.append(CentralNorth_Routes6[i])
        Time_Weekday.append(time_weekday/60/60)

# Central South stores
CentralSouth_Routes2 = (list(combinations(CentralSouth_stores, 2)))
CentralSouth_Routes3 = (list(combinations(CentralSouth_stores, 3)))
CentralSouth_Routes4 = (list(combinations(CentralSouth_stores, 4)))
CentralSouth_Routes5 = (list(combinations(CentralSouth_stores, 5)))
CentralSouth_Routes6 = (list(combinations(CentralSouth_stores, 6)))

for i in range(len(CentralSouth_Routes2)):
    store1 = CentralSouth_Routes2[i][0]
    store2 = CentralSouth_Routes2[i][1]
    demand_weekday = 0
    time_weekday = 0

    for j in range(len(CentralSouth_stores)):
        if store1 == CentralSouth_stores[j]:
            demand_weekday += CentralSouth_WeekdayDemands[j]
            time_weekday += CentralSouth_WeekdayDemands[j] * 450

    for k in range(len(CentralSouth_stores)):
        if store2 == CentralSouth_stores[k]:
            demand_weekday += CentralSouth_WeekdayDemands[k]
            time_weekday += CentralSouth_WeekdayDemands[k] * 450

    for store in range(len(stores)):
        if store1 == stores[store]:
            time_weekday += distribution_time[store]
        if store2 == stores[store]:
            time_weekday += distribution_time[store]

    for store_row in range(len(stores)):
        if store1 == stores[store_row]:
            for store_col in range(len(stores)):
                if store2 == stores[store_col]:
                    time_weekday += travel_durations[store_row][store_col]

    if (demand_weekday < demand_threshold and time_weekday <= time_threshold):
        CentralSouthRoutes_Weekday.append(CentralSouth_Routes2[i])
        Routes_Weekday.append(CentralSouth_Routes2[i])
        Time_Weekday.append(time_weekday/60/60)

for i in range(len(CentralSouth_Routes3)):
    store1 = CentralSouth_Routes3[i][0]
    store2 = CentralSouth_Routes3[i][1]
    store3 = CentralSouth_Routes3[i][2]
    demand_weekday = 0
    time_weekday = 0

    for j in range(len(CentralSouth_stores)):
        if store1 == CentralSouth_stores[j]:
            demand_weekday += CentralSouth_WeekdayDemands[j]
            time_weekday += CentralSouth_WeekdayDemands[j] * 450

    for k in range(len(CentralSouth_stores)):
        if store2 == CentralSouth_stores[k]:
            demand_weekday += CentralSouth_WeekdayDemands[k]
            time_weekday += CentralSouth_WeekdayDemands[k] * 450

    for l in range(len(CentralSouth_stores)):
        if store3 == CentralSouth_stores[l]:
            demand_weekday += CentralSouth_WeekdayDemands[l]
            time_weekday += CentralSouth_WeekdayDemands[l] * 450

    for store in range(len(stores)):
        if store1 == stores[store]:
            time_weekday += distribution_time[store]
        if store3 == stores[store]:
            time_weekday += distribution_time[store]

    for store_row in range(len(stores)):
        if store1 == stores[store_row]:
            for store_col in range(len(stores)):
                if store2 == stores[store_col]:
                    time_weekday += travel_durations[store_row][store_col]

    for store_row in range(len(stores)):
        if store2 == stores[store_row]:
            for store_col in range(len(stores)):
                if store3 == stores[store_col]:
                    time_weekday += travel_durations[store_row][store_col]

    if (demand_weekday < demand_threshold and time_weekday <= time_threshold):
        CentralSouthRoutes_Weekday.append(CentralSouth_Routes3[i])
        Routes_Weekday.append(CentralSouth_Routes3[i])
        Time_Weekday.append(time_weekday/60/60)

for i in range(len(CentralSouth_Routes4)):
    
    store1 = CentralSouth_Routes4[i][0]
    store2 = CentralSouth_Routes4[i][1]
    store3 = CentralSouth_Routes4[i][2]
    store4 = CentralSouth_Routes4[i][3]
    demand_weekday = 0
    time_weekday = 0

    for j in range(len(CentralSouth_stores)):
        if store1 == CentralSouth_stores[j]:
            demand_weekday += CentralSouth_WeekdayDemands[j]
            time_weekday += CentralSouth_WeekdayDemands[j] * 450

    for k in range(len(CentralSouth_stores)):
        if store2 == CentralSouth_stores[k]:
            demand_weekday += CentralSouth_WeekdayDemands[k]
            time_weekday += CentralSouth_WeekdayDemands[k] * 450

    for l in range(len(CentralSouth_stores)):
        if store3 == CentralSouth_stores[l]:
            demand_weekday += CentralSouth_WeekdayDemands[l]
            time_weekday += CentralSouth_WeekdayDemands[l] * 450

    for m in range(len(CentralSouth_stores)):
        if store4 == CentralSouth_stores[m]:
            demand_weekday += CentralSouth_WeekdayDemands[m]
            time_weekday += CentralSouth_WeekdayDemands[m] * 450

    for store in range(len(stores)):
        if store1 == stores[store]:
            time_weekday += distribution_time[store]
        if store4 == stores[store]:
            time_weekday += distribution_time[store]

    for store_row in range(len(stores)):
        if store1 == stores[store_row]:
            for store_col in range(len(stores)):
                if store2 == stores[store_col]:
                    time_weekday += travel_durations[store_row][store_col]

    for store_row in range(len(stores)):
        if store2 == stores[store_row]:
            for store_col in range(len(stores)):
                if store3 == stores[store_col]:
                    time_weekday += travel_durations[store_row][store_col]

    for store_row in range(len(stores)):
        if store3 == stores[store_row]:
            for store_col in range(len(stores)):
                if store4 == stores[store_col]:
                    time_weekday += travel_durations[store_row][store_col]

    if (demand_weekday < demand_threshold and time_weekday <= time_threshold):
        CentralSouthRoutes_Weekday.append(CentralSouth_Routes4[i])
        Routes_Weekday.append(CentralSouth_Routes4[i])
        Time_Weekday.append(time_weekday/60/60)

for i in range(len(CentralSouth_Routes5)):
    store1 = CentralSouth_Routes5[i][0]
    store2 = CentralSouth_Routes5[i][1]
    store3 = CentralSouth_Routes5[i][2]
    store4 = CentralSouth_Routes5[i][3]
    store5 = CentralSouth_Routes5[i][4]

    demand_weekday = 0
    time_weekday = 0
    for j in range(len(CentralSouth_stores)):
        if store1 == CentralSouth_stores[j]:
            demand_weekday += CentralSouth_WeekdayDemands[j]
            time_weekday += CentralSouth_WeekdayDemands[j] * 450

    for k in range(len(CentralSouth_stores)):
        if store2 == CentralSouth_stores[k]:
            demand_weekday += CentralSouth_WeekdayDemands[k]
            time_weekday += CentralSouth_WeekdayDemands[k] * 450

    for l in range(len(CentralSouth_stores)):
        if store3 == CentralSouth_stores[l]:
            demand_weekday += CentralSouth_WeekdayDemands[l]
            time_weekday += CentralSouth_WeekdayDemands[l] * 450

    for m in range(len(CentralSouth_stores)):
        if store4 == CentralSouth_stores[m]:
            demand_weekday += CentralSouth_WeekdayDemands[m]
            time_weekday += CentralSouth_WeekdayDemands[m] * 450

    for n in range(len(CentralSouth_stores)):
        if store5 == CentralSouth_stores[n]:
            demand_weekday += CentralSouth_WeekdayDemands[n]
            time_weekday += CentralSouth_WeekdayDemands[n] * 450

    for store in range(len(stores)):
        if store1 == stores[store]:
            time_weekday += distribution_time[store]
        if store5 == stores[store]:
            time_weekday += distribution_time[store]

    for store_row in range(len(stores)):
        if store1 == stores[store_row]:
            for store_col in range(len(stores)):
                if store2 == stores[store_col]:
                    time_weekday += travel_durations[store_row][store_col]

    for store_row in range(len(stores)):
        if store2 == stores[store_row]:
            for store_col in range(len(stores)):
                if store3 == stores[store_col]:
                    time_weekday += travel_durations[store_row][store_col]

    for store_row in range(len(stores)):
        if store3 == stores[store_row]:
            for store_col in range(len(stores)):
                if store4 == stores[store_col]:
                    time_weekday += travel_durations[store_row][store_col]

    for store_row in range(len(stores)):
        if store4 == stores[store_row]:
            for store_col in range(len(stores)):
                if store5 == stores[store_col]:
                    time_weekday += travel_durations[store_row][store_col]

    if (demand_weekday < demand_threshold and time_weekday <= time_threshold):
        CentralSouthRoutes_Weekday.append(CentralSouth_Routes5[i])
        Routes_Weekday.append(CentralSouth_Routes5[i])
        Time_Weekday.append(time_weekday/60/60)

for i in range(len(CentralSouth_Routes6)):
    store1 = CentralSouth_Routes6[i][0]
    store2 = CentralSouth_Routes6[i][1]
    store3 = CentralSouth_Routes6[i][2]
    store4 = CentralSouth_Routes6[i][3]
    store5 = CentralSouth_Routes6[i][4]
    store6 = CentralSouth_Routes6[i][5]

    demand_weekday = 0
    time_weekday = 0

    for j in range(len(CentralSouth_stores)):
        if store1 == CentralSouth_stores[j]:
            demand_weekday += CentralSouth_WeekdayDemands[j]
            time_weekday += CentralSouth_WeekdayDemands[j] * 450

    for k in range(len(CentralSouth_stores)):
        if store2 == CentralSouth_stores[k]:
            demand_weekday += CentralSouth_WeekdayDemands[k]
            time_weekday += CentralSouth_WeekdayDemands[k] * 450

    for l in range(len(CentralSouth_stores)):
        if store3 == CentralSouth_stores[l]:
            demand_weekday += CentralSouth_WeekdayDemands[l]
            time_weekday += CentralSouth_WeekdayDemands[l] * 450

    for m in range(len(CentralSouth_stores)):
        if store4 == CentralSouth_stores[m]:
            demand_weekday += CentralSouth_WeekdayDemands[m]
            time_weekday += CentralSouth_WeekdayDemands[m] * 450

    for n in range(len(CentralSouth_stores)):
        if store5 == CentralSouth_stores[n]:
            demand_weekday += CentralSouth_WeekdayDemands[n]
            time_weekday += CentralSouth_WeekdayDemands[n] * 450

    for o in range(len(CentralSouth_stores)):
        if store6 == CentralSouth_stores[o]:
            demand_weekday += CentralSouth_WeekdayDemands[o]
            time_weekday += CentralSouth_WeekdayDemands[o] * 450

    for store in range(len(stores)):
        if store1 == stores[store]:
            time_weekday += distribution_time[store]
        if store5 == stores[store]:
            time_weekday += distribution_time[store]

    for store_row in range(len(stores)):
        if store1 == stores[store_row]:
            for store_col in range(len(stores)):
                if store2 == stores[store_col]:
                    time_weekday += travel_durations[store_row][store_col]

    for store_row in range(len(stores)):
        if store2 == stores[store_row]:
            for store_col in range(len(stores)):
                if store3 == stores[store_col]:
                    time_weekday += travel_durations[store_row][store_col]

    for store_row in range(len(stores)):
        if store3 == stores[store_row]:
            for store_col in range(len(stores)):
                if store4 == stores[store_col]:
                    time_weekday += travel_durations[store_row][store_col]

    for store_row in range(len(stores)):
        if store4 == stores[store_row]:
            for store_col in range(len(stores)):
                if store5 == stores[store_col]:
                    time_weekday += travel_durations[store_row][store_col]

    for store_row in range(len(stores)):
        if store5 == stores[store_row]:
            for store_col in range(len(stores)):
                if store6 == stores[store_col]:
                    time_weekday += travel_durations[store_row][store_col]

    if (demand_weekday < demand_threshold and time_weekday <= time_threshold):
        CentralSouthRoutes_Weekday.append(CentralSouth_Routes6[i])
        Routes_Weekday.append(CentralSouth_Routes6[i])
        Time_Weekday.append(time_weekday/60/60)

North_Routes2 = (list(combinations(North_stores, 2)))
North_Routes3 = (list(combinations(North_stores, 3)))
North_Routes4 = (list(combinations(North_stores, 4)))
North_Routes5 = (list(combinations(North_stores, 5)))
North_Routes6 = (list(combinations(North_stores, 6)))

for i in range(len(North_Routes2)):
    store1 = North_Routes2[i][0]
    store2 = North_Routes2[i][1]
    demand_weekday = 0
    time_weekday = 0

    for j in range(len(North_stores)):
        if store1 == North_stores[j]:
            demand_weekday += North_WeekdayDemands[j]
            time_weekday += North_WeekdayDemands[j] * 450

    for k in range(len(North_stores)):
        if store2 == North_stores[k]:
            demand_weekday += North_WeekdayDemands[k]
            time_weekday += North_WeekdayDemands[k] * 450

    for store in range(len(stores)):
        if store1 == stores[store]:
            time_weekday += distribution_time[store]
        if store2 == stores[store]:
            time_weekday += distribution_time[store]

    for store_row in range(len(stores)):
        if store1 == stores[store_row]:
            for store_col in range(len(stores)):
                if store2 == stores[store_col]:
                    time_weekday += travel_durations[store_row][store_col]

    if (demand_weekday < demand_threshold and time_weekday <= time_threshold):
        NorthRoutes_Weekday.append(North_Routes2[i])
        Routes_Weekday.append(North_Routes2[i])
        Time_Weekday.append(time_weekday/60/60)

for i in range(len(North_Routes3)):
    store1 = North_Routes3[i][0]
    store2 = North_Routes3[i][1]
    store3 = North_Routes3[i][2]
    demand_weekday = 0
    time_weekday = 0

    for j in range(len(North_stores)):
        if store1 == North_stores[j]:
            demand_weekday += North_WeekdayDemands[j]
            time_weekday += North_WeekdayDemands[j] * 450

    for k in range(len(North_stores)):
        if store2 == North_stores[k]:
            demand_weekday += North_WeekdayDemands[k]
            time_weekday += North_WeekdayDemands[k] * 450

    for l in range(len(North_stores)):
        if store3 == North_stores[l]:
            demand_weekday += North_WeekdayDemands[l]
            time_weekday += North_WeekdayDemands[l] * 450

    for store in range(len(stores)):
        if store1 == stores[store]:
            time_weekday += distribution_time[store]
        if store3 == stores[store]:
            time_weekday += distribution_time[store]

    for store_row in range(len(stores)):
        if store1 == stores[store_row]:
            for store_col in range(len(stores)):
                if store2 == stores[store_col]:
                    time_weekday += travel_durations[store_row][store_col]

    for store_row in range(len(stores)):
        if store2 == stores[store_row]:
            for store_col in range(len(stores)):
                if store3 == stores[store_col]:
                    time_weekday += travel_durations[store_row][store_col]

    if (demand_weekday < demand_threshold and time_weekday <= time_threshold):
        NorthRoutes_Weekday.append(North_Routes3[i])
        Routes_Weekday.append(North_Routes3[i])
        Time_Weekday.append(time_weekday/60/60)

for i in range(len(North_Routes4)):
    store1 = North_Routes4[i][0]
    store2 = North_Routes4[i][1]
    store3 = North_Routes4[i][2]
    store4 = North_Routes4[i][3]
    demand_weekday = 0
    time_weekday = 0

    for j in range(len(North_stores)):
        if store1 == North_stores[j]:
            demand_weekday += North_WeekdayDemands[j]
            time_weekday += North_WeekdayDemands[j] * 450

    for k in range(len(North_stores)):
        if store2 == North_stores[k]:
            demand_weekday += North_WeekdayDemands[k]
            time_weekday += North_WeekdayDemands[k] * 450

    for l in range(len(North_stores)):
        if store3 == North_stores[l]:
            demand_weekday += North_WeekdayDemands[l]
            time_weekday += North_WeekdayDemands[l] * 450

    for m in range(len(North_stores)):
        if store4 == North_stores[m]:
            demand_weekday += North_WeekdayDemands[m]
            time_weekday += North_WeekdayDemands[m] * 450

    for store in range(len(stores)):
        if store1 == stores[store]:
            time_weekday += distribution_time[store]
        if store4 == stores[store]:
            time_weekday += distribution_time[store]

    for store_row in range(len(stores)):
        if store1 == stores[store_row]:
            for store_col in range(len(stores)):
                if store2 == stores[store_col]:
                    time_weekday += travel_durations[store_row][store_col]

    for store_row in range(len(stores)):
        if store2 == stores[store_row]:
            for store_col in range(len(stores)):
                if store3 == stores[store_col]:
                    time_weekday += travel_durations[store_row][store_col]

    for store_row in range(len(stores)):
        if store3 == stores[store_row]:
            for store_col in range(len(stores)):
                if store4 == stores[store_col]:
                    time_weekday += travel_durations[store_row][store_col]

    if (demand_weekday < demand_threshold and time_weekday <= time_threshold):
        NorthRoutes_Weekday.append(North_Routes4[i])
        Routes_Weekday.append(North_Routes4[i])
        Time_Weekday.append(time_weekday/60/60)

for i in range(len(North_Routes5)):
    store1 = North_Routes5[i][0]
    store2 = North_Routes5[i][1]
    store3 = North_Routes5[i][2]
    store4 = North_Routes5[i][3]
    store5 = North_Routes5[i][4]

    demand_weekday = 0
    time_weekday = 0

    for j in range(len(North_stores)):
        if store1 == North_stores[j]:
            demand_weekday += North_WeekdayDemands[j]
            time_weekday += North_WeekdayDemands[j] * 450

    for k in range(len(North_stores)):
        if store2 == North_stores[k]:
            demand_weekday += North_WeekdayDemands[k]
            time_weekday += North_WeekdayDemands[k] * 450

    for l in range(len(North_stores)):
        if store3 == North_stores[l]:
            demand_weekday += North_WeekdayDemands[l]
            time_weekday += North_WeekdayDemands[l] * 450

    for m in range(len(North_stores)):
        if store4 == North_stores[m]:
            demand_weekday += North_WeekdayDemands[m]
            time_weekday += North_WeekdayDemands[m] * 450

    for n in range(len(North_stores)):
        if store4 == North_stores[n]:
            demand_weekday += North_WeekdayDemands[n]
            time_weekday += North_WeekdayDemands[n] * 450
            
    for store in range(len(stores)):
        if store1 == stores[store]:
            time_weekday += distribution_time[store]
        if store5 == stores[store]:
            time_weekday += distribution_time[store]

    for store_row in range(len(stores)):
        if store1 == stores[store_row]:
            for store_col in range(len(stores)):
                if store2 == stores[store_col]:
                    time_weekday += travel_durations[store_row][store_col]

    for store_row in range(len(stores)):
        if store2 == stores[store_row]:
            for store_col in range(len(stores)):
                if store3 == stores[store_col]:
                    time_weekday += travel_durations[store_row][store_col]

    for store_row in range(len(stores)):
        if store3 == stores[store_row]:
            for store_col in range(len(stores)):
                if store4 == stores[store_col]:
                    time_weekday += travel_durations[store_row][store_col]

    for store_row in range(len(stores)):
        if store4 == stores[store_row]:
            for store_col in range(len(stores)):
                if store5 == stores[store_col]:
                    time_weekday += travel_durations[store_row][store_col]

    if (demand_weekday < demand_threshold and time_weekday <= time_threshold):
        NorthRoutes_Weekday.append(North_Routes5[i])
        Routes_Weekday.append(North_Routes5[i])
        Time_Weekday.append(time_weekday/60/60)

for i in range(len(North_Routes6)):
    store1 = North_Routes6[i][0]
    store2 = North_Routes6[i][1]
    store3 = North_Routes6[i][2]
    store4 = North_Routes6[i][3]
    store5 = North_Routes6[i][4]
    store6 = North_Routes6[i][5]

    demand_weekday = 0
    time_weekday = 0

    for j in range(len(North_stores)):
        if store1 == North_stores[j]:
            demand_weekday += North_WeekdayDemands[j]
            time_weekday += North_WeekdayDemands[j] * 450

    for k in range(len(North_stores)):
        if store2 == North_stores[k]:
            demand_weekday += North_WeekdayDemands[k]
            time_weekday += North_WeekdayDemands[k] * 450

    for l in range(len(North_stores)):
        if store3 == North_stores[l]:
            demand_weekday += North_WeekdayDemands[l]
            time_weekday += North_WeekdayDemands[l] * 450

    for m in range(len(North_stores)):
        if store4 == North_stores[m]:
            demand_weekday += North_WeekdayDemands[m]
            time_weekday += North_WeekdayDemands[m] * 450

    for n in range(len(North_stores)):
        if store5 == North_stores[n]:
            demand_weekday += North_WeekdayDemands[n]
            time_weekday += North_WeekdayDemands[n] * 450

    for o in range(len(North_stores)):
        if store6 == North_stores[o]:
            demand_weekday += North_WeekdayDemands[o]
            time_weekday += North_WeekdayDemands[o] * 450

    for store in range(len(stores)):
        if store1 == stores[store]:
            time_weekday += distribution_time[store]
        if store5 == stores[store]:
            time_weekday += distribution_time[store]

    for store_row in range(len(stores)):
        if store1 == stores[store_row]:
            for store_col in range(len(stores)):
                if store2 == stores[store_col]:
                    time_weekday += travel_durations[store_row][store_col]

    for store_row in range(len(stores)):
        if store2 == stores[store_row]:
            for store_col in range(len(stores)):
                if store3 == stores[store_col]:
                    time_weekday += travel_durations[store_row][store_col]

    for store_row in range(len(stores)):
        if store3 == stores[store_row]:
            for store_col in range(len(stores)):
                if store4 == stores[store_col]:
                    time_weekday += travel_durations[store_row][store_col]

    for store_row in range(len(stores)):
        if store4 == stores[store_row]:
            for store_col in range(len(stores)):
                if store5 == stores[store_col]:
                    time_weekday += travel_durations[store_row][store_col]

    for store_row in range(len(stores)):
        if store5 == stores[store_row]:
            for store_col in range(len(stores)):
                if store6 == stores[store_col]:
                    time_weekday += travel_durations[store_row][store_col]

    if (demand_weekday < demand_threshold and time_weekday <= time_threshold):
        NorthRoutes_Weekday.append(North_Routes6[i])
        Routes_Weekday.append(North_Routes6[i])
        Time_Weekday.append(time_weekday/60/60)

South_Routes2 = (list(combinations(South_stores, 2)))
South_Routes3 = (list(combinations(South_stores, 3)))
South_Routes4 = (list(combinations(South_stores, 4)))
South_Routes5 = (list(combinations(South_stores, 5)))
South_Routes6 = (list(combinations(South_stores, 6)))

for i in range(len(South_Routes2)):
    store1 = South_Routes2[i][0]
    store2 = South_Routes2[i][1]
    demand_weekday = 0
    time_weekday = 0

    for j in range(len(South_stores)):
        if store1 == South_stores[j]:
            demand_weekday += South_WeekdayDemands[j]
            time_weekday += South_WeekdayDemands[j] * 450

    for k in range(len(South_stores)):
        if store2 == South_stores[k]:
            demand_weekday += South_WeekdayDemands[k]
            time_weekday += South_WeekdayDemands[k] * 450

    for store in range(len(stores)):
        if store1 == stores[store]:
            time_weekday += distribution_time[store]
        if store2 == stores[store]:
            time_weekday += distribution_time[store]

    for store_row in range(len(stores)):
        if store1 == stores[store_row]:
            for store_col in range(len(stores)):
                if store2 == stores[store_col]:
                    time_weekday += travel_durations[store_row][store_col]

    if (demand_weekday < demand_threshold and time_weekday <= time_threshold):
        SouthRoutes_Weekday.append(South_Routes2[i])
        Routes_Weekday.append(South_Routes2[i])
        Time_Weekday.append(time_weekday/60/60)

for i in range(len(South_Routes3)):
    store1 = South_Routes3[i][0]
    store2 = South_Routes3[i][1]
    store3 = South_Routes3[i][2]
    demand_weekday = 0
    time_weekday = 0

    for j in range(len(South_stores)):
        if store1 == South_stores[j]:
            demand_weekday += South_WeekdayDemands[j]
            time_weekday += South_WeekdayDemands[j] * 450

    for k in range(len(South_stores)):
        if store2 == South_stores[k]:
            demand_weekday += South_WeekdayDemands[k]
            time_weekday += South_WeekdayDemands[k] * 450

    for l in range(len(South_stores)):
        if store3 == South_stores[l]:
            demand_weekday += South_WeekdayDemands[l]
            time_weekday += South_WeekdayDemands[l] * 450

    for store in range(len(stores)):
        if store1 == stores[store]:
            time_weekday += distribution_time[store]
        if store3 == stores[store]:
            time_weekday += distribution_time[store]

    for store_row in range(len(stores)):
        if store1 == stores[store_row]:
            for store_col in range(len(stores)):
                if store2 == stores[store_col]:
                    time_weekday += travel_durations[store_row][store_col]

    for store_row in range(len(stores)):
        if store2 == stores[store_row]:
            for store_col in range(len(stores)):
                if store3 == stores[store_col]:
                    time_weekday += travel_durations[store_row][store_col]
                    
    if (demand_weekday < demand_threshold and time_weekday <= time_threshold):
        SouthRoutes_Weekday.append(South_Routes3[i])
        Routes_Weekday.append(South_Routes3[i])
        Time_Weekday.append(time_weekday/60/60)

for i in range(len(South_Routes4)):
    store1 = South_Routes4[i][0]
    store2 = South_Routes4[i][1]
    store3 = South_Routes4[i][2]
    store4 = South_Routes4[i][3]
    demand_weekday = 0
    time_weekday = 0

    for j in range(len(South_stores)):
        if store1 == South_stores[j]:
            demand_weekday += South_WeekdayDemands[j]
            time_weekday += South_WeekdayDemands[j] * 450

    for k in range(len(South_stores)):
        if store2 == South_stores[k]:
            demand_weekday += South_WeekdayDemands[k]
            time_weekday += South_WeekdayDemands[k] * 450

    for l in range(len(South_stores)):
        if store3 == South_stores[l]:
            demand_weekday += South_WeekdayDemands[l]
            time_weekday += South_WeekdayDemands[l] * 450

    for m in range(len(South_stores)):
        if store4 == South_stores[m]:
            demand_weekday += South_WeekdayDemands[m]
            time_weekday += South_WeekdayDemands[m] * 450

    for store in range(len(stores)):
        if store1 == stores[store]:
            time_weekday += distribution_time[store]
        if store4 == stores[store]:
            time_weekday += distribution_time[store]

    for store_row in range(len(stores)):
        if store1 == stores[store_row]:
            for store_col in range(len(stores)):
                if store2 == stores[store_col]:
                    time_weekday += travel_durations[store_row][store_col]

    for store_row in range(len(stores)):
        if store2 == stores[store_row]:
            for store_col in range(len(stores)):
                if store3 == stores[store_col]:
                    time_weekday += travel_durations[store_row][store_col]

    for store_row in range(len(stores)):
        if store3 == stores[store_row]:
            for store_col in range(len(stores)):
                if store4 == stores[store_col]:
                    time_weekday += travel_durations[store_row][store_col]

    if (demand_weekday < demand_threshold and time_weekday <= time_threshold):
        SouthRoutes_Weekday.append(South_Routes4[i])
        Routes_Weekday.append(South_Routes4[i])
        Time_Weekday.append(time_weekday/60/60)

for i in range(len(South_Routes5)):
    store1 = South_Routes5[i][0]
    store2 = South_Routes5[i][1]
    store3 = South_Routes5[i][2]
    store4 = South_Routes5[i][3]
    store5 = South_Routes5[i][4]

    demand_weekday = 0
    time_weekday = 0

    for j in range(len(South_stores)):
        if store1 == South_stores[j]:
            demand_weekday += South_WeekdayDemands[j]
            time_weekday += South_WeekdayDemands[j] * 450

    for k in range(len(South_stores)):
        if store2 == South_stores[k]:
            demand_weekday += South_WeekdayDemands[k]
            time_weekday += South_WeekdayDemands[k] * 450

    for l in range(len(South_stores)):
        if store3 == South_stores[l]:
            demand_weekday += South_WeekdayDemands[l]
            time_weekday += South_WeekdayDemands[l] * 450

    for m in range(len(South_stores)):
        if store4 == South_stores[m]:
            demand_weekday += South_WeekdayDemands[m]
            time_weekday += South_WeekdayDemands[m] * 450

    for n in range(len(South_stores)):
        if store5 == South_stores[n]:
            demand_weekday += South_WeekdayDemands[n]
            time_weekday += South_WeekdayDemands[n] * 450

    for store in range(len(stores)):
        if store1 == stores[store]:
            time_weekday += distribution_time[store]
        if store5 == stores[store]:
            time_weekday += distribution_time[store]

    for store_row in range(len(stores)):
        if store1 == stores[store_row]:
            for store_col in range(len(stores)):
                if store2 == stores[store_col]:
                    time_weekday += travel_durations[store_row][store_col]

    for store_row in range(len(stores)):
        if store2 == stores[store_row]:
            for store_col in range(len(stores)):
                if store3 == stores[store_col]:
                    time_weekday += travel_durations[store_row][store_col]

    for store_row in range(len(stores)):
        if store3 == stores[store_row]:
            for store_col in range(len(stores)):
                if store4 == stores[store_col]:
                    time_weekday += travel_durations[store_row][store_col]

    for store_row in range(len(stores)):
        if store4 == stores[store_row]:
            for store_col in range(len(stores)):
                if store5 == stores[store_col]:
                    time_weekday += travel_durations[store_row][store_col]

    if (demand_weekday < demand_threshold and time_weekday <= time_threshold):
        SouthRoutes_Weekday.append(South_Routes5[i])
        Routes_Weekday.append(South_Routes5[i])
        Time_Weekday.append(time_weekday/60/60)

for i in range(len(South_Routes6)):
    store1 = South_Routes6[i][0]
    store2 = South_Routes6[i][1]
    store3 = South_Routes6[i][2]
    store4 = South_Routes6[i][3]
    store5 = South_Routes6[i][4]
    store6 = South_Routes6[i][5]

    demand_weekday = 0
    time_weekday = 0

    for j in range(len(South_stores)):
        if store1 == South_stores[j]:
            demand_weekday += South_WeekdayDemands[j]
            time_weekday += South_WeekdayDemands[j] * 450

    for k in range(len(South_stores)):
        if store2 == South_stores[k]:
            demand_weekday += South_WeekdayDemands[k]
            time_weekday += South_WeekdayDemands[k] * 450

    for l in range(len(South_stores)):
        if store3 == South_stores[l]:
            demand_weekday += South_WeekdayDemands[l]
            time_weekday += South_WeekdayDemands[l] * 450

    for m in range(len(South_stores)):
        if store4 == South_stores[m]:
            demand_weekday += South_WeekdayDemands[m]
            time_weekday += South_WeekdayDemands[m] * 450

    for n in range(len(South_stores)):
        if store5 == South_stores[n]:
            demand_weekday += South_WeekdayDemands[n]
            time_weekday += South_WeekdayDemands[n] * 450

    for o in range(len(South_stores)):
        if store6 == South_stores[o]:
            demand_weekday += South_WeekdayDemands[o]
            time_weekday += South_WeekdayDemands[o] * 450

    for store in range(len(stores)):
        if store1 == stores[store]:
            time_weekday += distribution_time[store]
        if store5 == stores[store]:
            time_weekday += distribution_time[store]

    for store_row in range(len(stores)):
        if store1 == stores[store_row]:
            for store_col in range(len(stores)):
                if store2 == stores[store_col]:
                    time_weekday += travel_durations[store_row][store_col]

    for store_row in range(len(stores)):
        if store2 == stores[store_row]:
            for store_col in range(len(stores)):
                if store3 == stores[store_col]:
                    time_weekday += travel_durations[store_row][store_col]

    for store_row in range(len(stores)):
        if store3 == stores[store_row]:
            for store_col in range(len(stores)):
                if store4 == stores[store_col]:
                    time_weekday += travel_durations[store_row][store_col]

    for store_row in range(len(stores)):
        if store4 == stores[store_row]:
            for store_col in range(len(stores)):
                if store5 == stores[store_col]:
                    time_weekday += travel_durations[store_row][store_col]

    for store_row in range(len(stores)):
        if store5 == stores[store_row]:
            for store_col in range(len(stores)):
                if store6 == stores[store_col]:
                    time_weekday += travel_durations[store_row][store_col]

    if (demand_weekday < demand_threshold and time_weekday <= time_threshold):
        SouthRoutes_Weekday.append(South_Routes6[i])
        Routes_Weekday.append(South_Routes6[i])
        Time_Weekday.append(time_weekday/60/60)

West_Routes2 = (list(combinations(West_stores, 2)))
West_Routes3 = (list(combinations(West_stores, 3)))
West_Routes4 = (list(combinations(West_stores, 4)))
West_Routes5 = (list(combinations(West_stores, 5)))
West_Routes6 = (list(combinations(West_stores, 6)))

for i in range(len(West_Routes2)):
    store1 = West_Routes2[i][0]
    store2 = West_Routes2[i][1]
    demand_weekday = 0
    time_weekday = 0

    for j in range(len(West_stores)):
        if store1 == West_stores[j]:
            demand_weekday += West_WeekdayDemands[j]
            time_weekday += West_WeekdayDemands[j] * 450

    for k in range(len(West_stores)):
        if store2 == West_stores[k]:
            demand_weekday += West_WeekdayDemands[k]
            time_weekday += West_WeekdayDemands[k] * 450

    for store in range(len(stores)):
        if store1 == stores[store]:
            time_weekday += distribution_time[store]
        if store2 == stores[store]:
            time_weekday += distribution_time[store]

    for store_row in range(len(stores)):
        if store1 == stores[store_row]:
            for store_col in range(len(stores)):
                if store2 == stores[store_col]:
                    time_weekday += travel_durations[store_row][store_col]

    if (demand_weekday < demand_threshold and time_weekday <= time_threshold):
        WestRoutes_Weekday.append(West_Routes2[i])
        Routes_Weekday.append(West_Routes2[i])
        Time_Weekday.append(time_weekday/60/60)

for i in range(len(West_Routes3)):
    store1 = West_Routes3[i][0]
    store2 = West_Routes3[i][1]
    store3 = West_Routes3[i][2]
    demand_weekday = 0
    time_weekday = 0

    for j in range(len(West_stores)):
        if store1 == West_stores[j]:
            demand_weekday += West_WeekdayDemands[j]
            time_weekday += West_WeekdayDemands[j] * 450

    for k in range(len(West_stores)):
        if store2 == West_stores[k]:
            demand_weekday += West_WeekdayDemands[k]
            time_weekday += West_WeekdayDemands[k] * 450

    for l in range(len(West_stores)):
        if store3 == West_stores[l]:
            demand_weekday += West_WeekdayDemands[l]
            time_weekday += West_WeekdayDemands[l] * 450

    for store in range(len(stores)):
        if store1 == stores[store]:
            time_weekday += distribution_time[store]
        if store3 == stores[store]:
            time_weekday += distribution_time[store]

    for store_row in range(len(stores)):
        if store1 == stores[store_row]:
            for store_col in range(len(stores)):
                if store2 == stores[store_col]:
                    time_weekday += travel_durations[store_row][store_col]

    for store_row in range(len(stores)):
        if store2 == stores[store_row]:
            for store_col in range(len(stores)):
                if store3 == stores[store_col]:
                    time_weekday += travel_durations[store_row][store_col]

    if (demand_weekday < demand_threshold and time_weekday <= time_threshold):
        WestRoutes_Weekday.append(West_Routes3[i])
        Routes_Weekday.append(West_Routes3[i])
        Time_Weekday.append(time_weekday/60/60)

for i in range(len(West_Routes4)):
    store1 = West_Routes4[i][0]
    store2 = West_Routes4[i][1]
    store3 = West_Routes4[i][2]
    store4 = West_Routes4[i][3]
    demand_weekday = 0
    time_weekday = 0

    for j in range(len(West_stores)):
        if store1 == West_stores[j]:
            demand_weekday += West_WeekdayDemands[j]
            time_weekday += West_WeekdayDemands[j] * 450

    for k in range(len(West_stores)):
        if store2 == West_stores[k]:
            demand_weekday += West_WeekdayDemands[k]
            time_weekday += West_WeekdayDemands[k] * 450

    for l in range(len(West_stores)):
        if store3 == West_stores[l]:
            demand_weekday += West_WeekdayDemands[l]
            time_weekday += West_WeekdayDemands[l] * 450

    for m in range(len(West_stores)):
        if store4 == West_stores[m]:
            demand_weekday += West_WeekdayDemands[m]
            time_weekday += West_WeekdayDemands[m] * 450

    for store in range(len(stores)):
        if store1 == stores[store]:
            time_weekday += distribution_time[store]
        if store4 == stores[store]:
            time_weekday += distribution_time[store]

    for store_row in range(len(stores)):
        if store1 == stores[store_row]:
            for store_col in range(len(stores)):
                if store2 == stores[store_col]:
                    time_weekday += travel_durations[store_row][store_col]

    for store_row in range(len(stores)):
        if store2 == stores[store_row]:
            for store_col in range(len(stores)):
                if store3 == stores[store_col]:
                    time_weekday += travel_durations[store_row][store_col]

    for store_row in range(len(stores)):
        if store3 == stores[store_row]:
            for store_col in range(len(stores)):
                if store4 == stores[store_col]:
                    time_weekday += travel_durations[store_row][store_col]

    if (demand_weekday < demand_threshold and time_weekday <= time_threshold):
        WestRoutes_Weekday.append(West_Routes4[i])
        Routes_Weekday.append(West_Routes4[i])
        Time_Weekday.append(time_weekday/60/60)

for i in range(len(West_Routes5)):
    store1 = West_Routes5[i][0]
    store2 = West_Routes5[i][1]
    store3 = West_Routes5[i][2]
    store4 = West_Routes5[i][3]
    store5 = West_Routes5[i][4]

    demand_weekday = 0
    time_weekday = 0

    for j in range(len(West_stores)):
        if store1 == West_stores[j]:
            demand_weekday += West_WeekdayDemands[j]
            time_weekday += West_WeekdayDemands[j] * 450

    for k in range(len(West_stores)):
        if store2 == West_stores[k]:
            demand_weekday += West_WeekdayDemands[k]
            time_weekday += West_WeekdayDemands[k] * 450

    for l in range(len(West_stores)):
        if store3 == West_stores[l]:
            demand_weekday += West_WeekdayDemands[l]
            time_weekday += West_WeekdayDemands[l] * 450

    for m in range(len(West_stores)):
        if store4 == West_stores[m]:
            demand_weekday += West_WeekdayDemands[m]
            time_weekday += West_WeekdayDemands[m] * 450

    for n in range(len(West_stores)):
        if store5 == West_stores[n]:
            demand_weekday += West_WeekdayDemands[n]
            time_weekday += West_WeekdayDemands[n] * 450

    for store in range(len(stores)):
        if store1 == stores[store]:
            time_weekday += distribution_time[store]
        if store5 == stores[store]:
            time_weekday += distribution_time[store]

    for store_row in range(len(stores)):
        if store1 == stores[store_row]:
            for store_col in range(len(stores)):
                if store2 == stores[store_col]:
                    time_weekday += travel_durations[store_row][store_col]

    for store_row in range(len(stores)):
        if store2 == stores[store_row]:
            for store_col in range(len(stores)):
                if store3 == stores[store_col]:
                    time_weekday += travel_durations[store_row][store_col]

    for store_row in range(len(stores)):
        if store3 == stores[store_row]:
            for store_col in range(len(stores)):
                if store4 == stores[store_col]:
                    time_weekday += travel_durations[store_row][store_col]

    for store_row in range(len(stores)):
        if store4 == stores[store_row]:
            for store_col in range(len(stores)):
                if store5 == stores[store_col]:
                    time_weekday += travel_durations[store_row][store_col]

    if (demand_weekday < demand_threshold and time_weekday <= time_threshold):
        WestRoutes_Weekday.append(West_Routes5[i])
        Routes_Weekday.append(West_Routes5[i])
        Time_Weekday.append(time_weekday/60/60)

for i in range(len(West_Routes6)):
    store1 = West_Routes6[i][0]
    store2 = West_Routes6[i][1]
    store3 = West_Routes6[i][2]
    store4 = West_Routes6[i][3]
    store5 = West_Routes6[i][4]
    store6 = West_Routes6[i][5]

    demand_weekday = 0
    time_weekday = 0

    for j in range(len(West_stores)):
        if store1 == West_stores[j]:
            demand_weekday += West_WeekdayDemands[j]
            time_weekday += West_WeekdayDemands[j] * 450

    for k in range(len(West_stores)):
        if store2 == West_stores[k]:
            demand_weekday += West_WeekdayDemands[k]
            time_weekday += West_WeekdayDemands[k] * 450

    for l in range(len(West_stores)):
        if store3 == West_stores[l]:
            demand_weekday += West_WeekdayDemands[l]
            time_weekday += West_WeekdayDemands[l] * 450

    for m in range(len(West_stores)):
        if store4 == West_stores[m]:
            demand_weekday += West_WeekdayDemands[m]
            time_weekday += West_WeekdayDemands[m] * 450

    for n in range(len(West_stores)):
        if store5 == West_stores[n]:
            demand_weekday += West_WeekdayDemands[n]
            time_weekday += West_WeekdayDemands[n] * 450

    for o in range(len(West_stores)):
        if store6 == West_stores[o]:
            demand_weekday += West_WeekdayDemands[o]
            time_weekday += West_WeekdayDemands[o] * 450

    for store in range(len(stores)):
        if store1 == stores[store]:
            time_weekday += distribution_time[store]
        if store5 == stores[store]:
            time_weekday += distribution_time[store]

    for store_row in range(len(stores)):
        if store1 == stores[store_row]:
            for store_col in range(len(stores)):
                if store2 == stores[store_col]:
                    time_weekday += travel_durations[store_row][store_col]

    for store_row in range(len(stores)):
        if store2 == stores[store_row]:
            for store_col in range(len(stores)):
                if store3 == stores[store_col]:
                    time_weekday += travel_durations[store_row][store_col]

    for store_row in range(len(stores)):
        if store3 == stores[store_row]:
            for store_col in range(len(stores)):
                if store4 == stores[store_col]:
                    time_weekday += travel_durations[store_row][store_col]

    for store_row in range(len(stores)):
        if store4 == stores[store_row]:
            for store_col in range(len(stores)):
                if store5 == stores[store_col]:
                    time_weekday += travel_durations[store_row][store_col]

    for store_row in range(len(stores)):
        if store5 == stores[store_row]:
            for store_col in range(len(stores)):
                if store6 == stores[store_col]:
                    time_weekday += travel_durations[store_row][store_col]

    if (demand_weekday < demand_threshold and time_weekday <= time_threshold):
        WestRoutes_Weekday.append(West_Routes6[i])
        Routes_Weekday.append(West_Routes6[i])
        Time_Weekday.append(time_weekday/60/60)

East_Routes2 = (list(combinations(East_stores, 2)))
East_Routes3 = (list(combinations(East_stores, 3)))
East_Routes4 = (list(combinations(East_stores, 4)))
East_Routes5 = (list(combinations(East_stores, 5)))
East_Routes6 = (list(combinations(East_stores, 6)))

for i in range(len(East_Routes2)):
    store1 = East_Routes2[i][0]
    store2 = East_Routes2[i][1]
    demand_weekday = 0
    time_weekday = 0

    for j in range(len(East_stores)):
        if store1 == East_stores[j]:
            demand_weekday += East_WeekdayDemands[j]
            time_weekday += East_WeekdayDemands[j] * 450

    for k in range(len(East_stores)):
        if store2 == East_stores[k]:
            demand_weekday += East_WeekdayDemands[k]
            time_weekday += East_WeekdayDemands[k] * 450

    for store in range(len(stores)):
        if store1 == stores[store]:
            time_weekday += distribution_time[store]
        if store2 == stores[store]:
            time_weekday += distribution_time[store]

    for store_row in range(len(stores)):
        if store1 == stores[store_row]:
            for store_col in range(len(stores)):
                if store2 == stores[store_col]:
                    time_weekday += travel_durations[store_row][store_col]

    if (demand_weekday < demand_threshold and time_weekday <= time_threshold):
        EastRoutes_Weekday.append(East_Routes2[i])
        Routes_Weekday.append(East_Routes2[i])
        Time_Weekday.append(time_weekday/60/60)

for i in range(len(East_Routes3)):
    store1 = East_Routes3[i][0]
    store2 = East_Routes3[i][1]
    store3 = East_Routes3[i][2]
    demand_weekday = 0
    time_weekday = 0

    for j in range(len(East_stores)):
        if store1 == East_stores[j]:
            demand_weekday += East_WeekdayDemands[j]
            time_weekday += East_WeekdayDemands[j] * 450

    for k in range(len(East_stores)):
        if store2 == East_stores[k]:
            demand_weekday += East_WeekdayDemands[k]
            time_weekday += East_WeekdayDemands[k] * 450

    for l in range(len(East_stores)):
        if store3 == East_stores[l]:
            demand_weekday += East_WeekdayDemands[l]
            time_weekday += East_WeekdayDemands[l] * 450

    for store in range(len(stores)):
        if store1 == stores[store]:
            time_weekday += distribution_time[store]
        if store3 == stores[store]:
            time_weekday += distribution_time[store]

    for store_row in range(len(stores)):
        if store1 == stores[store_row]:
            for store_col in range(len(stores)):
                if store2 == stores[store_col]:
                    time_weekday += travel_durations[store_row][store_col]

    for store_row in range(len(stores)):
        if store2 == stores[store_row]:
            for store_col in range(len(stores)):
                if store3 == stores[store_col]:
                    time_weekday += travel_durations[store_row][store_col]

    if (demand_weekday < demand_threshold and time_weekday <= time_threshold):
        EastRoutes_Weekday.append(East_Routes3[i])
        Routes_Weekday.append(East_Routes3[i])
        Time_Weekday.append(time_weekday/60/60)

for i in range(len(East_Routes4)):
    store1 = East_Routes4[i][0]
    store2 = East_Routes4[i][1]
    store3 = East_Routes4[i][2]
    store4 = East_Routes4[i][3]
    demand_weekday = 0
    time_weekday = 0

    for j in range(len(East_stores)):
        if store1 == East_stores[j]:
            demand_weekday += East_WeekdayDemands[j]
            time_weekday += East_WeekdayDemands[j] * 450

    for k in range(len(East_stores)):
        if store2 == East_stores[k]:
            demand_weekday += East_WeekdayDemands[k]
            time_weekday += East_WeekdayDemands[k] * 450

    for l in range(len(East_stores)):
        if store3 == East_stores[l]:
            demand_weekday += East_WeekdayDemands[l]
            time_weekday += East_WeekdayDemands[l] * 450

    for m in range(len(East_stores)):
        if store4 == East_stores[m]:
            demand_weekday += East_WeekdayDemands[m]
            time_weekday += East_WeekdayDemands[m] * 450

    for store in range(len(stores)):
        if store1 == stores[store]:
            time_weekday += distribution_time[store]
        if store4 == stores[store]:
            time_weekday += distribution_time[store]

    for store_row in range(len(stores)):
        if store1 == stores[store_row]:
            for store_col in range(len(stores)):
                if store2 == stores[store_col]:
                    time_weekday += travel_durations[store_row][store_col]

    for store_row in range(len(stores)):
        if store2 == stores[store_row]:
            for store_col in range(len(stores)):
                if store3 == stores[store_col]:
                    time_weekday += travel_durations[store_row][store_col]

    for store_row in range(len(stores)):
        if store3 == stores[store_row]:
            for store_col in range(len(stores)):
                if store4 == stores[store_col]:
                    time_weekday += travel_durations[store_row][store_col]

    if (demand_weekday < demand_threshold and time_weekday <= time_threshold):
        EastRoutes_Weekday.append(East_Routes4[i])
        Routes_Weekday.append(East_Routes4[i])
        Time_Weekday.append(time_weekday/60/60)

for i in range(len(East_Routes5)):
    store1 = East_Routes5[i][0]
    store2 = East_Routes5[i][1]
    store3 = East_Routes5[i][2]
    store4 = East_Routes5[i][3]
    store5 = East_Routes5[i][4]

    demand_weekday = 0
    time_weekday = 0

    for j in range(len(East_stores)):
        if store1 == East_stores[j]:
            demand_weekday += East_WeekdayDemands[j]
            time_weekday += East_WeekdayDemands[j] * 450

    for k in range(len(East_stores)):
        if store2 == East_stores[k]:
            demand_weekday += East_WeekdayDemands[k]
            time_weekday += East_WeekdayDemands[k] * 450

    for l in range(len(East_stores)):
        if store3 == East_stores[l]:
            demand_weekday += East_WeekdayDemands[l]
            time_weekday += East_WeekdayDemands[l] * 450

    for m in range(len(East_stores)):
        if store4 == East_stores[m]:
            demand_weekday += East_WeekdayDemands[m]
            time_weekday += East_WeekdayDemands[m] * 450

    for n in range(len(East_stores)):
        if store5 == East_stores[n]:
            demand_weekday += East_WeekdayDemands[n]
            time_weekday += East_WeekdayDemands[n] * 450

    for store in range(len(stores)):
        if store1 == stores[store]:
            time_weekday += distribution_time[store]
        if store5 == stores[store]:
            time_weekday += distribution_time[store]

    for store_row in range(len(stores)):
        if store1 == stores[store_row]:
            for store_col in range(len(stores)):
                if store2 == stores[store_col]:
                    time_weekday += travel_durations[store_row][store_col]

    for store_row in range(len(stores)):
        if store2 == stores[store_row]:
            for store_col in range(len(stores)):
                if store3 == stores[store_col]:
                    time_weekday += travel_durations[store_row][store_col]

    for store_row in range(len(stores)):
        if store3 == stores[store_row]:
            for store_col in range(len(stores)):
                if store4 == stores[store_col]:
                    time_weekday += travel_durations[store_row][store_col]

    for store_row in range(len(stores)):
        if store4 == stores[store_row]:
            for store_col in range(len(stores)):
                if store5 == stores[store_col]:
                    time_weekday += travel_durations[store_row][store_col]

    if (demand_weekday < demand_threshold and time_weekday <= time_threshold):
        EastRoutes_Weekday.append(East_Routes5[i])
        Routes_Weekday.append(East_Routes5[i])
        Time_Weekday.append(time_weekday/60/60)

for i in range(len(East_Routes6)):
    store1 = East_Routes6[i][0]
    store2 = East_Routes6[i][1]
    store3 = East_Routes6[i][2]
    store4 = East_Routes6[i][3]
    store5 = East_Routes6[i][4]
    store6 = East_Routes6[i][5]

    demand_weekday = 0
    time_weekday = 0

    for j in range(len(East_stores)):
        if store1 == East_stores[j]:
            demand_weekday += East_WeekdayDemands[j]
            time_weekday += East_WeekdayDemands[j] * 450

    for k in range(len(East_stores)):
        if store2 == East_stores[k]:
            demand_weekday += East_WeekdayDemands[k]
            time_weekday += East_WeekdayDemands[k] * 450

    for l in range(len(East_stores)):
        if store3 == East_stores[l]:
            demand_weekday += East_WeekdayDemands[l]
            time_weekday += East_WeekdayDemands[l] * 450

    for m in range(len(East_stores)):
        if store4 == East_stores[m]:
            demand_weekday += East_WeekdayDemands[m]
            time_weekday += East_WeekdayDemands[m] * 450

    for n in range(len(East_stores)):
        if store5 == East_stores[n]:
            demand_weekday += East_WeekdayDemands[n]
            time_weekday += East_WeekdayDemands[n] * 450

    for o in range(len(East_stores)):
        if store6 == East_stores[o]:
            demand_weekday += East_WeekdayDemands[o]
            time_weekday += East_WeekdayDemands[o] * 450

    for store in range(len(stores)):
        if store1 == stores[store]:
            time_weekday += distribution_time[store]
        if store5 == stores[store]:
            time_weekday += distribution_time[store]

    for store_row in range(len(stores)):
        if store1 == stores[store_row]:
            for store_col in range(len(stores)):
                if store2 == stores[store_col]:
                    time_weekday += travel_durations[store_row][store_col]

    for store_row in range(len(stores)):
        if store2 == stores[store_row]:
            for store_col in range(len(stores)):
                if store3 == stores[store_col]:
                    time_weekday += travel_durations[store_row][store_col]

    for store_row in range(len(stores)):
        if store3 == stores[store_row]:
            for store_col in range(len(stores)):
                if store4 == stores[store_col]:
                    time_weekday += travel_durations[store_row][store_col]

    for store_row in range(len(stores)):
        if store4 == stores[store_row]:
            for store_col in range(len(stores)):
                if store5 == stores[store_col]:
                    time_weekday += travel_durations[store_row][store_col]

    for store_row in range(len(stores)):
        if store5 == stores[store_row]:
            for store_col in range(len(stores)):
                if store6 == stores[store_col]:
                    time_weekday += travel_durations[store_row][store_col]

    if (demand_weekday < demand_threshold and time_weekday <= time_threshold):
        EastRoutes_Weekday.append(East_Routes6[i])
        Routes_Weekday.append(East_Routes6[i])
        Time_Weekday.append(time_weekday/60/60)

max_routes = 60

# Listing the possible number of routes
weekday_possible_routes = [i for i in range(0,len(Routes_Weekday))]

# Setting up the number of variables needed
WeekdayRoute_vars = LpVariable.dicts("Weekday_Route", weekday_possible_routes, 0, None, 'Integer')

# Setting up the minimisation objective function
prob_weekday = LpProblem("Woolworths NZ VRP weekday", LpMinimize)

# Objective function
prob_weekday += lpSum([225 * WeekdayRoute_vars[route] * Time_Weekday[route] if Time_Weekday[route] < 4 else (225 * WeekdayRoute_vars[route] * 4) + (275 * WeekdayRoute_vars[route] * (Time_Weekday[route] - 4)) for route in weekday_possible_routes])

# Adding the constraints
prob_weekday += lpSum([WeekdayRoute_vars[route] for route in weekday_possible_routes]) <= max_routes

for store in stores:
    prob_weekday += lpSum([WeekdayRoute_vars[route] for route in weekday_possible_routes if store in Routes_Weekday[route]]) == 1

# Writing the LP to a file
prob_weekday.writeLP("" + os.getcwd() + os.sep + "LP_files" + os.sep + "WoolworthsVRP_weekday_closure.lp")

# Solving the LP
prob_weekday.solve(PULP_CBC_CMD(msg=0))

weekday_status = LpStatus[prob_weekday.status]
least_cost_weekdays = value(prob_weekday.objective)

optimalRoutes_weekday = []
num_weekday = 0
for v in prob_weekday.variables():
    if v.varValue == 1:
        optimalRoutes_weekday.append(v.name)
        num_weekday += 1