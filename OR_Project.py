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
CentralNorth_WeekendDemands = np.genfromtxt("" + os.getcwd() + os.sep + "Data" + os.sep + "LocationCentralNorth.csv", delimiter= ',', skip_header=1, usecols=2)

# Find median demands of each day for every store in Central South
CentralSouth_WeekdayDemands = np.genfromtxt("" + os.getcwd() + os.sep + "Data" + os.sep + "LocationCentralSouth.csv", delimiter= ',', skip_header=1, usecols=1)
CentralSouth_WeekendDemands = np.genfromtxt("" + os.getcwd() + os.sep + "Data" + os.sep + "LocationCentralSouth.csv", delimiter= ',', skip_header=1, usecols=2)

# Find median demands of each day for every store in North
North_WeekdayDemands = np.genfromtxt("" + os.getcwd() + os.sep + "Data" + os.sep + "LocationNorthRegion.csv", delimiter= ',', skip_header=1, usecols=1)
North_WeekendDemands = np.genfromtxt("" + os.getcwd() + os.sep + "Data" + os.sep + "LocationNorthRegion.csv", delimiter= ',', skip_header=1, usecols=2)

# Find median demands of each day for every store in South
South_WeekdayDemands = np.genfromtxt("" + os.getcwd() + os.sep + "Data" + os.sep + "LocationSouthRegion.csv", delimiter= ',', skip_header=1, usecols=1)
South_WeekendDemands = np.genfromtxt("" + os.getcwd() + os.sep + "Data" + os.sep + "LocationSouthRegion.csv", delimiter= ',', skip_header=1, usecols=2)

# Find median demands of each day for every store in West
West_WeekdayDemands = np.genfromtxt("" + os.getcwd() + os.sep + "Data" + os.sep + "LocationWestRegion.csv", delimiter= ',', skip_header=1, usecols=1)
West_WeekendDemands = np.genfromtxt("" + os.getcwd() + os.sep + "Data" + os.sep + "LocationWestRegion.csv", delimiter= ',', skip_header=1, usecols=2)

# Find median demands of each day for every store in East
East_WeekdayDemands = np.genfromtxt("" + os.getcwd() + os.sep + "Data" + os.sep + "LocationEastRegion.csv", delimiter= ',', skip_header=1, usecols=1)
East_WeekendDemands = np.genfromtxt("" + os.getcwd() + os.sep + "Data" + os.sep + "LocationEastRegion.csv", delimiter= ',', skip_header=1, usecols=2)

demand_threshold = 27
time_threshold = 60 * 4 * 2 * 30

Routes_Weekday = []
Routes_Weekend = []
Time_Weekday = []
Time_Weekend = []

CentralNorthRoutes_Weekday = []
CentralNorthRoutes_Weekend = []

CentralSouthRoutes_Weekday = []
CentralSouthRoutes_Weekend = []

NorthRoutes_Weekday = []
NorthRoutes_Weekend = []

SouthRoutes_Weekday = []
SouthRoutes_Weekend = []

WestRoutes_Weekday = []
WestRoutes_Weekend = []

EastRoutes_Weekday = []
EastRoutes_Weekend = []

CentralNorth_Routes2 = (list(combinations(CentralNorth_stores, 2)))
CentralNorth_Routes3 = (list(combinations(CentralNorth_stores, 3)))
CentralNorth_Routes4 = (list(combinations(CentralNorth_stores, 4)))
CentralNorth_Routes5 = (list(combinations(CentralNorth_stores, 5)))

for i in range(len(CentralNorth_Routes2)):
    store1 = CentralNorth_Routes2[i][0]
    store2 = CentralNorth_Routes2[i][1]
    demand_weekday = 0
    demand_weekend = 0
    time_weekday = 0
    time_weekend = 0

    for j in range(len(CentralNorth_stores)):
        if store1 == CentralNorth_stores[j]:
            demand_weekday += CentralNorth_WeekdayDemands[j]
            demand_weekend += CentralNorth_WeekendDemands[j]
            time_weekday += CentralNorth_WeekdayDemands[j] * 450
            time_weekend += CentralNorth_WeekdayDemands[j] * 450

    for k in range(len(CentralNorth_stores)):
        if store2 == CentralNorth_stores[k]:
            demand_weekday += CentralNorth_WeekdayDemands[k]
            demand_weekend += CentralNorth_WeekendDemands[k]
            time_weekday += CentralNorth_WeekdayDemands[k] * 450
            time_weekend += CentralNorth_WeekdayDemands[k] * 450

    for store in range(len(stores)):
        if store1 == stores[store]:
            time_weekday += distribution_time[store]
            time_weekend += distribution_time[store]
        if store2 == stores[store]:
            time_weekday += distribution_time[store]
            time_weekend += distribution_time[store]

    for store_row in range(len(stores)):
        if store1 == stores[store_row]:
            for store_col in range(len(stores)):
                if store2 == stores[store_col]:
                    time_weekday += travel_durations[store_row][store_col]
                    time_weekend += travel_durations[store_row][store_col]

    if (demand_weekday < demand_threshold and time_weekday < time_threshold):
        CentralNorthRoutes_Weekday.append(CentralNorth_Routes2[i])
        Routes_Weekday.append(CentralNorth_Routes2[i])
        Time_Weekday.append(time_weekday/60/60)
        
    if (demand_weekend < demand_threshold and time_weekend < time_threshold):
        CentralNorthRoutes_Weekend.append(CentralNorth_Routes2[i])
        Routes_Weekend.append(CentralNorth_Routes2[i])
        Time_Weekend.append(time_weekend/60/60)

for i in range(len(CentralNorth_Routes3)):
    store1 = CentralNorth_Routes3[i][0]
    store2 = CentralNorth_Routes3[i][1]
    store3 = CentralNorth_Routes3[i][2]
    demand_weekday = 0
    demand_weekend = 0
    time_weekday = 0
    time_weekend = 0

    for j in range(len(CentralNorth_stores)):
        if store1 == CentralNorth_stores[j]:
            demand_weekday += CentralNorth_WeekdayDemands[j]
            demand_weekend += CentralNorth_WeekendDemands[j]
            time_weekday += CentralNorth_WeekdayDemands[j] * 450
            time_weekend += CentralNorth_WeekdayDemands[j] * 450

    for k in range(len(CentralNorth_stores)):
        if store2 == CentralNorth_stores[k]:
            demand_weekday += CentralNorth_WeekdayDemands[k]
            demand_weekend += CentralNorth_WeekendDemands[k]
            time_weekday += CentralNorth_WeekdayDemands[k] * 450
            time_weekend += CentralNorth_WeekdayDemands[k] * 450

    for l in range(len(CentralNorth_stores)):
        if store3 == CentralNorth_stores[l]:
            demand_weekday += CentralNorth_WeekdayDemands[l]
            demand_weekend += CentralNorth_WeekendDemands[l]
            time_weekday += CentralNorth_WeekdayDemands[l] * 450
            time_weekend += CentralNorth_WeekdayDemands[l] * 450

    for store in range(len(stores)):
        if store1 == stores[store]:
            time_weekday += distribution_time[store]
            time_weekend += distribution_time[store]            
        if store3 == stores[store]:
            time_weekday += distribution_time[store]
            time_weekend += distribution_time[store]

    for store_row in range(len(stores)):
        if store1 == stores[store_row]:
            for store_col in range(len(stores)):
                if store2 == stores[store_col]:
                    time_weekday += travel_durations[store_row][store_col]
                    time_weekend += travel_durations[store_row][store_col]

    for store_row in range(len(stores)):
        if store2 == stores[store_row]:
            for store_col in range(len(stores)):
                if store3 == stores[store_col]:
                    time_weekday += travel_durations[store_row][store_col]
                    time_weekend += travel_durations[store_row][store_col]

    if (demand_weekday < demand_threshold and time_weekday < time_threshold):
        CentralNorthRoutes_Weekday.append(CentralNorth_Routes3[i])
        Routes_Weekday.append(CentralNorth_Routes3[i])
        Time_Weekday.append(time_weekday/60/60)

    if (demand_weekend < demand_threshold and time_weekend < time_threshold):
        CentralNorthRoutes_Weekend.append(CentralNorth_Routes3[i])
        Routes_Weekend.append(CentralNorth_Routes3[i])
        Time_Weekend.append(time_weekend/60/60)

