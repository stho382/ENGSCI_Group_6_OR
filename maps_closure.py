import pandas as pd
import folium
from weekend_routes_closure import *
from weekday_routes_closure import *
from dotenv import load_dotenv
import os
import openrouteservice as ors

demands_df = pd.read_csv('https://raw.githubusercontent.com/stho382/ENGSCI_Group_6_OR/main/Data/WoolworthsDemands.csv')
distances_df = pd.read_csv('https://raw.githubusercontent.com/stho382/ENGSCI_Group_6_OR/main/Data/WoolworthsDistances.csv')
locations_df = pd.read_csv('https://raw.githubusercontent.com/stho382/ENGSCI_Group_6_OR/main/Data/WoolworthsLocations.csv')
travel_durations_df = pd.read_csv('https://raw.githubusercontent.com/stho382/ENGSCI_Group_6_OR/main/Data/WoolworthsTravelDurations.csv')
north_df = pd.read_csv('https://raw.githubusercontent.com/stho382/ENGSCI_Group_6_OR/main/Data/LocationNorthRegion.csv')
south_df = pd.read_csv('https://raw.githubusercontent.com/stho382/ENGSCI_Group_6_OR/main/Data/LocationSouthRegion.csv')
west_df = pd.read_csv('https://raw.githubusercontent.com/stho382/ENGSCI_Group_6_OR/main/Data/LocationWestRegion.csv')
east_df = pd.read_csv('https://raw.githubusercontent.com/stho382/ENGSCI_Group_6_OR/main/Data/LocationEastRegion.csv')
centralNorth_df = pd.read_csv('https://raw.githubusercontent.com/stho382/ENGSCI_Group_6_OR/main/Data/LocationCentralNorth.csv')
centralSouth_df = pd.read_csv('https://raw.githubusercontent.com/stho382/ENGSCI_Group_6_OR/main/Data/LocationCentralSouth.csv')

locationsclosure_df = pd.read_csv('' + os.getcwd() + os.sep + 'Data' + os.sep + 'WoolworthsLocations_closure.csv')

coords_closure = locationsclosure_df[['Long', 'Lat']] # Mapping packages work with Long, Lat arrays
coords_closure = coords_closure.to_numpy().tolist() # Make the arrays into a list of lists.

allweekdayroutes = []
allweekendroutes = []

for i in range(len(optimalRoutes_weekday)):
    optimalRoutes_weekday_number = int(optimalRoutes_weekday[i][14:len(optimalRoutes_weekday[i])])
    allweekdayroutes.append(Routes_Weekday[optimalRoutes_weekday_number])

for i in range(len(optimalRoutes_weekend)):
    optimalRoutes_weekend_number = int(optimalRoutes_weekend[i][14:len(optimalRoutes_weekend[i])])
    allweekendroutes.append(Routes_Weekend[optimalRoutes_weekend_number])

# Importing API key
load_dotenv()
API_KEY = os.getenv("API_KEY")
client = ors.Client(key=f"{API_KEY}")

# adding routes to route_weekday
route_weekday = []
    # Loops through all optimal routes on weekdays
