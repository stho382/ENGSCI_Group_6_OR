import openrouteservice as ors
from OR_Project import *
from OR_visualisations import coords
from dotenv import load_dotenv
import os
import pandas as pd

load_dotenv()
API_KEY = os.getenv("API_KEY")
client = ors.Client(key=f"{API_KEY}")


def routesmappingweekend():
    route_weekend = []
    locations_df = pd.read_csv('https://raw.githubusercontent.com/stho382/ENGSCI_Group_6_OR/main/Data/WoolworthsLocations.csv')
    locations_df.set_index('Store', inplace=True)
    coords = locations_df[['Long', 'Lat']] # Mapping packages work with Long, Lat arrays
    coords = coords.to_numpy().tolist() # Make the arrays into a list of lists.


    # Loops through all optimal routes on weekend
    for i in range(len(optimalRoutes_weekend)):

        # Finds all stores in specific route
        list_routes = Routes_Weekend[int(optimalRoutes_weekend[i][14:])]

        # Create a coordinates array to store locations of stores
        coordinates = []

        # Loops through specific route
        for j in range(len(list_routes)):
            
            # Loops through all stores
            for k in range(len(all_stores)):

                # Compares specific route store with all stores and appends location to coordinates array
                if list_routes[j] == all_stores[k]:
                    coordinates.append(coords[k])

        # Checks if specific route is going through 2 stores
        if (len(list_routes) == 2):
            route_weekend.append(client.directions(
            coordinates = [coords[55], coordinates[0], coordinates[1], coords[55]], 
            profile = 'driving-hgv', # can be driving-car, driving-hgv, etc.
            format='geojson',
            validate = False
            ))

        # Checks if specific route is going through 3 stores
        if (len(list_routes) == 3):
            route_weekend.append(client.directions(
            coordinates = [coords[55], coordinates[0], coordinates[1], coordinates[2], coords[55]], 
            profile = 'driving-hgv', # can be driving-car, driving-hgv, etc.
            format='geojson',
            validate = False
            ))

        # Checks if specific route is going through 4 stores
        if (len(list_routes) == 4):
            route_weekend.append(client.directions(
            coordinates = [coords[55], coordinates[0], coordinates[1], coordinates[2], coordinates[3], coords[55]], 
            profile = 'driving-hgv', # can be driving-car, driving-hgv, etc.
            format='geojson',
            validate = False
            ))

        # Checks if specific route is going through 5 stores
        if (len(list_routes) == 5):
            route_weekend.append(client.directions(
            coordinates = [coords[55], coordinates[0], coordinates[1], coordinates[2], coordinates[3], coordinates[4], coords[55]], 
            profile = 'driving-hgv', # can be driving-car, driving-hgv, etc.
            format='geojson',
            validate = False
            ))

        # Checks if specific route is going through 6 stores
        if (len(list_routes) == 6):
            route_weekend.append(client.directions(
            coordinates = [coords[55], coordinates[0], coordinates[1], coordinates[2], coordinates[3], coordinates[4], coordinates[5], coords[55]],
            profile = 'driving-hgv', # can be driving-car, driving-hgv, etc.
            format='geojson',
            validate = False
            ))


    # Loops through all optimal routes on weekend
    for i in range(len(optimalRoutes_weekend)):

        # Finds all stores in specific route
        list_routes = Routes_Weekend[int(optimalRoutes_weekend[i][14:])]

        # Create a coordinates array to store locations of stores
        coordinates = []

        # Loops through specific route
        for j in range(len(list_routes)):
            
            # Loops through all stores
            for k in range(len(all_stores)):

                # Compares specific route store with all stores and appends location to coordinates array
                if list_routes[j] == all_stores[k]:
                    coordinates.append(coords[k])

        # Checks if specific route is going through 2 stores
        if (len(list_routes) == 2):
            route_weekend.append(client.directions(
            coordinates = [coords[55], coordinates[0], coordinates[1], coords[55]], 
            profile = 'driving-hgv', # can be driving-car, driving-hgv, etc.
            format='geojson',
            validate = False
            ))

        # Checks if specific route is going through 3 stores
        if (len(list_routes) == 3):
            route_weekend.append(client.directions(
            coordinates = [coords[55], coordinates[0], coordinates[1], coordinates[2], coords[55]], 
            profile = 'driving-hgv', # can be driving-car, driving-hgv, etc.
            format='geojson',
            validate = False
            ))

        # Checks if specific route is going through 4 stores
        if (len(list_routes) == 4):
            route_weekend.append(client.directions(
            coordinates = [coords[55], coordinates[0], coordinates[1], coordinates[2], coordinates[3], coords[55]], 
            profile = 'driving-hgv', # can be driving-car, driving-hgv, etc.
            format='geojson',
            validate = False
            ))

        # Checks if specific route is going through 5 stores
        if (len(list_routes) == 5):
            route_weekend.append(client.directions(
            coordinates = [coords[55], coordinates[0], coordinates[1], coordinates[2], coordinates[3], coordinates[4], coords[55]], 
            profile = 'driving-hgv', # can be driving-car, driving-hgv, etc.
            format='geojson',
            validate = False
            ))

        # Checks if specific route is going through 6 stores
        if (len(list_routes) == 6):
            route_weekend.append(client.directions(
            coordinates = [coords[55], coordinates[0], coordinates[1], coordinates[2], coordinates[3], coordinates[4], coordinates[5], coords[55]],
            profile = 'driving-hgv', # can be driving-car, driving-hgv, etc.
            format='geojson',
            validate = False
            ))