for i in range(len(CentralNorth_Routes4)):
    store1 = CentralNorth_Routes4[i][0]
    store2 = CentralNorth_Routes4[i][1]
    store3 = CentralNorth_Routes4[i][2]
    store4 = CentralNorth_Routes4[i][3]
    demand_weekday = 0
    demand_weekend = 0
    time_weekday = 0
    time_weekend = 0

    for j in range(len(CentralNorth_stores)):
        if store1 == CentralNorth_stores[j]:
            demand_weekday += CentralNorth_WeekdayDemands[j]
            demand_weekend += CentralNorth_WeekendDemands[j]
            time_weekday += CentralNorth_WeekdayDemands[j] * 450
            time_weekend += CentralNorth_WeekdayDemands[j] * 450

    for k in range(len(CentralNorth_stores)):
        if store2 == CentralNorth_stores[k]:
            demand_weekday += CentralNorth_WeekdayDemands[k]
            demand_weekend += CentralNorth_WeekendDemands[k]
            time_weekday += CentralNorth_WeekdayDemands[k] * 450
            time_weekend += CentralNorth_WeekdayDemands[k] * 450

    for l in range(len(CentralNorth_stores)):
        if store3 == CentralNorth_stores[l]:
            demand_weekday += CentralNorth_WeekdayDemands[l]
            demand_weekend += CentralNorth_WeekendDemands[l]
            time_weekday += CentralNorth_WeekdayDemands[l] * 450
            time_weekend += CentralNorth_WeekdayDemands[l] * 450

    for m in range(len(CentralNorth_stores)):
        if store4 == CentralNorth_stores[m]:
            demand_weekday += CentralNorth_WeekdayDemands[m]
            demand_weekend += CentralNorth_WeekendDemands[m]
            time_weekday += CentralNorth_WeekdayDemands[m] * 450
            time_weekend += CentralNorth_WeekdayDemands[m] * 450

    for store in range(len(stores)):
        if store1 == stores[store]:
            time_weekday += distribution_time[store]
            time_weekend += distribution_time[store]
        if store4 == stores[store]:
            time_weekday += distribution_time[store]
            time_weekend += distribution_time[store]

    for store_row in range(len(stores)):
        if store1 == stores[store_row]:
            for store_col in range(len(stores)):
                if store2 == stores[store_col]:
                    time_weekday += travel_durations[store_row][store_col]
                    time_weekend += travel_durations[store_row][store_col]

    for store_row in range(len(stores)):
        if store2 == stores[store_row]:
            for store_col in range(len(stores)):
                if store3 == stores[store_col]:
                    time_weekday += travel_durations[store_row][store_col]
                    time_weekend += travel_durations[store_row][store_col]

    for store_row in range(len(stores)):
        if store3 == stores[store_row]:
            for store_col in range(len(stores)):
                if store4 == stores[store_col]:
                    time_weekday += travel_durations[store_row][store_col]
                    time_weekend += travel_durations[store_row][store_col]

    if (demand_weekday < demand_threshold and time_weekday < time_threshold):
        CentralNorthRoutes_Weekday.append(CentralNorth_Routes4[i])
        Routes_Weekday.append(CentralNorth_Routes4[i])
        Time_Weekday.append(time_weekday/60/60)
        Cost_Weekday.append(time / 60 / 60 * 225)

    if (demand_weekend < demand_threshold and time_weekend < time_threshold):
        CentralNorthRoutes_Weekend.append(CentralNorth_Routes4[i])
        Routes_Weekend.append(CentralNorth_Routes4[i])
        Time_Weekend.append(time/60/60)
        Cost_Weekend.append(time_weekend / 60 / 60 * 225)

for i in range(len(CentralNorth_Routes5)):
    store1 = CentralNorth_Routes5[i][0]
    store2 = CentralNorth_Routes5[i][1]
    store3 = CentralNorth_Routes5[i][2]
    store4 = CentralNorth_Routes5[i][3]
    store5 = CentralNorth_Routes5[i][4]

    demand_weekday = 0
    demand_weekend = 0
    time_weekday = 0
    time_weekend = 0

    for j in range(len(CentralNorth_stores)):
        if store1 == CentralNorth_stores[j]:
            demand_weekday += CentralNorth_WeekdayDemands[j]
            demand_weekend += CentralNorth_WeekendDemands[j]
            time_weekday += CentralNorth_WeekdayDemands[j] * 450
            time_weekend += CentralNorth_WeekdayDemands[j] * 450

    for k in range(len(CentralNorth_stores)):
        if store2 == CentralNorth_stores[k]:
            demand_weekday += CentralNorth_WeekdayDemands[k]
            demand_weekend += CentralNorth_WeekendDemands[k]
            time_weekday += CentralNorth_WeekdayDemands[k] * 450
            time_weekend += CentralNorth_WeekdayDemands[k] * 450

    for l in range(len(CentralNorth_stores)):
        if store3 == CentralNorth_stores[l]:
            demand_weekday += CentralNorth_WeekdayDemands[l]
            demand_weekend += CentralNorth_WeekendDemands[l]
            time_weekday += CentralNorth_WeekdayDemands[l] * 450
            time_weekend += CentralNorth_WeekdayDemands[l] * 450

    for m in range(len(CentralNorth_stores)):
        if store4 == CentralNorth_stores[m]:
            demand_weekday += CentralNorth_WeekdayDemands[m]
            demand_weekend += CentralNorth_WeekendDemands[m]
            time_weekday += CentralNorth_WeekdayDemands[m] * 450
            time_weekend += CentralNorth_WeekdayDemands[m] * 450

    for n in range(len(CentralNorth_stores)):
        if store4 == CentralNorth_stores[n]:
            demand_weekday += CentralNorth_WeekdayDemands[n]
            demand_weekend += CentralNorth_WeekendDemands[n]
            time_weekday += CentralNorth_WeekdayDemands[n] * 450
            time_weekend += CentralNorth_WeekdayDemands[n] * 450

    for store in range(len(stores)):
        if store1 == stores[store]:
            time_weekday += distribution_time[store]
            time_weekend += distribution_time[store]
        if store5 == stores[store]:
            time_weekday += distribution_time[store]
            time_weekend += distribution_time[store]

    for store_row in range(len(stores)):
        if store1 == stores[store_row]:
            for store_col in range(len(stores)):
                if store2 == stores[store_col]:
                    time_weekday += travel_durations[store_row][store_col]
                    time_weekend += travel_durations[store_row][store_col]

    for store_row in range(len(stores)):
        if store2 == stores[store_row]:
            for store_col in range(len(stores)):
                if store3 == stores[store_col]:
                    time_weekday += travel_durations[store_row][store_col]
                    time_weekend += travel_durations[store_row][store_col]

    for store_row in range(len(stores)):
        if store3 == stores[store_row]:
            for store_col in range(len(stores)):
                if store4 == stores[store_col]:
                    time_weekday += travel_durations[store_row][store_col]
                    time_weekend += travel_durations[store_row][store_col]

    for store_row in range(len(stores)):
        if store4 == stores[store_row]:
            for store_col in range(len(stores)):
                if store5 == stores[store_col]:
                    time_weekday += travel_durations[store_row][store_col]
                    time_weekend += travel_durations[store_row][store_col]

    if (demand_weekday < demand_threshold and time_weekday < time_threshold):
        CentralNorthRoutes_Weekday.append(CentralNorth_Routes5[i])
        Routes_Weekday.append(CentralNorth_Routes5[i])
        Time_Weekday.append(time_weekday/60/60)

    if (demand_weekend < demand_threshold and time_weekend < time_threshold):
        CentralNorthRoutes_Weekend.append(CentralNorth_Routes5[i])
        Routes_Weekend.append(CentralNorth_Routes5[i])
        Time_Weekend.append(time_weekend/60/60)

CentralSouth_Routes2 = (list(combinations(CentralSouth_stores, 2)))
CentralSouth_Routes3 = (list(combinations(CentralSouth_stores, 3)))
CentralSouth_Routes4 = (list(combinations(CentralSouth_stores, 4)))
CentralSouth_Routes5 = (list(combinations(CentralSouth_stores, 5)))

for i in range(len(CentralSouth_Routes2)):
    store1 = CentralSouth_Routes2[i][0]
    store2 = CentralSouth_Routes2[i][1]
    demand_weekday = 0
    demand_weekend = 0
    time_weekday = 0
    time_weekend = 0

    for j in range(len(CentralSouth_stores)):
        if store1 == CentralSouth_stores[j]:
            demand_weekday += CentralSouth_WeekdayDemands[j]
            demand_weekend += CentralSouth_WeekendDemands[j]
            time_weekday += CentralSouth_WeekdayDemands[j] * 450
            time_weekend += CentralSouth_WeekendDemands[j] * 450

    for k in range(len(CentralNorth_stores)):
        if store2 == CentralNorth_stores[k]:
            demand_weekday += CentralSouth_WeekdayDemands[k]
            demand_weekend += CentralSouth_WeekendDemands[k]
            time_weekday += CentralSouth_WeekdayDemands[k] * 450
            time_weekend += CentralSouth_WeekendDemands[k] * 450

    for store in range(len(stores)):
        if store1 == stores[store]:
            time_weekday += distribution_time[store]
            time_weekend += distribution_time[store]
        if store2 == stores[store]:
            time_weekday += distribution_time[store]
            time_weekend += distribution_time[store]

    for store_row in range(len(stores)):
        if store1 == stores[store_row]:
            for store_col in range(len(stores)):
                if store2 == stores[store_col]:
                    time_weekday += travel_durations[store_row][store_col]
                    time_weekend += travel_durations[store_row][store_col]

    if (demand_weekday < demand_threshold and time_weekday < time_threshold):
        CentralSouthRoutes_Weekday.append(CentralSouth_Routes2[i])
        Routes_Weekday.append(CentralSouth_Routes2[i])
        Time_Weekday.append(time_weekday/60/60)

    if (demand_weekend < demand_threshold and time_weekend < time_threshold):
        CentralSouthRoutes_Weekend.append(CentralSouth_Routes2[i])
        Routes_Weekend.append(CentralSouth_Routes2[i])
        Time_Weekend.append(time_weekend/60/60)

