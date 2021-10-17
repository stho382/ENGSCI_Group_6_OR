from weekday_routes import *
from weekend_routes import *
from maps import *
from simulations import *

""""Printing Optimal Routes"""
# Prints status of solution
print("Weekday Status:", weekday_status)

# The optimised objective function solution
print("Least cost for the Weekday =", least_cost_weekdays)

print("\n")

print("Number of trucks used in the weekdays: $", num_weekday)

print("\n")

for i in range(len(optimalRoutes_weekday)):
    optimalRoutes_weekday_number = int(optimalRoutes_weekday[i][14:len(optimalRoutes_weekday[i])])
    print(Routes_Weekday[optimalRoutes_weekday_number])

print("\n")

# Prints status of solution
print("Weekend Status:", weekend_status)

# The optimised objective function solution
print("Least cost for the Weekend = $", least_cost_weekends)

print("\n")

print("Number of trucks used in the weekends: ", num_weekend)

print("\n")

for i in range(len(optimalRoutes_weekend)):
    optimalRoutes_weekend_number = int(optimalRoutes_weekend[i][14:len(optimalRoutes_weekend[i])])
    print(Routes_Weekend[optimalRoutes_weekend_number])


""""Opening visualisation maps"""

print("\n")

print("Opening visualisations of the weekday optimal routes in web browser")
webbrowser.open("" + os.getcwd() + os.sep + "route_maps" + os.sep + "weekday_route_visualisation.html")

print("Opening visualisations of the weekend optimal routes in web browser")
webbrowser.open("" + os.getcwd() + os.sep + "route_maps" + os.sep + "weekend_route_visualisation.html")

""""Plotting simulations"""
# weekday simulations
print("\n")
print("Weekday Simulation Statistics:")
weekday_sim()

# weekedn simulations
print("\n")
print("Weekend Simulation Statistics:")
weekend_sim()