for i in range(len(optimalRoutes_weekday)):

        # Finds all stores in specific route
    list_routes = Routes_Weekday[int(optimalRoutes_weekday[i][14:])]

        # Create a coordinates array to store locations of stores
    coordinates = []

        # Loops through specific route
    for j in range(len(list_routes)):
            
            # Loops through all stores
        for k in range(len(locationsclosure_df)):

                # Compares specific route store with all stores and appends location to coordinates array
            if list_routes[j] == locationsclosure_df.Store[k]:
                coordinates.append(coords_closure[k])

        # Checks if specific route is going through 2 stores
    if (len(coordinates) == 2):
        route_weekday.append(client.directions(
        coordinates = [coords_closure[53], coordinates[0], coordinates[1], coords_closure[53]], 
        profile = 'driving-hgv', # can be driving-car, driving-hgv, etc.
        format='geojson',
        validate = False
        ))

    # Checks if specific route is going through 3 stores
    elif (len(coordinates) == 3):
        route_weekday.append(client.directions(
        coordinates = [coords_closure[53], coordinates[0], coordinates[1], coordinates[2], coords_closure[53]], 
        profile = 'driving-hgv', # can be driving-car, driving-hgv, etc.
        format='geojson',
        validate = False
        ))

    # Checks if specific route is going through 4 stores
    elif (len(coordinates) == 4):
        route_weekday.append(client.directions(
        coordinates = [coords_closure[53], coordinates[0], coordinates[1], coordinates[2], coordinates[3], coords_closure[53]], 
        profile = 'driving-hgv', # can be driving-car, driving-hgv, etc.
        format='geojson',
        validate = False
        ))

    # Checks if specific route is going through 5 stores
    elif (len(coordinates) == 5):
        route_weekday.append(client.directions(
        coordinates = [coords_closure[53], coordinates[0], coordinates[1], coordinates[2], coordinates[3], coordinates[4], coords_closure[53]], 
        profile = 'driving-hgv', # can be driving-car, driving-hgv, etc.
        format='geojson',
        validate = False
        ))

    # Checks if specific route is going through 6 stores
    elif (len(coordinates) == 6):
        route_weekday.append(client.directions(
        coordinates = [coords_closure[53], coordinates[0], coordinates[1], coordinates[2], coordinates[3], coordinates[4], coordinates[5], coords_closure[53]],
        profile = 'driving-hgv', # can be driving-car, driving-hgv, etc.
        format='geojson',
        validate = False
        ))

m = folium.Map(location = list(reversed(coords_closure[2])), zoom_start=10)
folium.Marker(list(reversed(coords_closure[0])), popup = locationsclosure_df.Store.values[0], icon = folium.Icon(color = 'green')).add_to(m)

for i in range(len(locationsclosure_df.Store)):
  if locationsclosure_df.Type[i] == "Distribution Centre":
    iconCol = "white"
    folium.Marker(list(reversed(coords_closure[i])), popup = locationsclosure_df.Store.values[i], icon = folium.Icon(color = iconCol)).add_to(m)
  for j in range (1, len(north_df.Store)):
    if locationsclosure_df.Store[i] == north_df.Store[j]:
      iconCol = "green"
      folium.Marker(list(reversed(coords_closure[i])), popup = locationsclosure_df.Store.values[i], icon = folium.Icon(color = iconCol)).add_to(m)
  for k in range (1, len(south_df.Store)):
    if locationsclosure_df.Store[i] == south_df.Store[k]:
      iconCol = "blue"
      folium.Marker(list(reversed(coords_closure[i])), popup = locationsclosure_df.Store.values[i], icon = folium.Icon(color = iconCol)).add_to(m)
  for l in range (1, len(east_df.Store)):
    if locationsclosure_df.Store[i] == east_df.Store[l]:
      iconCol = "purple"
      folium.Marker(list(reversed(coords_closure[i])), popup = locationsclosure_df.Store.values[i], icon = folium.Icon(color = iconCol)).add_to(m)
  for n in range (1, len(west_df.Store)):
    if locationsclosure_df.Store[i] == west_df.Store[n]:
      iconCol = "black"
      folium.Marker(list(reversed(coords_closure[i])), popup = locationsclosure_df.Store.values[i], icon = folium.Icon(color = iconCol)).add_to(m)
  for o in range (1, len(centralNorth_df.Store)):
    if locationsclosure_df.Store[i] == centralNorth_df.Store[o]:
      iconCol = "red"
      folium.Marker(list(reversed(coords_closure[i])), popup = locationsclosure_df.Store.values[i], icon = folium.Icon(color = iconCol)).add_to(m)
  for p in range (1, len(centralSouth_df.Store)):
    if locationsclosure_df.Store[i] == centralSouth_df.Store[p]:
      iconCol = "lightblue"
      folium.Marker(list(reversed(coords_closure[i])), popup = locationsclosure_df.Store.values[i], icon = folium.Icon(color = iconCol)).add_to(m)

# north = green   east = red    west = blue  south = black  centralnorth = purple  centralsouth = lightblue

# allweekdayroutes = []

# for i in range(len(optimalRoutes_weekday)):
#     optimalRoutes_weekday_number = int(optimalRoutes_weekday[i][14:len(optimalRoutes_weekday[i])])
#     allweekdayroutes.append(Routes_Weekday[optimalRoutes_weekday_number])