for i in range(len(CentralSouth_Routes3)):
    store1 = CentralSouth_Routes3[i][0]
    store2 = CentralSouth_Routes3[i][1]
    store3 = CentralSouth_Routes3[i][2]
    demand_weekday = 0
    demand_weekend = 0
    time_weekday = 0
    time_weekend = 0

    for j in range(len(CentralSouth_stores)):
        if store1 == CentralSouth_stores[j]:
            demand_weekday += CentralSouth_WeekdayDemands[j]
            demand_weekend += CentralSouth_WeekendDemands[j]
            time_weekday += CentralSouth_WeekdayDemands[j] * 450
            time_weekend += CentralSouth_WeekendDemands[j] * 450

    for k in range(len(CentralSouth_stores)):
        if store2 == CentralSouth_stores[k]:
            demand_weekday += CentralSouth_WeekdayDemands[k]
            demand_weekend += CentralSouth_WeekendDemands[k]
            time_weekday += CentralSouth_WeekdayDemands[k] * 450
            time_weekend += CentralSouth_WeekendDemands[k] * 450

    for l in range(len(CentralSouth_stores)):
        if store3 == CentralSouth_stores[l]:
            demand_weekday += CentralSouth_WeekdayDemands[l]
            demand_weekend += CentralSouth_WeekendDemands[l]
            time_weekday += CentralSouth_WeekdayDemands[l] * 450
            time_weekend += CentralSouth_WeekendDemands[l] * 450

    for store in range(len(stores)):
        if store1 == stores[store]:
            time_weekday += distribution_time[store]
            time_weekend += distribution_time[store]
        if store3 == stores[store]:
            time_weekday += distribution_time[store]
            time_weekend += distribution_time[store]

    for store_row in range(len(stores)):
        if store1 == stores[store_row]:
            for store_col in range(len(stores)):
                if store2 == stores[store_col]:
                    time_weekday += travel_durations[store_row][store_col]
                    time_weekend += travel_durations[store_row][store_col]

    for store_row in range(len(stores)):
        if store2 == stores[store_row]:
            for store_col in range(len(stores)):
                if store3 == stores[store_col]:
                    time_weekday += travel_durations[store_row][store_col]
                    time_weekend += travel_durations[store_row][store_col]

    if (demand_weekday < demand_threshold and time_weekday < time_threshold):
        CentralSouthRoutes_Weekday.append(CentralSouth_Routes3[i])
        Routes_Weekday.append(CentralSouth_Routes3[i])
        Time_Weekday.append(time_weekday/60/60)

    if (demand_weekend < demand_threshold and time_weekend < time_threshold):
        CentralSouthRoutes_Weekend.append(CentralSouth_Routes3[i])
        Routes_Weekend.append(CentralSouth_Routes3[i])
        Time_Weekend.append(time_weekend/60/60)

for i in range(len(CentralSouth_Routes4)):
    
    store1 = CentralSouth_Routes4[i][0]
    store2 = CentralSouth_Routes4[i][1]
    store3 = CentralSouth_Routes4[i][2]
    store4 = CentralSouth_Routes4[i][3]
    demand_weekday = 0
    demand_weekend = 0
    time_weekday = 0
    time_weekend = 0

    for j in range(len(CentralSouth_stores)):
        if store1 == CentralSouth_stores[j]:
            demand_weekday += CentralSouth_WeekdayDemands[j]
            demand_weekend += CentralSouth_WeekendDemands[j]
            time_weekday += CentralSouth_WeekdayDemands[j] * 450
            time_weekend += CentralSouth_WeekendDemands[j] * 450

    for k in range(len(CentralSouth_stores)):
        if store2 == CentralSouth_stores[k]:
            demand_weekday += CentralSouth_WeekdayDemands[k]
            demand_weekend += CentralSouth_WeekendDemands[k]
            time_weekday += CentralSouth_WeekdayDemands[k] * 450
            time_weekend += CentralSouth_WeekendDemands[k] * 450

    for l in range(len(CentralSouth_stores)):
        if store3 == CentralSouth_stores[l]:
            demand_weekday += CentralSouth_WeekdayDemands[l]
            demand_weekend += CentralSouth_WeekendDemands[l]
            time_weekday += CentralSouth_WeekdayDemands[l] * 450
            time_weekend += CentralSouth_WeekendDemands[l] * 450

    for m in range(len(CentralSouth_stores)):
        if store4 == CentralSouth_stores[m]:
            demand_weekday += CentralSouth_WeekdayDemands[m]
            demand_weekend += CentralSouth_WeekendDemands[m]
            time_weekday += CentralSouth_WeekdayDemands[m] * 450
            time_weekend += CentralSouth_WeekendDemands[m] * 450

    for store in range(len(stores)):
        if store1 == stores[store]:
            time_weekday += distribution_time[store]
            time_weekend += distribution_time[store]
        if store4 == stores[store]:
            time_weekday += distribution_time[store]
            time_weekend += distribution_time[store]

    for store_row in range(len(stores)):
        if store1 == stores[store_row]:
            for store_col in range(len(stores)):
                if store2 == stores[store_col]:
                    time_weekday += travel_durations[store_row][store_col]
                    time_weekend += travel_durations[store_row][store_col]

    for store_row in range(len(stores)):
        if store2 == stores[store_row]:
            for store_col in range(len(stores)):
                if store3 == stores[store_col]:
                    time_weekday += travel_durations[store_row][store_col]
                    time_weekend += travel_durations[store_row][store_col]

    for store_row in range(len(stores)):
        if store3 == stores[store_row]:
            for store_col in range(len(stores)):
                if store4 == stores[store_col]:
                    time_weekday += travel_durations[store_row][store_col]
                    time_weekend += travel_durations[store_row][store_col]

    if (demand_weekday < demand_threshold and time_weekday < time_threshold):
        CentralSouthRoutes_Weekday.append(CentralSouth_Routes4[i])
        Routes_Weekday.append(CentralSouth_Routes4[i])
        Time_Weekday.append(time_weekday/60/60)

    if (demand_weekend < demand_threshold and time_weekend < time_threshold):
        CentralSouthRoutes_Weekend.append(CentralSouth_Routes4[i])
        Routes_Weekend.append(CentralSouth_Routes4[i])
        Time_Weekend.append(time_weekend/60/60)

for i in range(len(CentralSouth_Routes5)):
    store1 = CentralSouth_Routes5[i][0]
    store2 = CentralSouth_Routes5[i][1]
    store3 = CentralSouth_Routes5[i][2]
    store4 = CentralSouth_Routes5[i][3]
    store5 = CentralSouth_Routes5[i][4]

    demand_weekday = 0
    demand_weekend = 0
    time_weekday = 0
    time_weekend = 0

    for j in range(len(CentralSouth_stores)):
        if store1 == CentralSouth_stores[j]:
            demand_weekday += CentralSouth_WeekdayDemands[j]
            demand_weekend += CentralSouth_WeekendDemands[j]
            time_weekday += CentralSouth_WeekdayDemands[j] * 450
            time_weekend += CentralSouth_WeekendDemands[j] * 450

    for k in range(len(CentralSouth_stores)):
        if store2 == CentralSouth_stores[k]:
            demand_weekday += CentralSouth_WeekdayDemands[k]
            demand_weekend += CentralSouth_WeekendDemands[k]
            time_weekday += CentralSouth_WeekdayDemands[k] * 450
            time_weekend += CentralSouth_WeekendDemands[k] * 450

    for l in range(len(CentralSouth_stores)):
        if store3 == CentralSouth_stores[l]:
            demand_weekday += CentralSouth_WeekdayDemands[l]
            demand_weekend += CentralSouth_WeekendDemands[l]
            time_weekday += CentralSouth_WeekdayDemands[l] * 450
            time_weekend += CentralSouth_WeekendDemands[l] * 450

    for m in range(len(CentralSouth_stores)):
        if store4 == CentralSouth_stores[m]:
            demand_weekday += CentralSouth_WeekdayDemands[m]
            demand_weekend += CentralSouth_WeekendDemands[m]
            time_weekday += CentralSouth_WeekdayDemands[m] * 450
            time_weekend += CentralSouth_WeekendDemands[m] * 450

    for n in range(len(CentralSouth_stores)):
        if store4 == CentralSouth_stores[n]:
            demand_weekday += CentralSouth_WeekdayDemands[n]
            demand_weekend += CentralSouth_WeekendDemands[n]
            time_weekday += CentralSouth_WeekdayDemands[n] * 450
            time_weekend += CentralSouth_WeekendDemands[n] * 450

    for store in range(len(stores)):
        if store1 == stores[store]:
            time_weekday += distribution_time[store]
            time_weekend += distribution_time[store]
        if store5 == stores[store]:
            time_weekday += distribution_time[store]
            time_weekend += distribution_time[store]

    for store_row in range(len(stores)):
        if store1 == stores[store_row]:
            for store_col in range(len(stores)):
                if store2 == stores[store_col]:
                    time_weekday += travel_durations[store_row][store_col]
                    time_weekend += travel_durations[store_row][store_col]

    for store_row in range(len(stores)):
        if store2 == stores[store_row]:
            for store_col in range(len(stores)):
                if store3 == stores[store_col]:
                    time_weekday += travel_durations[store_row][store_col]
                    time_weekend += travel_durations[store_row][store_col]

    for store_row in range(len(stores)):
        if store3 == stores[store_row]:
            for store_col in range(len(stores)):
                if store4 == stores[store_col]:
                    time_weekday += travel_durations[store_row][store_col]
                    time_weekend += travel_durations[store_row][store_col]

    for store_row in range(len(stores)):
        if store4 == stores[store_row]:
            for store_col in range(len(stores)):
                if store5 == stores[store_col]:
                    time_weekday += travel_durations[store_row][store_col]
                    time_weekend += travel_durations[store_row][store_col]

    if (demand_weekday < demand_threshold and time_weekday < time_threshold):
        CentralSouthRoutes_Weekday.append(CentralSouth_Routes5[i])
        Routes_Weekday.append(CentralSouth_Routes5[i])
        Time_Weekday.append(time_weekday/60/60)

    if (demand_weekend < demand_threshold and time_weekend < time_threshold):
        CentralSouthRoutes_Weekend.append(CentralSouth_Routes5[i])
        Routes_Weekend.append(CentralSouth_Routes5[i])
        Time_Weekend.append(time_weekend/60/60)

North_Routes2 = (list(combinations(North_stores, 2)))
North_Routes3 = (list(combinations(North_stores, 3)))
North_Routes4 = (list(combinations(North_stores, 4)))
North_Routes5 = (list(combinations(North_stores, 5)))
North_Routes6 = (list(combinations(North_stores, 6)))

