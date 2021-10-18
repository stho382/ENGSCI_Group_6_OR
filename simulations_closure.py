import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from scipy import stats
from maps_closure import *
from weekend_routes_closure import *
from weekday_routes_closure import *
import statistics
import math

# Importing means, variances and demands
weekday_mean_variance_closure = pd.read_csv("https://raw.githubusercontent.com/stho382/ENGSCI_Group_6_OR/sebastian_development/Data/weekday_mean_demand_and_variance_closure.csv", usecols= range(0,3))
weekend_mean_variance_closure = pd.read_csv("https://raw.githubusercontent.com/stho382/ENGSCI_Group_6_OR/sebastian_development/Data/weekend_mean_demand_and_variance_closure.csv", usecols= range(0,3))
travel_durations_df = pd.read_csv('https://raw.githubusercontent.com/stho382/ENGSCI_Group_6_OR/main/Data/WoolworthsTravelDurations_closure.csv')
travel_durations_df.set_index("Unnamed: 0", inplace = True)
travel_durations_df.index.name = 'Store'

np.random.seed(500)
def split_my_array(tuple_of_stores, store_vars):
    """
    This function is used to split routes that have demands greater than 26 during the simulation
    
    Parameters
    ----------
    tuple_of_stores (tuple) - a tuple containg the stores for 1 route
    store_vars (dictionary) - dictionary containing each of the stores and their respective demands

    Returns
    ----------
    good_paths (list) - list of paths that have been split and have demands less than or equal to 26
    good_path_demands (list) - list of demands for the routes in good_paths

    """
    # Creating a temporary array to store the paths to be split
    temp_array = []
    temp_array.append(tuple_of_stores)
    
    # initialising the lists to be returned with the split paths and their respective demands
    good_paths = []
    good_path_demands = []
    number_of_extra_trucks_used = 0
    
    #Finding the total demand in the array
    while len(temp_array) > 0:
        total_demand_in_tuple = 0
        good_stores = ()
        bad_stores = ()
        # loop through every store in the first route within temp_array
        for store in temp_array[0]:
            # if the sum of the current total demand and the current store's demand is less than or equal to 26,
            # add the store's demand to the total demand
            # and add the store to the pair of good stores whose sum of demands is less than or equal to 26
            if total_demand_in_tuple + store_vars.get(store) <= 26:
                total_demand_in_tuple += store_vars.get(store)
                good_stores = good_stores + (store,)

            else:
                # if the sum of the current total demand and the current storsse's demand is greater than 26,
                # append the store to the list of bad stores to be further split
                bad_stores = bad_stores + (store,)
        
        if len(bad_stores) > 0:
            # if the length of the bad stores is none, that means there are no more stores to be split,
            # and the function can stop appending to the list of bad stores
            temp_array.append(bad_stores)
            number_of_extra_trucks_used += 1
        
        good_paths.append(good_stores)
        good_path_demands.append(total_demand_in_tuple)
        
        # remove the first element in the temp array if it has been split as per the demand constraints
        temp_array.pop(0)

    return good_paths, good_path_demands, number_of_extra_trucks_used


def find_my_cost(route_array, store_vars):
    """
    This function is used to find the cost of the route given as input
    
    Parameters
    ----------
    route_array (list) - a list containing the stores for 1 route
    store_vars (dictionary) - dictionary containing each of the stores and their respective demands

    Returns
    ----------
    total cost (double) - cost of the route

    """

    # Accounting for traffic variation using normal distribution
    # https://www.tomtom.com/en_gb/traffic-index/auckland-traffic/ - during rush hour, 20 mins of extra time is spent waiting
    # mean of 600 seconds with a standard deviation of 180 flattens the normal curve at around 0 and 1200 seconds (20 min), making it less
    # less likely to occur on a given day
    traffic_duration = stats.norm.rvs(20*60, 7*60)

    # Finding the time duration between the distribution centre and the first store in addition to the pallet unloading time at the store and traffic
    first_store_time = travel_durations_df[route_array[0]]['Distribution Centre Auckland'] + (450 * store_vars.get(route_array[0]))
    
    # Finding the time duration between the current store and the next store in the route in addition to the pallet unloading time at the current store and traffic
    rest_of_store_times = 0
    for i in range(1, len(route_array)):
        rest_of_store_times += ((travel_durations_df[route_array[i-1]][route_array[i]] + (450 * store_vars.get(route_array[i]))))
    
    # Finding the time duration between the distribution centre and the last store in addition to the pallet unloading time at the store and traffic
    last_store_time = travel_durations_df['Distribution Centre Auckland'][route_array[-1]]

    # Find the total cost
    final_duration = (first_store_time + rest_of_store_times + last_store_time + traffic_duration) / 3600
    if final_duration <= 4:
        total_cost = final_duration * 225
    else:
        init_cost = 4 * 225
        total_cost = init_cost + ((final_duration - 4) * 275)
    
    return total_cost

"""Weekday Simulation"""