for i in range(len(optimalRoutes_weekday)):
  
  if (len(allweekdayroutes[i])==2):
   
    for j in range (len(allweekdayroutes[i])):
     
      for store in range (len(west_df.Store)):
        if (allweekdayroutes[i][j] == west_df.Store[store]):
          folium.PolyLine(locations = [list(reversed(coord))
          for coord in
          route_weekday[i]['features'][0]['geometry']['coordinates']],weight=3, color='black',).add_to(m)
    
      for store in range (len(north_df.Store)):
        if (allweekdayroutes[i][j] == north_df.Store[store]):
          folium.PolyLine(locations = [list(reversed(coord))
          for coord in
          route_weekday[i]['features'][0]['geometry']['coordinates']],weight=3, color='green',).add_to(m)
     
      for store in range (len(centralNorth_df.Store)):
        if (allweekdayroutes[i][j] == centralNorth_df.Store[store]):
          folium.PolyLine(locations = [list(reversed(coord))
          for coord in
          route_weekday[i]['features'][0]['geometry']['coordinates']],weight=3, color='red',).add_to(m)
     
      for store in range (len(centralSouth_df.Store)):
        if (allweekdayroutes[i][j] == centralSouth_df.Store[store]):
          folium.PolyLine(locations = [list(reversed(coord))
          for coord in
          route_weekday[i]['features'][0]['geometry']['coordinates']],weight=3, color='lightblue',).add_to(m)
     
      for store in range (len(east_df.Store)):
        if (allweekdayroutes[i][j] == east_df.Store[store]):
          folium.PolyLine(locations = [list(reversed(coord))
          for coord in
          route_weekday[i]['features'][0]['geometry']['coordinates']],weight=3, color='purple',).add_to(m)
   
      for store in range (len(south_df.Store)):
        if (allweekdayroutes[i][j] == south_df.Store[store]):
          folium.PolyLine(locations = [list(reversed(coord))
          for coord in
          route_weekday[i]['features'][0]['geometry']['coordinates']],weight=3, color='blue',).add_to(m)

  elif (len(allweekdayroutes[i])==3):
   
    for f in range (len(allweekdayroutes[i])):
   
      for store in range (len(west_df.Store)):
        if (allweekdayroutes[i][f] == west_df.Store[store]):
          folium.PolyLine(locations = [list(reversed(coord))
          for coord in
          route_weekday[i]['features'][0]['geometry']['coordinates']],weight=3, color='black',).add_to(m)
   
      for store in range (len(north_df.Store)):
        if (allweekdayroutes[i][f] == north_df.Store[store]):
          folium.PolyLine(locations = [list(reversed(coord))
          for coord in
          route_weekday[i]['features'][0]['geometry']['coordinates']],weight=3, color='green',).add_to(m)
   
      for store in range (len(centralNorth_df.Store)):
        if (allweekdayroutes[i][f] == centralNorth_df.Store[store]):
          folium.PolyLine(locations = [list(reversed(coord))
          for coord in
          route_weekday[i]['features'][0]['geometry']['coordinates']],weight=3, color='red',).add_to(m)
    
      for store in range (len(centralSouth_df.Store)):
        if (allweekdayroutes[i][f] == centralSouth_df.Store[store]):
          folium.PolyLine(locations = [list(reversed(coord))
          for coord in
          route_weekday[i]['features'][0]['geometry']['coordinates']],weight=3, color='lightblue',).add_to(m)
    
      for store in range (len(east_df.Store)):
        if (allweekdayroutes[i][f] == east_df.Store[store]):
          folium.PolyLine(locations = [list(reversed(coord))
          for coord in
          route_weekday[i]['features'][0]['geometry']['coordinates']],weight=3, color='purple',).add_to(m)
    
      for store in range (len(south_df.Store)):
        if (allweekdayroutes[i][f] == south_df.Store[store]):
          folium.PolyLine(locations = [list(reversed(coord))
          for coord in
          route_weekday[i]['features'][0]['geometry']['coordinates']],weight=3, color='blue',).add_to(m)
 
  elif (len(allweekdayroutes[i])==4):
 
    for q in range (len(allweekdayroutes[i])):

      for store in range (len(west_df.Store)):
        if (allweekdayroutes[i][q] == west_df.Store[store]):
          folium.PolyLine(locations = [list(reversed(coord))
          for coord in
          route_weekday[i]['features'][0]['geometry']['coordinates']],weight=3, color='black',).add_to(m)
 
      for store in range (len(north_df.Store)):
        if (allweekdayroutes[i][q] == north_df.Store[store]):
          folium.PolyLine(locations = [list(reversed(coord))
          for coord in
          route_weekday[i]['features'][0]['geometry']['coordinates']],weight=3, color='green',).add_to(m)
 
      for store in range (len(centralNorth_df.Store)):
        if (allweekdayroutes[i][q] == centralNorth_df.Store[store]):
          folium.PolyLine(locations = [list(reversed(coord))
          for coord in
          route_weekday[i]['features'][0]['geometry']['coordinates']],weight=3, color='red',).add_to(m)
 
      for store in range (len(centralSouth_df.Store)):
        if (allweekdayroutes[i][q] == centralSouth_df.Store[store]):
          folium.PolyLine(locations = [list(reversed(coord))
          for coord in
          route_weekday[i]['features'][0]['geometry']['coordinates']],weight=3, color='lightblue',).add_to(m)
 
      for store in range (len(east_df.Store)):
        if (allweekdayroutes[i][q] == east_df.Store[store]):
          folium.PolyLine(locations = [list(reversed(coord))
          for coord in
          route_weekday[i]['features'][0]['geometry']['coordinates']],weight=3, color='purple',).add_to(m)
 
      for store in range (len(south_df.Store)):
        if (allweekdayroutes[i][q] == south_df.Store[store]):
          folium.PolyLine(locations = [list(reversed(coord))
          for coord in
          route_weekday[i]['features'][0]['geometry']['coordinates']],weight=3, color='blue',).add_to(m)
 
  elif (len(allweekdayroutes[i])==5):
 
    for x in range (len(allweekdayroutes[i])):

      for store in range (len(west_df.Store)):
        if (allweekdayroutes[i][x] == west_df.Store[store]):
          folium.PolyLine(locations = [list(reversed(coord))
          for coord in
          route_weekday[i]['features'][0]['geometry']['coordinates']],weight=3, color='black',).add_to(m)
 
      for store in range (len(north_df.Store)):
        if (allweekdayroutes[i][x] == north_df.Store[store]):
          folium.PolyLine(locations = [list(reversed(coord))
          for coord in
          route_weekday[i]['features'][0]['geometry']['coordinates']],weight=3, color='green',).add_to(m)
 
      for store in range (len(centralNorth_df.Store)):
        if (allweekdayroutes[i][x] == centralNorth_df.Store[store]):
          folium.PolyLine(locations = [list(reversed(coord))
          for coord in
          route_weekday[i]['features'][0]['geometry']['coordinates']],weight=3, color='red',).add_to(m)
 
      for store in range (len(centralSouth_df.Store)):
        if (allweekdayroutes[i][x] == centralSouth_df.Store[store]):
          folium.PolyLine(locations = [list(reversed(coord))
          for coord in
          route_weekday[i]['features'][0]['geometry']['coordinates']],weight=3, color='lightblue',).add_to(m)
 
      for store in range (len(east_df.Store)):
        if (allweekdayroutes[i][x] == east_df.Store[store]):
          folium.PolyLine(locations = [list(reversed(coord))
          for coord in
          route_weekday[i]['features'][0]['geometry']['coordinates']],weight=3, color='purple',).add_to(m)
 
      for store in range (len(south_df.Store)):
        if (allweekdayroutes[i][x] == south_df.Store[store]):
          folium.PolyLine(locations = [list(reversed(coord))
          for coord in
          route_weekday[i]['features'][0]['geometry']['coordinates']],weight=3, color='blue',).add_to(m)
 
  elif (len(allweekdayroutes[i])==6):
 
    for x2 in range (len(allweekdayroutes[i])):

      for store in range (len(west_df.Store)):
        if (allweekdayroutes[i][x2] == west_df.Store[store]):
          folium.PolyLine(locations = [list(reversed(coord))
          for coord in
          route_weekday[i]['features'][0]['geometry']['coordinates']],weight=3, color='black',).add_to(m)
 
      for store in range (len(north_df.Store)):
        if (allweekdayroutes[i][x2] == north_df.Store[store]):
          folium.PolyLine(locations = [list(reversed(coord))
          for coord in
          route_weekday[i]['features'][0]['geometry']['coordinates']],weight=3, color='green',).add_to(m)
 
      for store in range (len(centralNorth_df.Store)):
        if (allweekdayroutes[i][x2] == centralNorth_df.Store[store]):
          folium.PolyLine(locations = [list(reversed(coord))
          for coord in
          route_weekday[i]['features'][0]['geometry']['coordinates']],weight=3, color='red',).add_to(m)
 
      for store in range (len(centralSouth_df.Store)):
        if (allweekdayroutes[i][x2] == centralSouth_df.Store[store]):
          folium.PolyLine(locations = [list(reversed(coord))
          for coord in
          route_weekday[i]['features'][0]['geometry']['coordinates']],weight=3, color='lightblue',).add_to(m)
 
      for store in range (len(east_df.Store)):
        if (allweekdayroutes[i][x2] == east_df.Store[store]):
          folium.PolyLine(locations = [list(reversed(coord))
          for coord in
          route_weekday[i]['features'][0]['geometry']['coordinates']],weight=3, color='purple',).add_to(m)
 
      for store in range (len(south_df.Store)):
        if (allweekdayroutes[i][x2] == south_df.Store[store]):
          folium.PolyLine(locations = [list(reversed(coord))
          for coord in
          route_weekday[i]['features'][0]['geometry']['coordinates']],weight=3, color='blue',).add_to(m)