for i in range(len(North_Routes2)):
    store1 = North_Routes2[i][0]
    store2 = North_Routes2[i][1]
    demand_weekday = 0
    demand_weekend = 0
    time_weekday = 0
    time_weekend = 0

    for j in range(len(North_stores)):
        if store1 == North_stores[j]:
            demand_weekday += North_WeekdayDemands[j]
            demand_weekend += North_WeekendDemands[j]
            time_weekday += North_WeekdayDemands[j] * 450
            time_weekend += North_WeekendDemands[j] * 450

    for k in range(len(North_stores)):
        if store2 == North_stores[k]:
            demand_weekday += North_WeekdayDemands[k]
            demand_weekend += North_WeekendDemands[k]
            time_weekday += North_WeekdayDemands[k] * 450
            time_weekend += North_WeekendDemands[k] * 450

    for store in range(len(stores)):
        if store1 == stores[store]:
            time_weekday += distribution_time[store]
            time_weekend += distribution_time[store]
        if store2 == stores[store]:
            time_weekday += distribution_time[store]
            time_weekend += distribution_time[store]

    for store_row in range(len(stores)):
        if store1 == stores[store_row]:
            for store_col in range(len(stores)):
                if store2 == stores[store_col]:
                    time_weekday += travel_durations[store_row][store_col]
                    time_weekend += travel_durations[store_row][store_col]

    if (demand_weekday < demand_threshold and time_weekday < time_threshold):
        NorthRoutes_Weekday.append(North_Routes2[i])
        Routes_Weekday.append(North_Routes2[i])
        Time_Weekday.append(time_weekday/60/60)

    if (demand_weekend < demand_threshold and time_weekend < time_threshold):
        NorthRoutes_Weekend.append(North_Routes2[i])
        Routes_Weekend.append(North_Routes2[i])
        Time_Weekend.append(time_weekend/60/60)

for i in range(len(North_Routes3)):
    store1 = North_Routes3[i][0]
    store2 = North_Routes3[i][1]
    store3 = North_Routes3[i][2]
    demand_weekday = 0
    demand_weekend = 0
    time_weekday = 0
    time_weekend = 0

    for j in range(len(North_stores)):
        if store1 == North_stores[j]:
            demand_weekday += North_WeekdayDemands[j]
            demand_weekend += North_WeekendDemands[j]
            time_weekday += North_WeekdayDemands[j] * 450
            time_weekend += North_WeekendDemands[j] * 450

    for k in range(len(North_stores)):
        if store2 == North_stores[k]:
            demand_weekday += North_WeekdayDemands[k]
            demand_weekend += North_WeekendDemands[k]
            time_weekday += North_WeekdayDemands[k] * 450
            time_weekend += North_WeekendDemands[k] * 450

    for l in range(len(North_stores)):
        if store3 == North_stores[l]:
            demand_weekday += North_WeekdayDemands[l]
            demand_weekend += North_WeekendDemands[l]
            time_weekday += North_WeekdayDemands[l] * 450
            time_weekend += North_WeekendDemands[l] * 450

    for store in range(len(stores)):
        if store1 == stores[store]:
            time_weekday += distribution_time[store]
            time_weekend += distribution_time[store]
        if store3 == stores[store]:
            time_weekday += distribution_time[store]
            time_weekend += distribution_time[store]

    for store_row in range(len(stores)):
        if store1 == stores[store_row]:
            for store_col in range(len(stores)):
                if store2 == stores[store_col]:
                    time_weekday += travel_durations[store_row][store_col]
                    time_weekend += travel_durations[store_row][store_col]

    for store_row in range(len(stores)):
        if store2 == stores[store_row]:
            for store_col in range(len(stores)):
                if store3 == stores[store_col]:
                    time_weekday += travel_durations[store_row][store_col]
                    time_weekend += travel_durations[store_row][store_col]

    if (demand_weekday < demand_threshold and time_weekday < time_threshold):
        NorthRoutes_Weekday.append(North_Routes3[i])
        Routes_Weekday.append(North_Routes3[i])
        Time_Weekday.append(time_weekday/60/60)

    if (demand_weekend < demand_threshold and time_weekend < time_threshold):
        NorthRoutes_Weekend.append(North_Routes3[i])
        Routes_Weekend.append(North_Routes3[i])
        Time_Weekend.append(time_weekend/60/60)

for i in range(len(North_Routes4)):
    store1 = North_Routes4[i][0]
    store2 = North_Routes4[i][1]
    store3 = North_Routes4[i][2]
    store4 = North_Routes4[i][3]
    demand_weekday = 0
    demand_weekend = 0
    time_weekday = 0
    time_weekend = 0

    for j in range(len(North_stores)):
        if store1 == North_stores[j]:
            demand_weekday += North_WeekdayDemands[j]
            demand_weekend += North_WeekendDemands[j]
            time_weekday += North_WeekdayDemands[j] * 450
            time_weekend += North_WeekendDemands[j] * 450

    for k in range(len(North_stores)):
        if store2 == North_stores[k]:
            demand_weekday += North_WeekdayDemands[k]
            demand_weekend += North_WeekendDemands[k]
            time_weekday += North_WeekdayDemands[k] * 450
            time_weekend += North_WeekendDemands[k] * 450

    for l in range(len(North_stores)):
        if store3 == North_stores[l]:
            demand_weekday += North_WeekdayDemands[l]
            demand_weekend += North_WeekendDemands[l]
            time_weekday += North_WeekdayDemands[l] * 450
            time_weekend += North_WeekendDemands[l] * 450

    for m in range(len(North_stores)):
        if store4 == North_stores[m]:
            demand_weekday += North_WeekdayDemands[m]
            demand_weekend += North_WeekendDemands[m]
            time_weekday += North_WeekdayDemands[m] * 450
            time_weekend += North_WeekendDemands[m] * 450

    for store in range(len(stores)):
        if store1 == stores[store]:
            time_weekday += distribution_time[store]
            time_weekend += distribution_time[store]
        if store4 == stores[store]:
            time_weekday += distribution_time[store]
            time_weekend += distribution_time[store]

    for store_row in range(len(stores)):
        if store1 == stores[store_row]:
            for store_col in range(len(stores)):
                if store2 == stores[store_col]:
                    time_weekday += travel_durations[store_row][store_col]
                    time_weekend += travel_durations[store_row][store_col]

    for store_row in range(len(stores)):
        if store2 == stores[store_row]:
            for store_col in range(len(stores)):
                if store3 == stores[store_col]:
                    time_weekday += travel_durations[store_row][store_col]
                    time_weekend += travel_durations[store_row][store_col]

    for store_row in range(len(stores)):
        if store3 == stores[store_row]:
            for store_col in range(len(stores)):
                if store4 == stores[store_col]:
                    time_weekday += travel_durations[store_row][store_col]
                    time_weekend += travel_durations[store_row][store_col]

    if (demand_weekday < demand_threshold and time_weekday < time_threshold):
        NorthRoutes_Weekday.append(North_Routes4[i])
        Routes_Weekday.append(North_Routes4[i])
        Time_Weekday.append(time_weekday/60/60)

    if (demand_weekend < demand_threshold and time_weekend < time_threshold):
        NorthRoutes_Weekend.append(North_Routes4[i])
        Routes_Weekend.append(North_Routes4[i])
        Time_Weekend.append(time_weekend/60/60)

for i in range(len(North_Routes5)):
    store1 = North_Routes5[i][0]
    store2 = North_Routes5[i][1]
    store3 = North_Routes5[i][2]
    store4 = North_Routes5[i][3]
    store5 = North_Routes5[i][4]

    demand_weekday = 0
    demand_weekend = 0
    time_weekday = 0
    time_weekend = 0

    for j in range(len(North_stores)):
        if store1 == North_stores[j]:
            demand_weekday += North_WeekdayDemands[j]
            demand_weekend += North_WeekendDemands[j]
            time_weekday += North_WeekdayDemands[j] * 450
            time_weekend += North_WeekendDemands[j] * 450

    for k in range(len(North_stores)):
        if store2 == North_stores[k]:
            demand_weekday += North_WeekdayDemands[k]
            demand_weekend += North_WeekendDemands[k]
            time_weekday += North_WeekdayDemands[k] * 450
            time_weekend += North_WeekendDemands[k] * 450

    for l in range(len(North_stores)):
        if store3 == North_stores[l]:
            demand_weekday += North_WeekdayDemands[l]
            demand_weekend += North_WeekendDemands[l]
            time_weekday += North_WeekdayDemands[l] * 450
            time_weekend += North_WeekendDemands[l] * 450

    for m in range(len(North_stores)):
        if store4 == North_stores[m]:
            demand_weekday += North_WeekdayDemands[m]
            demand_weekend += North_WeekendDemands[m]
            time_weekday += North_WeekdayDemands[m] * 450
            time_weekend += North_WeekendDemands[m] * 450

    for n in range(len(North_stores)):
        if store4 == North_stores[n]:
            demand_weekday += North_WeekdayDemands[n]
            demand_weekend += North_WeekendDemands[n]
            time_weekday += North_WeekdayDemands[n] * 450
            time_weekend += North_WeekendDemands[n] * 450
            
    for store in range(len(stores)):
        if store1 == stores[store]:
            time_weekday += distribution_time[store]
            time_weekend += distribution_time[store]
        if store5 == stores[store]:
            time_weekday += distribution_time[store]
            time_weekend += distribution_time[store]

    for store_row in range(len(stores)):
        if store1 == stores[store_row]:
            for store_col in range(len(stores)):
                if store2 == stores[store_col]:
                    time_weekday += travel_durations[store_row][store_col]
                    time_weekend += travel_durations[store_row][store_col]

    for store_row in range(len(stores)):
        if store2 == stores[store_row]:
            for store_col in range(len(stores)):
                if store3 == stores[store_col]:
                    time_weekday += travel_durations[store_row][store_col]
                    time_weekend += travel_durations[store_row][store_col]

    for store_row in range(len(stores)):
        if store3 == stores[store_row]:
            for store_col in range(len(stores)):
                if store4 == stores[store_col]:
                    time_weekday += travel_durations[store_row][store_col]
                    time_weekend += travel_durations[store_row][store_col]

    for store_row in range(len(stores)):
        if store4 == stores[store_row]:
            for store_col in range(len(stores)):
                if store5 == stores[store_col]:
                    time_weekday += travel_durations[store_row][store_col]
                    time_weekend += travel_durations[store_row][store_col]

    if (demand_weekday < demand_threshold and time_weekday < time_threshold):
        NorthRoutes_Weekday.append(North_Routes5[i])
        Routes_Weekday.append(North_Routes5[i])
        Time_Weekday.append(time_weekday/60/60)

    if (demand_weekend < demand_threshold and time_weekend < time_threshold):
        NorthRoutes_Weekend.append(North_Routes5[i])
        Routes_Weekend.append(North_Routes5[i])
        Time_Weekend.append(time_weekend/60/60)