def weekday_closure_sim():
    # Generating the max costs times for weekdays
    sum_simulation_costs_weekday_closure = [0] * 2000
    median_extra_trucks_weekday_closure = [0] * 2000

    # Simulating routes
    for i in range(len(sum_simulation_costs_weekday_closure)):
        # Using bootstrap method to repeatedly resample demands for each store
        store_vars_closure = {}
        for j in range(len(weekday_mean_variance_closure['Store'].values)):
            store_name = weekday_mean_variance_closure['Store'].values[j] # store
            mu = weekday_mean_variance_closure['Weekday_mean'].values[j] # mean
            sigma = np.sqrt(weekday_mean_variance_closure['Weekday_variance'].values[j]) # standard deviation
            # Assuming normal distribution and bootstrapping repeatedly
            results = statistics.median(stats.norm.rvs(loc = mu, scale = sigma, size=50))
            # Storing the stores and their results in a dictionary814215
            store_vars_closure.update({store_name : results})
        
        # finding the routes for the simulation
        good_path_vars_closure = {}
        extra_trucks_used_weekday_closure = 0

        # Looping through all weekday routes
        for route in allweekdayroutes:
            # Find good routes and their respective demands and number of trucks needed
            good_paths, good_path_demands, no_of_trucks = split_my_array(list(route), store_vars_closure)

            # Loop through routes in specific schedule
            for k in range(len(good_paths)):
                good_path_vars_closure[good_paths[k]] = good_path_demands[k]
            extra_trucks_used_weekday_closure += no_of_trucks
        
        # finding the cost for each of the routes
        route_cost = {}
        
        # Loop through all schedules in good schedules
        for paths in good_path_vars_closure:
            route_cost.update({ paths : find_my_cost(list(paths), store_vars_closure)})
        
        sum_simulation_costs_weekday_closure[i] = sum(list(route_cost.values()))
        median_extra_trucks_weekday_closure[i] = extra_trucks_used_weekday_closure


    print("No. of trucks used in total after closure: " + str(num_weekday + math.ceil(statistics.median(median_extra_trucks_weekday_closure))))


    # Average cost for weekdays
    print("Average cost for weekdays after closure: $" + str(statistics.median(sum_simulation_costs_weekday_closure)))


    # One sample t-test, with H0 = expected cost for weekdays.
    print("One sample T-test for weekday after closure: " + str(stats.ttest_1samp(sum_simulation_costs_weekday_closure, statistics.median(sum_simulation_costs_weekday_closure))))


    # Percentile interval
    sum_simulation_costs_weekday_closure.sort()
    lower_bound = sum_simulation_costs_weekday_closure[25]
    upper_bound = sum_simulation_costs_weekday_closure[1975]

    print("lower bound after closure: " + str(lower_bound))
    print("upper bound after closure: " + str(upper_bound))

    # show the plot
    sns.distplot(sum_simulation_costs_weekday_closure)
    plt.title("Simulation for the stores weekdays after closure")
    plt.xlabel("Cost ($ NZD)")
    plt.vlines([lower_bound, upper_bound], 0, 0.0015, colors="r", linestyles="--")
    plt.show()



"""Weekend Simulation"""

def weekend_closure_sim():
    # Generating the max costs times for weekdays
    sum_simulation_costs_weekend_closure = [0] * 2000
    median_extra_trucks_weekend_closure = [0] * 2000

    for i in range(len(sum_simulation_costs_weekend_closure)):
        # Using bootstrap method to repeatedly resample demands for each store
        store_vars_closure = {}
        for j in range(len(weekend_mean_variance_closure['Store'].values)):
            store_name = weekend_mean_variance_closure['Store'].values[j]
            mu = weekend_mean_variance_closure['Weekend_mean'].values[j]
            sigma = np.sqrt(weekend_mean_variance_closure['Weekend_variance'].values[j])
            # Assuming normal distribution and bootstrapping repeatedly
            results = statistics.median(stats.norm.rvs(loc = mu, scale = sigma, size=50))
            # Storing the stores and their results ina dictionary
            store_vars_closure.update({store_name : results})
        
        # finding the routes for the simulation
        good_path_vars = {}
        extra_trucks_used_weekend = 0

        for route in allweekendroutes:
            good_paths, good_path_demands, no_of_trucks = split_my_array(list(route), store_vars_closure)
            for k in range(len(good_paths)):
                good_path_vars[good_paths[k]] = good_path_demands[k]
            extra_trucks_used_weekend += no_of_trucks
        
        # finding the cost for each of the routes
        route_cost = {}
        
        for paths in good_path_vars:
            route_cost.update({ paths : find_my_cost(list(paths), store_vars_closure)})
        
        sum_simulation_costs_weekend_closure[i] = sum(list(route_cost.values()))
        median_extra_trucks_weekend_closure[i] = extra_trucks_used_weekend


    print("No. of trucks used in total after closure: " + str(num_weekend + math.ceil(statistics.median(median_extra_trucks_weekend_closure))))


    # Average cost for weekdays
    print("Average cost for weekend after closure: $" + str(statistics.median(sum_simulation_costs_weekend_closure)))


    # One sample t-test, with H0 = expected cost for weekdays.
    print("One sample T-test for weekdend after closure: " + str(stats.ttest_1samp(sum_simulation_costs_weekend_closure, statistics.median(sum_simulation_costs_weekend_closure))))


    # Percentile interval
    sum_simulation_costs_weekend_closure.sort()
    lower_bound = sum_simulation_costs_weekend_closure[25]
    upper_bound = sum_simulation_costs_weekend_closure[1975]

    print("lower bound after closure: " + str(lower_bound))
    print("upper bound after closure: " + str(upper_bound))

    # show the plot
    sns.distplot(sum_simulation_costs_weekend_closure)
    plt.title("Simulation for the stores weekend after closure")
    plt.xlabel("Cost ($ NZD)")
    plt.vlines([lower_bound, upper_bound], 0, 0.0038, colors="r", linestyles="--")
    plt.show()