m.save("" + os.getcwd() + os.sep + "route_maps" + os.sep + "weekday_closure_route_visualisation.html")


# WEEKEND

# adding routes to route_weekday
route_weekend = []
    # Loops through all optimal routes on weekdays
for i in range(len(optimalRoutes_weekend)):

        # Finds all stores in specific route
    list_routes = Routes_Weekend[int(optimalRoutes_weekend[i][14:])]

        # Create a coordinates array to store locations of stores
    coordinates = []

        # Loops through specific route
    for j in range(len(list_routes)):
            
            # Loops through all stores
        for k in range(len(locationsclosure_df)):

                # Compares specific route store with all stores and appends location to coordinates array
            if list_routes[j] == locationsclosure_df.Store[k]:
                coordinates.append(coords_closure[k])

        # Checks if specific route is going through 2 stores
    if (len(coordinates) == 2):
        route_weekend.append(client.directions(
        coordinates = [coords_closure[53], coordinates[0], coordinates[1], coords_closure[53]], 
        profile = 'driving-hgv', # can be driving-car, driving-hgv, etc.
        format='geojson',
        validate = False
        ))

    # Checks if specific route is going through 3 stores
    elif (len(coordinates) == 3):
        route_weekend.append(client.directions(
        coordinates = [coords_closure[53], coordinates[0], coordinates[1], coordinates[2], coords_closure[53]], 
        profile = 'driving-hgv', # can be driving-car, driving-hgv, etc.
        format='geojson',
        validate = False
        ))

    # Checks if specific route is going through 4 stores
    elif (len(coordinates) == 4):
        route_weekend.append(client.directions(
        coordinates = [coords_closure[53], coordinates[0], coordinates[1], coordinates[2], coordinates[3], coords_closure[53]], 
        profile = 'driving-hgv', # can be driving-car, driving-hgv, etc.
        format='geojson',
        validate = False
        ))

    # Checks if specific route is going through 5 stores
    elif (len(coordinates) == 5):
        route_weekend.append(client.directions(
        coordinates = [coords_closure[53], coordinates[0], coordinates[1], coordinates[2], coordinates[3], coordinates[4], coords_closure[53]], 
        profile = 'driving-hgv', # can be driving-car, driving-hgv, etc.
        format='geojson',
        validate = False
        ))

    # Checks if specific route is going through 6 stores
    elif (len(coordinates) == 6):
        route_weekend.append(client.directions(
        coordinates = [coords_closure[53], coordinates[0], coordinates[1], coordinates[2], coordinates[3], coordinates[4], coordinates[5], coords_closure[53]],
        profile = 'driving-hgv', # can be driving-car, driving-hgv, etc.
        format='geojson',
        validate = False
        ))