South_Routes2 = (list(combinations(South_stores, 2)))
South_Routes3 = (list(combinations(South_stores, 3)))
South_Routes4 = (list(combinations(South_stores, 4)))
South_Routes5 = (list(combinations(South_stores, 5)))

for i in range(len(South_Routes2)):
    store1 = South_Routes2[i][0]
    store2 = South_Routes2[i][1]
    demand_weekday = 0
    demand_weekend = 0
    time = 0

    for j in range(len(South_stores)):
        if store1 == South_stores[j]:
            demand_weekday += South_WeekdayDemands[j]
            demand_weekend += South_WeekendDemands[j]
            time += CentralNorth_WeekdayDemands[j] * 450

    for k in range(len(South_stores)):
        if store2 == South_stores[k]:
            demand_weekday += South_WeekdayDemands[k]
            demand_weekend += South_WeekendDemands[k]
            time += CentralNorth_WeekdayDemands[k] * 450

    for store in range(len(stores)):
        if store1 == stores[store]:
            time += distribution_time[store]
        if store2 == stores[store]:
            time += distribution_time[store]
    
    for store_row in range(len(stores)):
        if store1 == stores[store_row]:
            for store_col in range(len(stores)):
                if store2 == stores[store_col]:
                    time += travel_durations[store_row][store_col]

    if (demand_weekday < demand_threshold and time < time_threshold):
        SouthRoutes_Weekday.append(South_Routes2[i])
        Routes_Weekday.append(South_Routes2[i])
        Time_Weekday.append(time/60/60)
        Cost_Weekday.append(time / 60 / 60 * 225)

    if (demand_weekend < demand_threshold and time < time_threshold):
        SouthRoutes_Weekend.append(South_Routes2[i])
        Routes_Weekend.append(South_Routes2[i])
        Time_Weekend.append(time/60/60)
        Cost_Weekend.append(time / 60 / 60 * 225)

for i in range(len(South_Routes3)):
    store1 = South_Routes3[i][0]
    store2 = South_Routes3[i][1]
    store3 = South_Routes3[i][2]
    demand_weekday = 0
    demand_weekend = 0
    time = 0

    for j in range(len(South_stores)):
        if store1 == South_stores[j]:
            demand_weekday += South_WeekdayDemands[j]
            demand_weekend += South_WeekendDemands[j]
            time += CentralNorth_WeekdayDemands[j] * 450

    for k in range(len(South_stores)):
        if store2 == South_stores[k]:
            demand_weekday += South_WeekdayDemands[k]
            demand_weekend += South_WeekendDemands[k]
            time += CentralNorth_WeekdayDemands[k] * 450

    for l in range(len(South_stores)):
        if store3 == South_stores[l]:
            demand_weekday += South_WeekdayDemands[l]
            demand_weekend += South_WeekendDemands[l]
            time += CentralNorth_WeekdayDemands[l] * 450

    for store in range(len(stores)):
        if store1 == stores[store]:
            time += distribution_time[store]
        if store3 == stores[store]:
            time += distribution_time[store]
    
    for store_row in range(len(stores)):
        if store1 == stores[store_row]:
            for store_col in range(len(stores)):
                if store2 == stores[store_col]:
                    time += travel_durations[store_row][store_col]

    for store_row in range(len(stores)):
        if store2 == stores[store_row]:
            for store_col in range(len(stores)):
                if store3 == stores[store_col]:
                    time += travel_durations[store_row][store_col]

    if (demand_weekday < demand_threshold and time < time_threshold):
        SouthRoutes_Weekday.append(South_Routes3[i])
        Routes_Weekday.append(South_Routes3[i])
        Time_Weekday.append(time/60/60)
        Cost_Weekday.append(time / 60 / 60 * 225)

    if (demand_weekend < demand_threshold and time < time_threshold):
        SouthRoutes_Weekend.append(South_Routes3[i])
        Routes_Weekend.append(South_Routes3[i])
        Time_Weekend.append(time/60/60)
        Cost_Weekend.append(time / 60 / 60 * 225)

for i in range(len(South_Routes4)):
    store1 = South_Routes4[i][0]
    store2 = South_Routes4[i][1]
    store3 = South_Routes4[i][2]
    store4 = South_Routes4[i][3]
    demand_weekday = 0
    demand_weekend = 0
    time = 0

    for j in range(len(South_stores)):
        if store1 == South_stores[j]:
            demand_weekday += South_WeekdayDemands[j]
            demand_weekend += South_WeekendDemands[j]
            time += CentralNorth_WeekdayDemands[j] * 450

    for k in range(len(South_stores)):
        if store2 == South_stores[k]:
            demand_weekday += South_WeekdayDemands[k]
            demand_weekend += South_WeekendDemands[k]
            time += CentralNorth_WeekdayDemands[k] * 450

    for l in range(len(South_stores)):
        if store3 == South_stores[l]:
            demand_weekday += South_WeekdayDemands[l]
            demand_weekend += South_WeekendDemands[l]
            time += CentralNorth_WeekdayDemands[l] * 450

    for m in range(len(South_stores)):
        if store4 == South_stores[m]:
            demand_weekday += South_WeekdayDemands[m]
            demand_weekend += South_WeekendDemands[m]
            time += CentralNorth_WeekdayDemands[m] * 450

    for store in range(len(stores)):
        if store1 == stores[store]:
            time += distribution_time[store]
        if store4 == stores[store]:
            time += distribution_time[store]
    
    for store_row in range(len(stores)):
        if store1 == stores[store_row]:
            for store_col in range(len(stores)):
                if store2 == stores[store_col]:
                    time += travel_durations[store_row][store_col]

    for store_row in range(len(stores)):
        if store2 == stores[store_row]:
            for store_col in range(len(stores)):
                if store3 == stores[store_col]:
                    time += travel_durations[store_row][store_col]

    for store_row in range(len(stores)):
        if store3 == stores[store_row]:
            for store_col in range(len(stores)):
                if store4 == stores[store_col]:
                    time += travel_durations[store_row][store_col]

    if (demand_weekday < demand_threshold and time < time_threshold):
        SouthRoutes_Weekday.append(South_Routes4[i])
        Routes_Weekday.append(South_Routes4[i])
        Time_Weekday.append(time/60/60)
        Cost_Weekday.append(time / 60 / 60 * 225)

    if (demand_weekend < demand_threshold and time < time_threshold):
        SouthRoutes_Weekend.append(South_Routes4[i])
        Routes_Weekend.append(South_Routes4[i])
        Time_Weekend.append(time/60/60)
        Cost_Weekend.append(time / 60 / 60 * 225)

for i in range(len(South_Routes5)):
    store1 = South_Routes5[i][0]
    store2 = South_Routes5[i][1]
    store3 = South_Routes5[i][2]
    store4 = South_Routes5[i][3]
    store5 = South_Routes5[i][4]

    demand_weekday = 0
    demand_weekend = 0
    time =0

    for j in range(len(South_stores)):
        if store1 == South_stores[j]:
            demand_weekday += South_WeekdayDemands[j]
            demand_weekend += South_WeekendDemands[j]
            time += CentralNorth_WeekdayDemands[j] * 450

    for k in range(len(South_stores)):
        if store2 == South_stores[k]:
            demand_weekday += South_WeekdayDemands[k]
            demand_weekend += South_WeekendDemands[k]
            time += CentralNorth_WeekdayDemands[k] * 450

    for l in range(len(South_stores)):
        if store3 == South_stores[l]:
            demand_weekday += South_WeekdayDemands[l]
            demand_weekend += South_WeekendDemands[l]
            time += CentralNorth_WeekdayDemands[l] * 450

    for m in range(len(South_stores)):
        if store4 == South_stores[m]:
            demand_weekday += South_WeekdayDemands[m]
            demand_weekend += South_WeekendDemands[m]
            time += CentralNorth_WeekdayDemands[m] * 450

    for n in range(len(South_stores)):
        if store4 == South_stores[n]:
            demand_weekday += South_WeekdayDemands[n]
            demand_weekend += South_WeekendDemands[n]
            time += CentralNorth_WeekdayDemands[n] * 450

    for store in range(len(stores)):
        if store1 == stores[store]:
            time += distribution_time[store]
        if store5 == stores[store]:
            time += distribution_time[store]
    
    for store_row in range(len(stores)):
        if store1 == stores[store_row]:
            for store_col in range(len(stores)):
                if store2 == stores[store_col]:
                    time += travel_durations[store_row][store_col]

    for store_row in range(len(stores)):
        if store2 == stores[store_row]:
            for store_col in range(len(stores)):
                if store3 == stores[store_col]:
                    time += travel_durations[store_row][store_col]

    for store_row in range(len(stores)):
        if store3 == stores[store_row]:
            for store_col in range(len(stores)):
                if store4 == stores[store_col]:
                    time += travel_durations[store_row][store_col]

    for store_row in range(len(stores)):
        if store4 == stores[store_row]:
            for store_col in range(len(stores)):
                if store5 == stores[store_col]:
                    time += travel_durations[store_row][store_col]

    if (demand_weekday < demand_threshold and time < time_threshold):
        SouthRoutes_Weekday.append(South_Routes5[i])
        Routes_Weekday.append(South_Routes5[i])
        Time_Weekday.append(time/60/60)
        Cost_Weekday.append(time / 60 / 60 * 225)

    if (demand_weekend < demand_threshold and time < time_threshold):
        SouthRoutes_Weekend.append(South_Routes5[i])
        Routes_Weekend.append(South_Routes5[i])
        Time_Weekend.append(time/60/60)
        Cost_Weekend.append(time / 60 / 60 * 225)

West_Routes2 = (list(combinations(West_stores, 2)))
West_Routes3 = (list(combinations(West_stores, 3)))
West_Routes4 = (list(combinations(West_stores, 4)))
West_Routes5 = (list(combinations(West_stores, 5)))

for i in range(len(West_Routes2)):
    store1 = West_Routes2[i][0]
    store2 = West_Routes2[i][1]
    demand_weekday = 0
    demand_weekend = 0
    time = 0

    for j in range(len(West_stores)):
        if store1 == West_stores[j]:
            demand_weekday += West_WeekdayDemands[j]
            demand_weekend += West_WeekendDemands[j]
            time += CentralNorth_WeekdayDemands[j] * 450

    for k in range(len(West_stores)):
        if store2 == West_stores[k]:
            demand_weekday += West_WeekdayDemands[k]
            demand_weekend += West_WeekendDemands[k]
            time += CentralNorth_WeekdayDemands[k] * 450

    for store in range(len(stores)):
        if store1 == stores[store]:
            time += distribution_time[store]
        if store2 == stores[store]:
            time += distribution_time[store]
    
    for store_row in range(len(stores)):
        if store1 == stores[store_row]:
            for store_col in range(len(stores)):
                if store2 == stores[store_col]:
                    time += travel_durations[store_row][store_col]

    if (demand_weekday < demand_threshold and time < time_threshold):
        WestRoutes_Weekday.append(West_Routes2[i])
        Routes_Weekday.append(West_Routes2[i])
        Time_Weekday.append(time/60/60)
        Cost_Weekday.append(time / 60 / 60 * 225)

    if (demand_weekend < demand_threshold and time < time_threshold):
        WestRoutes_Weekday.append(West_Routes2[i])
        Routes_Weekend.append(West_Routes2[i])
        Time_Weekend.append(time/60/60)
        Cost_Weekend.append(time / 60 / 60 * 225)

for i in range(len(West_Routes3)):
    store1 = West_Routes3[i][0]
    store2 = West_Routes3[i][1]
    store3 = West_Routes3[i][2]
    demand_weekday = 0
    demand_weekend = 0
    time = 0

    for j in range(len(West_stores)):
        if store1 == West_stores[j]:
            demand_weekday += West_WeekdayDemands[j]
            demand_weekend += West_WeekendDemands[j]
            time += CentralNorth_WeekdayDemands[j] * 450

    for k in range(len(West_stores)):
        if store2 == West_stores[k]:
            demand_weekday += West_WeekdayDemands[k]
            demand_weekend += West_WeekendDemands[k]
            time += CentralNorth_WeekdayDemands[k] * 450

    for l in range(len(West_stores)):
        if store3 == West_stores[l]:
            demand_weekday += West_WeekdayDemands[l]
            demand_weekend += West_WeekendDemands[l]
            time += CentralNorth_WeekdayDemands[l] * 450

    for store in range(len(stores)):
        if store1 == stores[store]:
            time += distribution_time[store]
        if store3 == stores[store]:
            time += distribution_time[store]
    
    for store_row in range(len(stores)):
        if store1 == stores[store_row]:
            for store_col in range(len(stores)):
                if store2 == stores[store_col]:
                    time += travel_durations[store_row][store_col]

    for store_row in range(len(stores)):
        if store2 == stores[store_row]:
            for store_col in range(len(stores)):
                if store3 == stores[store_col]:
                    time += travel_durations[store_row][store_col]

    if (demand_weekday < demand_threshold and time < time_threshold):
        WestRoutes_Weekday.append(West_Routes3[i])
        Routes_Weekday.append(West_Routes3[i])
        Time_Weekday.append(time/60/60)
        Cost_Weekday.append(time / 60 / 60 * 225)

    if (demand_weekend < demand_threshold and time < time_threshold):
        WestRoutes_Weekend.append(West_Routes3[i])
        Routes_Weekend.append(West_Routes3[i])
        Time_Weekend.append(time/60/60)
        Cost_Weekend.append(time / 60 / 60 * 225)

for i in range(len(West_Routes4)):
    store1 = West_Routes4[i][0]
    store2 = West_Routes4[i][1]
    store3 = West_Routes4[i][2]
    store4 = West_Routes4[i][3]
    demand_weekday = 0
    demand_weekend = 0
    time = 0

    for j in range(len(West_stores)):
        if store1 == West_stores[j]:
            demand_weekday += West_WeekdayDemands[j]
            demand_weekend += West_WeekendDemands[j]
            time += CentralNorth_WeekdayDemands[j] * 450

    for k in range(len(West_stores)):
        if store2 == West_stores[k]:
            demand_weekday += West_WeekdayDemands[k]
            demand_weekend += West_WeekendDemands[k]
            time += CentralNorth_WeekdayDemands[k] * 450

    for l in range(len(West_stores)):
        if store3 == West_stores[l]:
            demand_weekday += West_WeekdayDemands[l]
            demand_weekend += West_WeekendDemands[l]
            time += CentralNorth_WeekdayDemands[l] * 450

    for m in range(len(West_stores)):
        if store4 == West_stores[m]:
            demand_weekday += West_WeekdayDemands[m]
            demand_weekend += West_WeekendDemands[m]
            time += CentralNorth_WeekdayDemands[m] * 450

    for store in range(len(stores)):
        if store1 == stores[store]:
            time += distribution_time[store]
        if store4 == stores[store]:
            time += distribution_time[store]
    
    for store_row in range(len(stores)):
        if store1 == stores[store_row]:
            for store_col in range(len(stores)):
                if store2 == stores[store_col]:
                    time += travel_durations[store_row][store_col]

    for store_row in range(len(stores)):
        if store2 == stores[store_row]:
            for store_col in range(len(stores)):
                if store3 == stores[store_col]:
                    time += travel_durations[store_row][store_col]

    for store_row in range(len(stores)):
        if store3 == stores[store_row]:
            for store_col in range(len(stores)):
                if store4 == stores[store_col]:
                    time += travel_durations[store_row][store_col]

    if (demand_weekday < demand_threshold and time < time_threshold):
        WestRoutes_Weekday.append(West_Routes4[i])
        Routes_Weekday.append(West_Routes4[i])
        Time_Weekday.append(time/60/60)
        Cost_Weekday.append(time / 60 / 60 * 225)

    if (demand_weekend < demand_threshold and time < time_threshold):
        WestRoutes_Weekend.append(West_Routes4[i])
        Routes_Weekend.append(West_Routes4[i])
        Time_Weekend.append(time/60/60)
        Cost_Weekend.append(time / 60 / 60 * 225)

for i in range(len(West_Routes5)):
    store1 = West_Routes5[i][0]
    store2 = West_Routes5[i][1]
    store3 = West_Routes5[i][2]
    store4 = West_Routes5[i][3]
    store5 = West_Routes5[i][4]

    demand_weekday = 0
    demand_weekend = 0
    time = 0

    for j in range(len(West_stores)):
        if store1 == West_stores[j]:
            demand_weekday += West_WeekdayDemands[j]
            demand_weekend += West_WeekendDemands[j]
            time += CentralNorth_WeekdayDemands[j] * 450

    for k in range(len(West_stores)):
        if store2 == West_stores[k]:
            demand_weekday += West_WeekdayDemands[k]
            demand_weekend += West_WeekendDemands[k]
            time += CentralNorth_WeekdayDemands[k] * 450

    for l in range(len(West_stores)):
        if store3 == West_stores[l]:
            demand_weekday += West_WeekdayDemands[l]
            demand_weekend += West_WeekendDemands[l]
            time += CentralNorth_WeekdayDemands[l] * 450

    for m in range(len(West_stores)):
        if store4 == West_stores[m]:
            demand_weekday += West_WeekdayDemands[m]
            demand_weekend += West_WeekendDemands[m]
            time += CentralNorth_WeekdayDemands[m] * 450

    for n in range(len(West_stores)):
        if store4 == West_stores[n]:
            demand_weekday += West_WeekdayDemands[n]
            demand_weekend += West_WeekendDemands[n]
            time += CentralNorth_WeekdayDemands[n] * 450

    for store in range(len(stores)):
        if store1 == stores[store]:
            time += distribution_time[store]
        if store5 == stores[store]:
            time += distribution_time[store]
    
    for store_row in range(len(stores)):
        if store1 == stores[store_row]:
            for store_col in range(len(stores)):
                if store2 == stores[store_col]:
                    time += travel_durations[store_row][store_col]

    for store_row in range(len(stores)):
        if store2 == stores[store_row]:
            for store_col in range(len(stores)):
                if store3 == stores[store_col]:
                    time += travel_durations[store_row][store_col]

    for store_row in range(len(stores)):
        if store3 == stores[store_row]:
            for store_col in range(len(stores)):
                if store4 == stores[store_col]:
                    time += travel_durations[store_row][store_col]

    for store_row in range(len(stores)):
        if store4 == stores[store_row]:
            for store_col in range(len(stores)):
                if store5 == stores[store_col]:
                    time += travel_durations[store_row][store_col]

    if (demand_weekday < demand_threshold and time < time_threshold):
        WestRoutes_Weekday.append(West_Routes5[i])
        Routes_Weekday.append(West_Routes5[i])
        Time_Weekday.append(time/60/60)
        Cost_Weekday.append(time / 60 / 60 * 225)

    if (demand_weekend < demand_threshold and time < time_threshold):
        WestRoutes_Weekend.append(West_Routes5[i])
        Routes_Weekend.append(West_Routes5[i])
        Time_Weekend.append(time/60/60)
        Cost_Weekend.append(time / 60 / 60 * 225)