m = folium.Map(location = list(reversed(coords_closure[2])), zoom_start=10)
folium.Marker(list(reversed(coords_closure[0])), popup = locationsclosure_df.Store.values[0], icon = folium.Icon(color = 'green')).add_to(m)

for i in range(len(locationsclosure_df.Store)):
  if locationsclosure_df.Type[i] == "Distribution Centre":
    iconCol = "white"
    folium.Marker(list(reversed(coords_closure[i])), popup = locationsclosure_df.Store.values[i], icon = folium.Icon(color = iconCol)).add_to(m)
  for j in range (1, len(north_df.Store)):
    if locationsclosure_df.Store[i] == north_df.Store[j]:
      iconCol = "green"
      folium.Marker(list(reversed(coords_closure[i])), popup = locationsclosure_df.Store.values[i], icon = folium.Icon(color = iconCol)).add_to(m)
  for k in range (1, len(south_df.Store)):
    if locationsclosure_df.Store[i] == south_df.Store[k]:
      iconCol = "blue"
      folium.Marker(list(reversed(coords_closure[i])), popup = locationsclosure_df.Store.values[i], icon = folium.Icon(color = iconCol)).add_to(m)
  for l in range (1, len(east_df.Store)):
    if locationsclosure_df.Store[i] == east_df.Store[l]:
      iconCol = "purple"
      folium.Marker(list(reversed(coords_closure[i])), popup = locationsclosure_df.Store.values[i], icon = folium.Icon(color = iconCol)).add_to(m)
  for n in range (1, len(west_df.Store)):
    if locationsclosure_df.Store[i] == west_df.Store[n]:
      iconCol = "black"
      folium.Marker(list(reversed(coords_closure[i])), popup = locationsclosure_df.Store.values[i], icon = folium.Icon(color = iconCol)).add_to(m)
  for o in range (1, len(centralNorth_df.Store)):
    if locationsclosure_df.Store[i] == centralNorth_df.Store[o]:
      iconCol = "red"
      folium.Marker(list(reversed(coords_closure[i])), popup = locationsclosure_df.Store.values[i], icon = folium.Icon(color = iconCol)).add_to(m)
  for p in range (1, len(centralSouth_df.Store)):
    if locationsclosure_df.Store[i] == centralSouth_df.Store[p]:
      iconCol = "lightblue"
      folium.Marker(list(reversed(coords_closure[i])), popup = locationsclosure_df.Store.values[i], icon = folium.Icon(color = iconCol)).add_to(m)

# north = green   east = red    west = blue  south = black  centralnorth = purple  centralsouth = lightblue




for i in range(len(optimalRoutes_weekend)):
  
  if (len(allweekendroutes[i])==2):
   
    for j in range (len(allweekendroutes[i])):
     
      for store in range (len(west_df.Store)):
        if (allweekendroutes[i][j] == west_df.Store[store]):
          folium.PolyLine(locations = [list(reversed(coord))
          for coord in
          route_weekend[i]['features'][0]['geometry']['coordinates']],weight=3, color='black',).add_to(m)
    
      for store in range (len(north_df.Store)):
        if (allweekendroutes[i][j] == north_df.Store[store]):
          folium.PolyLine(locations = [list(reversed(coord))
          for coord in
          route_weekend[i]['features'][0]['geometry']['coordinates']],weight=3, color='green',).add_to(m)
     
      for store in range (len(centralNorth_df.Store)):
        if (allweekendroutes[i][j] == centralNorth_df.Store[store]):
          folium.PolyLine(locations = [list(reversed(coord))
          for coord in
          route_weekend[i]['features'][0]['geometry']['coordinates']],weight=3, color='red',).add_to(m)
     
      for store in range (len(centralSouth_df.Store)):
        if (allweekendroutes[i][j] == centralSouth_df.Store[store]):
          folium.PolyLine(locations = [list(reversed(coord))
          for coord in
          route_weekend[i]['features'][0]['geometry']['coordinates']],weight=3, color='lightblue',).add_to(m)
     
      for store in range (len(east_df.Store)):
        if (allweekendroutes[i][j] == east_df.Store[store]):
          folium.PolyLine(locations = [list(reversed(coord))
          for coord in
          route_weekend[i]['features'][0]['geometry']['coordinates']],weight=3, color='purple',).add_to(m)
   
      for store in range (len(south_df.Store)):
        if (allweekendroutes[i][j] == south_df.Store[store]):
          folium.PolyLine(locations = [list(reversed(coord))
          for coord in
          route_weekend[i]['features'][0]['geometry']['coordinates']],weight=3, color='blue',).add_to(m)

  elif (len(allweekendroutes[i])==3):
   
    for f in range (len(allweekendroutes[i])):
   
      for store in range (len(west_df.Store)):
        if (allweekendroutes[i][f] == west_df.Store[store]):
          folium.PolyLine(locations = [list(reversed(coord))
          for coord in
          route_weekend[i]['features'][0]['geometry']['coordinates']],weight=3, color='black',).add_to(m)
   
      for store in range (len(north_df.Store)):
        if (allweekendroutes[i][f] == north_df.Store[store]):
          folium.PolyLine(locations = [list(reversed(coord))
          for coord in
          route_weekend[i]['features'][0]['geometry']['coordinates']],weight=3, color='green',).add_to(m)
   
      for store in range (len(centralNorth_df.Store)):
        if (allweekendroutes[i][f] == centralNorth_df.Store[store]):
          folium.PolyLine(locations = [list(reversed(coord))
          for coord in
          route_weekend[i]['features'][0]['geometry']['coordinates']],weight=3, color='red',).add_to(m)
    
      for store in range (len(centralSouth_df.Store)):
        if (allweekendroutes[i][f] == centralSouth_df.Store[store]):
          folium.PolyLine(locations = [list(reversed(coord))
          for coord in
          route_weekend[i]['features'][0]['geometry']['coordinates']],weight=3, color='lightblue',).add_to(m)
    
      for store in range (len(east_df.Store)):
        if (allweekendroutes[i][f] == east_df.Store[store]):
          folium.PolyLine(locations = [list(reversed(coord))
          for coord in
          route_weekend[i]['features'][0]['geometry']['coordinates']],weight=3, color='purple',).add_to(m)
    
      for store in range (len(south_df.Store)):
        if (allweekendroutes[i][f] == south_df.Store[store]):
          folium.PolyLine(locations = [list(reversed(coord))
          for coord in
          route_weekend[i]['features'][0]['geometry']['coordinates']],weight=3, color='blue',).add_to(m)
 
  elif (len(allweekendroutes[i])==4):
 
    for q in range (len(allweekendroutes[i])):

      for store in range (len(west_df.Store)):
        if (allweekendroutes[i][q] == west_df.Store[store]):
          folium.PolyLine(locations = [list(reversed(coord))
          for coord in
          route_weekend[i]['features'][0]['geometry']['coordinates']],weight=3, color='black',).add_to(m)
 
      for store in range (len(north_df.Store)):
        if (allweekendroutes[i][q] == north_df.Store[store]):
          folium.PolyLine(locations = [list(reversed(coord))
          for coord in
          route_weekend[i]['features'][0]['geometry']['coordinates']],weight=3, color='green',).add_to(m)
 
      for store in range (len(centralNorth_df.Store)):
        if (allweekendroutes[i][q] == centralNorth_df.Store[store]):
          folium.PolyLine(locations = [list(reversed(coord))
          for coord in
          route_weekend[i]['features'][0]['geometry']['coordinates']],weight=3, color='red',).add_to(m)
 
      for store in range (len(centralSouth_df.Store)):
        if (allweekendroutes[i][q] == centralSouth_df.Store[store]):
          folium.PolyLine(locations = [list(reversed(coord))
          for coord in
          route_weekend[i]['features'][0]['geometry']['coordinates']],weight=3, color='lightblue',).add_to(m)
 
      for store in range (len(east_df.Store)):
        if (allweekendroutes[i][q] == east_df.Store[store]):
          folium.PolyLine(locations = [list(reversed(coord))
          for coord in
          route_weekend[i]['features'][0]['geometry']['coordinates']],weight=3, color='purple',).add_to(m)
 
      for store in range (len(south_df.Store)):
        if (allweekendroutes[i][q] == south_df.Store[store]):
          folium.PolyLine(locations = [list(reversed(coord))
          for coord in
          route_weekend[i]['features'][0]['geometry']['coordinates']],weight=3, color='blue',).add_to(m)
 
  elif (len(allweekendroutes[i])==5):
 
    for x in range (len(allweekendroutes[i])):

      for store in range (len(west_df.Store)):
        if (allweekendroutes[i][x] == west_df.Store[store]):
          folium.PolyLine(locations = [list(reversed(coord))
          for coord in
          route_weekend[i]['features'][0]['geometry']['coordinates']],weight=3, color='black',).add_to(m)
 
      for store in range (len(north_df.Store)):
        if (allweekendroutes[i][x] == north_df.Store[store]):
          folium.PolyLine(locations = [list(reversed(coord))
          for coord in
          route_weekend[i]['features'][0]['geometry']['coordinates']],weight=3, color='green',).add_to(m)
 
      for store in range (len(centralNorth_df.Store)):
        if (allweekendroutes[i][x] == centralNorth_df.Store[store]):
          folium.PolyLine(locations = [list(reversed(coord))
          for coord in
          route_weekend[i]['features'][0]['geometry']['coordinates']],weight=3, color='red',).add_to(m)
 
      for store in range (len(centralSouth_df.Store)):
        if (allweekendroutes[i][x] == centralSouth_df.Store[store]):
          folium.PolyLine(locations = [list(reversed(coord))
          for coord in
          route_weekend[i]['features'][0]['geometry']['coordinates']],weight=3, color='lightblue',).add_to(m)
 
      for store in range (len(east_df.Store)):
        if (allweekendroutes[i][x] == east_df.Store[store]):
          folium.PolyLine(locations = [list(reversed(coord))
          for coord in
          route_weekend[i]['features'][0]['geometry']['coordinates']],weight=3, color='purple',).add_to(m)
 
      for store in range (len(south_df.Store)):
        if (allweekendroutes[i][x] == south_df.Store[store]):
          folium.PolyLine(locations = [list(reversed(coord))
          for coord in
          route_weekend[i]['features'][0]['geometry']['coordinates']],weight=3, color='blue',).add_to(m)
 
  elif (len(allweekendroutes[i])==6):
 
    for x2 in range (len(allweekendroutes[i])):

      for store in range (len(west_df.Store)):
        if (allweekendroutes[i][x2] == west_df.Store[store]):
          folium.PolyLine(locations = [list(reversed(coord))
          for coord in
          route_weekend[i]['features'][0]['geometry']['coordinates']],weight=3, color='black',).add_to(m)
 
      for store in range (len(north_df.Store)):
        if (allweekendroutes[i][x2] == north_df.Store[store]):
          folium.PolyLine(locations = [list(reversed(coord))
          for coord in
          route_weekend[i]['features'][0]['geometry']['coordinates']],weight=3, color='green',).add_to(m)
 
      for store in range (len(centralNorth_df.Store)):
        if (allweekendroutes[i][x2] == centralNorth_df.Store[store]):
          folium.PolyLine(locations = [list(reversed(coord))
          for coord in
          route_weekend[i]['features'][0]['geometry']['coordinates']],weight=3, color='red',).add_to(m)
 
      for store in range (len(centralSouth_df.Store)):
        if (allweekendroutes[i][x2] == centralSouth_df.Store[store]):
          folium.PolyLine(locations = [list(reversed(coord))
          for coord in
          route_weekend[i]['features'][0]['geometry']['coordinates']],weight=3, color='lightblue',).add_to(m)
 
      for store in range (len(east_df.Store)):
        if (allweekendroutes[i][x2] == east_df.Store[store]):
          folium.PolyLine(locations = [list(reversed(coord))
          for coord in
          route_weekend[i]['features'][0]['geometry']['coordinates']],weight=3, color='purple',).add_to(m)
 
      for store in range (len(south_df.Store)):
        if (allweekendroutes[i][x2] == south_df.Store[store]):
          folium.PolyLine(locations = [list(reversed(coord))
          for coord in
          route_weekend[i]['features'][0]['geometry']['coordinates']],weight=3, color='blue',).add_to(m)

m.save("" + os.getcwd() + os.sep + "route_maps" + os.sep + "weekend_closure_route_visualisation.html")