East_Routes2 = (list(combinations(East_stores, 2)))
East_Routes3 = (list(combinations(East_stores, 3)))
East_Routes4 = (list(combinations(East_stores, 4)))
East_Routes5 = (list(combinations(East_stores, 5)))

for i in range(len(East_Routes2)):
    store1 = East_Routes2[i][0]
    store2 = East_Routes2[i][1]
    demand_weekday = 0
    demand_weekend = 0
    time = 0

    for j in range(len(East_stores)):
        if store1 == East_stores[j]:
            demand_weekday += East_WeekdayDemands[j]
            demand_weekend += East_WeekendDemands[j]
            time += CentralNorth_WeekdayDemands[j] * 450

    for k in range(len(East_stores)):
        if store2 == East_stores[k]:
            demand_weekday += East_WeekdayDemands[k]
            demand_weekend += East_WeekendDemands[k]
            time += CentralNorth_WeekdayDemands[k] * 450

    for store in range(len(stores)):
        if store1 == stores[store]:
            time += distribution_time[store]
        if store2 == stores[store]:
            time += distribution_time[store]
    
    for store_row in range(len(stores)):
        if store1 == stores[store_row]:
            for store_col in range(len(stores)):
                if store2 == stores[store_col]:
                    time += travel_durations[store_row][store_col]

    if (demand_weekday < demand_threshold and time < time_threshold):
        EastRoutes_Weekday.append(East_Routes2[i])
        Routes_Weekday.append(East_Routes2[i])
        Time_Weekday.append(time/60/60)
        Cost_Weekday.append(time / 60 / 60 * 225)

    if (demand_weekend < demand_threshold and time < time_threshold):
        EastRoutes_Weekday.append(East_Routes2[i])
        Routes_Weekend.append(East_Routes2[i])
        Time_Weekend.append(time/60/60)
        Cost_Weekend.append(time / 60 / 60 * 225)

for i in range(len(East_Routes3)):
    store1 = East_Routes3[i][0]
    store2 = East_Routes3[i][1]
    store3 = East_Routes3[i][2]
    demand_weekday = 0
    demand_weekend = 0
    time = 0

    for j in range(len(East_stores)):
        if store1 == East_stores[j]:
            demand_weekday += East_WeekdayDemands[j]
            demand_weekend += East_WeekendDemands[j]
            time += CentralNorth_WeekdayDemands[j] * 450

    for k in range(len(East_stores)):
        if store2 == East_stores[k]:
            demand_weekday += East_WeekdayDemands[k]
            demand_weekend += East_WeekendDemands[k]
            time += CentralNorth_WeekdayDemands[k] * 450

    for l in range(len(East_stores)):
        if store3 == East_stores[l]:
            demand_weekday += East_WeekdayDemands[l]
            demand_weekend += East_WeekendDemands[l]
            time += CentralNorth_WeekdayDemands[l] * 450

    for store in range(len(stores)):
        if store1 == stores[store]:
            time += distribution_time[store]
        if store3 == stores[store]:
            time += distribution_time[store]
    
    for store_row in range(len(stores)):
        if store1 == stores[store_row]:
            for store_col in range(len(stores)):
                if store2 == stores[store_col]:
                    time += travel_durations[store_row][store_col]

    for store_row in range(len(stores)):
        if store2 == stores[store_row]:
            for store_col in range(len(stores)):
                if store3 == stores[store_col]:
                    time += travel_durations[store_row][store_col]

    if (demand_weekday < demand_threshold and time < time_threshold):
        EastRoutes_Weekday.append(East_Routes3[i])
        Routes_Weekday.append(East_Routes3[i])
        Time_Weekday.append(time/60/60)
        Cost_Weekday.append(time / 60 / 60 * 225)

    if (demand_weekend < demand_threshold and time < time_threshold):
        EastRoutes_Weekend.append(East_Routes3[i])
        Routes_Weekend.append(East_Routes3[i])
        Time_Weekend.append(time/60/60)
        Cost_Weekend.append(time / 60 / 60 * 225)

for i in range(len(East_Routes4)):
    store1 = East_Routes4[i][0]
    store2 = East_Routes4[i][1]
    store3 = East_Routes4[i][2]
    store4 = East_Routes4[i][3]
    demand_weekday = 0
    demand_weekend = 0
    time = 0

    for j in range(len(East_stores)):
        if store1 == East_stores[j]:
            demand_weekday += East_WeekdayDemands[j]
            demand_weekend += East_WeekendDemands[j]
            time += CentralNorth_WeekdayDemands[j] * 450

    for k in range(len(East_stores)):
        if store2 == East_stores[k]:
            demand_weekday += East_WeekdayDemands[k]
            demand_weekend += East_WeekendDemands[k]
            time += CentralNorth_WeekdayDemands[k] * 450

    for l in range(len(East_stores)):
        if store3 == East_stores[l]:
            demand_weekday += East_WeekdayDemands[l]
            demand_weekend += East_WeekendDemands[l]
            time += CentralNorth_WeekdayDemands[l] * 450

    for m in range(len(East_stores)):
        if store4 == East_stores[m]:
            demand_weekday += East_WeekdayDemands[m]
            demand_weekend += East_WeekendDemands[m]
            time += CentralNorth_WeekdayDemands[m] * 450

    for store in range(len(stores)):
        if store1 == stores[store]:
            time += distribution_time[store]
        if store4 == stores[store]:
            time += distribution_time[store]
    
    for store_row in range(len(stores)):
        if store1 == stores[store_row]:
            for store_col in range(len(stores)):
                if store2 == stores[store_col]:
                    time += travel_durations[store_row][store_col]

    for store_row in range(len(stores)):
        if store2 == stores[store_row]:
            for store_col in range(len(stores)):
                if store3 == stores[store_col]:
                    time += travel_durations[store_row][store_col]

    for store_row in range(len(stores)):
        if store3 == stores[store_row]:
            for store_col in range(len(stores)):
                if store4 == stores[store_col]:
                    time += travel_durations[store_row][store_col]

    if (demand_weekday < demand_threshold and time < time_threshold):
        EastRoutes_Weekday.append(East_Routes4[i])
        Routes_Weekday.append(East_Routes4[i])
        Time_Weekday.append(time/60/60)
        Cost_Weekday.append(time / 60 / 60 * 225)

    if (demand_weekend < demand_threshold and time < time_threshold):
        EastRoutes_Weekend.append(East_Routes4[i])
        Routes_Weekend.append(East_Routes4[i])
        Time_Weekend.append(time/60/60)
        Cost_Weekend.append(time / 60 / 60 * 225)

for i in range(len(East_Routes5)):
    store1 = East_Routes5[i][0]
    store2 = East_Routes5[i][1]
    store3 = East_Routes5[i][2]
    store4 = East_Routes5[i][3]
    store5 = East_Routes5[i][4]

    demand_weekday = 0
    demand_weekend = 0
    time = 0

    for j in range(len(East_stores)):
        if store1 == East_stores[j]:
            demand_weekday += East_WeekdayDemands[j]
            demand_weekend += East_WeekendDemands[j]
            time += CentralNorth_WeekdayDemands[j] * 450

    for k in range(len(East_stores)):
        if store2 == East_stores[k]:
            demand_weekday += East_WeekdayDemands[k]
            demand_weekend += East_WeekendDemands[k]
            time += CentralNorth_WeekdayDemands[k] * 450

    for l in range(len(East_stores)):
        if store3 == East_stores[l]:
            demand_weekday += East_WeekdayDemands[l]
            demand_weekend += East_WeekendDemands[l]
            time += CentralNorth_WeekdayDemands[l] * 450

    for m in range(len(East_stores)):
        if store4 == East_stores[m]:
            demand_weekday += East_WeekdayDemands[m]
            demand_weekend += East_WeekendDemands[m]
            time += CentralNorth_WeekdayDemands[m] * 450

    for n in range(len(West_stores)):
        if store4 == West_stores[n]:
            demand_weekday += East_WeekdayDemands[n]
            demand_weekend += East_WeekendDemands[n]
            time += CentralNorth_WeekdayDemands[n] * 450

    for store in range(len(stores)):
        if store1 == stores[store]:
            time += distribution_time[store]
        if store5 == stores[store]:
            time += distribution_time[store]
    
    for store_row in range(len(stores)):
        if store1 == stores[store_row]:
            for store_col in range(len(stores)):
                if store2 == stores[store_col]:
                    time += travel_durations[store_row][store_col]

    for store_row in range(len(stores)):
        if store2 == stores[store_row]:
            for store_col in range(len(stores)):
                if store3 == stores[store_col]:
                    time += travel_durations[store_row][store_col]

    for store_row in range(len(stores)):
        if store3 == stores[store_row]:
            for store_col in range(len(stores)):
                if store4 == stores[store_col]:
                    time += travel_durations[store_row][store_col]

    for store_row in range(len(stores)):
        if store4 == stores[store_row]:
            for store_col in range(len(stores)):
                if store5 == stores[store_col]:
                    time += travel_durations[store_row][store_col]

    if (demand_weekday < demand_threshold and time < time_threshold):
        EastRoutes_Weekday.append(East_Routes5[i])
        Routes_Weekday.append(East_Routes5[i])
        Time_Weekday.append(time/60/60)
        Cost_Weekday.append(time / 3600 * 225)

    if (demand_weekend < demand_threshold and time < time_threshold):
        EastRoutes_Weekend.append(East_Routes5[i])
        Routes_Weekend.append(East_Routes5[i])
        Time_Weekend.append(time/60/60)
        Cost_Weekend.append(time / 60 / 60 * 225)


max_routes = 60

# Listing the possible number of routes
weekday_possible_routes = [i for i in range(0,len(Routes_Weekday))]
weekend_possible_routes = [i for i in range(0,len(Routes_Weekend))]

# Setting up the number of variables needed
WeekdayRoute_vars = LpVariable.dicts("Route", weekday_possible_routes, 0, None, LpBinary)
WeekendRoute_vars = LpVariable.dicts("Route", weekend_possible_routes, 0, None, LpBinary)

# Setting up the minimisation objective function
prob_weekday = LpProblem("Woolworths NZ VRP weekday", LpMinimize)
prob_weekend = LpProblem("Woolworths NZ VRP weekend", LpMinimize)

# Objective function
prob_weekday += lpSum([225 * WeekdayRoute_vars[route] * Time_Weekday[route] if Time_Weekday[route] < 4 else 275 * WeekdayRoute_vars[route] * Time_Weekday[route] for route in weekday_possible_routes])

prob_weekend += lpSum([225 * WeekendRoute_vars[route] * Time_Weekend[route] if Time_Weekend[route] < 4 else 275 * WeekendRoute_vars[route] * Time_Weekend[route] for route in weekend_possible_routes])

# Adding the constraints
prob_weekday += lpSum([WeekdayRoute_vars[route] for route in weekday_possible_routes]) <= max_routes
prob_weekend += lpSum([WeekendRoute_vars[route] for route in weekend_possible_routes]) <= max_routes

for store in stores:
    prob_weekday += lpSum([WeekdayRoute_vars[route] for route in weekday_possible_routes if store in Routes_Weekday[route]]) == 1

    prob_weekend += lpSum([WeekendRoute_vars[route] for route in weekend_possible_routes if store in Routes_Weekend[route]]) == 1

# Writing the LP
prob_weekday.writeLP("" + os.getcwd() + os.sep + "LP_files" + os.sep + "WoolworthsVRP_weekday.lp")
prob_weekend.writeLP("" + os.getcwd() + os.sep + "LP_files" + os.sep + "WoolworthsVRP_weekend.lp")

# Solving the LP
prob_weekday.solve()
prob_weekend.solve()

# Variables printed with the optimal value
for v in prob_weekday.variables():
    print(v.name, "=", v.varValue)
for w in prob_weekend.variables():
    print(w.name, "=", w.varValue)

# Prints status of solution
print("Weekday Status:", LpStatus[prob_weekday.status])
print("Weekend Status:", LpStatus[prob_weekend.status])

# The optimised objective function solution
print("Least cost for the Weekday =", value(prob_weekday.objective))
print("Least cost for the Weekend =", value(prob_weekend.objective))

# Finding the total number of trucks used
num_weekday = 0
for v in prob_weekday.variables():
    if v.varValue == 1:
        num_weekday += 1

print("Number of trucks used in the weekdays: ", num_weekday)

num_weekend = 0
for w in prob_weekend.variables():
    if w.varValue == 1:
        num_weekend += 1

print("Number of trucks used in the weekends: ", num_weekend)

"""
optimalRoutes_weekday = []
num=0
for v in prob_weekday.variables():
    if v.varValue == 1:
        optimalRoutes_weekday.append(v.name)
        num += 1
print("Number of trucks used: ", num)
print(optimalRoutes_weekday)


for v in prob.variables():
    if v.varValue == 1.0:
        print(Routes_Weekday[])


print(Routes_Weekday[117])
print(Routes_Weekday[226])
print(Routes_Weekday[236])
print(Routes_Weekday[258])
print(Routes_Weekday[272])
print(Routes_Weekday[283])
print(Routes_Weekday[326])
print(Routes_Weekday[399])
print(Routes_Weekday[427])
print(Routes_Weekday[428])
print(Routes_Weekday[430])
print(Routes_Weekday[498])
print(Routes_Weekday[51])
print(Routes_Weekday[578])
print(Routes_Weekday[617])
print(Routes_Weekday[627])
print(Routes_Weekday[666])
print(Routes_Weekday[677])
print(Routes_Weekday[678])
print(Routes_Weekday[681])
print(Routes_Weekday[779])
print(Routes_Weekday[794])
print(Routes_Weekday[84])
print(Routes_Weekday[844])
print(Routes_Weekday[880])






# Matrix for Weekday routes
Weekday_routeLength = len(Routes_Weekday)
Weekday_lp = np.zeros((len(stores), Weekday_routeLength))

for i in range(Weekday_routeLength):
    for j in range(len(stores)):
        test2 = stores[j]

        for k in range(len(Routes_Weekday[i])):

            test = Routes_Weekday[i][k]

            if(test == test2):
                Weekday_lp[j][i] = 1

# Matrix for Weekend routes
Weekend_routeLength = len(Routes_Weekend)
Weekend_lp = np.zeros((len(stores), Weekend_routeLength))

for i in range(Weekend_routeLength):
    for j in range(len(stores)):
        test2 = stores[j]

        for k in range(len(Routes_Weekend[i])):

            test = Routes_Weekend[i][k]

            if(test == test2):
                Weekend_lp[j][i] = 1



# Creates array for lp from 1 to the length of the weekday and weekend arrays

Weekday_routeVariable = []
Weekend_routeVariable = []

for i in range(len(Time_Weekday)):
    Weekday_routeVariable.append(i)

for j in range(len(Time_Weekend)):
    Weekend_routeVariable.append(j)

# create problem and variables
Weekday_prob = LpProblem("Weekday", LpMinimize)
Weekday_vars = LpVariable.dicts("Weekday", Weekday_routeVariable, 0, None, 'Integer')

Weekend_prob = LpProblem("Weekend", LpMinimize)
Weekend_vars = LpVariable.dicts("Weekend", Weekend_routeVariable, 0, None, 'Integer')


Weekday_objective = []

for i in range(len(Time_Weekday)):
    if Time_Weekday[i] <= 4200:Weekday_objective = []

for i in range(len(Time_Weekday)):
    if Time_Weekday[i] <= 4200:
        Weekday_objective.append((225 / 3600) * Weekday_vars[i] * (Time_Weekday[i] + 900))
    else:
        Weekday_objective.append((275 / 3600) * Weekday_vars[i] * (Time_Weekday[i] + 900))
    
Weekday_prob += lpSum(Weekday_objective), "Cost"
    ##Weekday_prob += lpSum([(225 / 3600) * Weekday_vars[i] * (Time_Weekday[i] + 900) for i in range(len(Time_Weekday))]), "Cost"

Weekend_prob += lpSum([(225 / 3600) * Weekend_vars[j] * (Time_Weekend[j] + 900) for j in range(len(Time_Weekend))]), "Cost"
        Weekday_objective.append((225 / 3600) * Weekday_vars[i] * (Time_Weekday[i] + 900))
    else:
        Weekday_objective.append((275 / 3600) * Weekday_vars[i] * (Time_Weekday[i] + 900))
    
Weekday_prob += lpSum(Weekday_objective), "Cost"
    ##Weekday_prob += lpSum([(225 / 3600) * Weekday_vars[i] * (Time_Weekday[i] + 900) for i in range(len(Time_Weekday))]), "Cost"

Weekend_prob += lpSum([(225 / 3600) * Weekend_vars[j] * (Time_Weekend[j] + 900) for j in range(len(Time_Weekend))]), "Cost"



# objective constraints
Weekday_prob += lpSum([Cost_Weekday[i] * Weekday_vars[i] * (Time_Weekday[i] + 900) for i in range(len(Time_Weekday))]), "Cost"

Weekend_prob += lpSum([Cost_Weekend[j] * Weekend_vars[j] * (Time_Weekend[j] + 900) for j in range(len(Time_Weekend))]), "Cost"

# route constraints
for i in range(len(stores)):
    Weekday_prob += lpSum([Weekday_vars[j] * Weekday_lp[i][j] for j in range(len(Weekday_routeVariable))]) == 1

for k in range(len(stores)):
    Weekend_prob += lpSum([Weekend_vars[l] * Weekend_lp[k][l] for l in range(len(Weekend_routeVariable))]) == 1



# Solves and prints status of solution
Weekday_prob.solve()
print("Weekday Status:", LpStatus[Weekday_prob.status])

Weekend_prob.solve()
print("Weekend Status:", LpStatus[Weekend_prob.status])

# Variables printed with the optimal value
for v in Weekday_prob.variables():
    print(v.name, "=", v.varValue)

for w in Weekend_prob.variables():
    print(w.name, "=", w.varValue)

# The optimised objective function solution
print("Least cost for the Weekday=", value(Weekday_prob.objective))

print("Least cost for the Weekend=", value(Weekend_prob.objective))

"""