from weekday_routes import *
from weekend_routes import *
from weekday_routes_closure import *
from weekend_routes_closure import *
from simulations import *
import webbrowser

""""Printing Optimal Routes"""
print("\n")

# Prints status of solution
print("Weekday Status bfore closure:", weekday_status)

# The optimised objective function solution
print("Least cost for the Weekday before closure= $", least_cost_weekdays)

print("\n")

print("Number of trucks used in the weekday before closure: ", num_weekday)

print("\n")

for i in range(len(optimalRoutes_weekday)):
    optimalRoutes_weekday_number = int(optimalRoutes_weekday[i][14:len(optimalRoutes_weekday[i])])
    print(Routes_Weekday[optimalRoutes_weekday_number])

print("\n")

# Prints status of solution
print("Weekend Status before closure:", weekend_status)

# The optimised objective function solution
print("Least cost for the Weekend before closure= $", least_cost_weekends)

print("\n")

print("Number of trucks used in the weekends before closure: ", num_weekend)

print("\n")

for i in range(len(optimalRoutes_weekend)):
    optimalRoutes_weekend_number = int(optimalRoutes_weekend[i][14:len(optimalRoutes_weekend[i])])
    print(Routes_Weekend[optimalRoutes_weekend_number])

print("\n")

from weekday_routes_closure import *
from weekend_routes_closure import *

# Prints status of solution
print("Weekday Status after closure:", weekday_status)

# The optimised objective function solution
print("Least cost for the Weekday after closure= $", least_cost_weekdays)

print("\n")

print("Number of trucks used in the weekdays after closure: ", num_weekday)

print("\n")

for i in range(len(optimalRoutes_weekday)):
    optimalRoutes_weekday_number = int(optimalRoutes_weekday[i][14:len(optimalRoutes_weekday[i])])
    print(Routes_Weekday[optimalRoutes_weekday_number])

print("\n")

# Prints status of solution
print("Weekend Status after closure:", weekend_status)

# The optimised objective function solution
print("Least cost for the Weekend after closure= $", least_cost_weekends)

print("\n")

print("Number of trucks used in the weekends after closure: ", num_weekend)

print("\n")

for i in range(len(optimalRoutes_weekend)):
    optimalRoutes_weekend_number = int(optimalRoutes_weekend[i][14:len(optimalRoutes_weekend[i])])
    print(Routes_Weekend[optimalRoutes_weekend_number])


""""Opening visualisation maps"""

print("\n")

print("Opening visualisations of the weekday optimal routes before closure in web browser")
webbrowser.open("" + os.getcwd() + os.sep + "route_maps" + os.sep + "weekday_route_visualisation.html")

print("Opening visualisations of the weekday optimal routes after closure in web browser")
webbrowser.open("" + os.getcwd() + os.sep + "route_maps" + os.sep + "weekday_closure_route_visualisation.html")

print("Opening visualisations of the weekend optimal routes before closure in web browser")
webbrowser.open("" + os.getcwd() + os.sep + "route_maps" + os.sep + "weekend_route_visualisation.html")

print("Opening visualisations of the weekend optimal routesafter closure in web browser")
webbrowser.open("" + os.getcwd() + os.sep + "route_maps" + os.sep + "weekend_closure_route_visualisation.html")

from simulations import *
""""Plotting simulations"""
# weekday simulations
print("\n")
print("Weekday Simulation Statistics before closure of stores:")
weekday_sim()

# weekend simulations
print("\n")
print("Weekend Simulation Statistics before closure of stores:")
weekend_sim()

from simulations_closure import *

# weekday simulations
print("\n")
print("Weekday Simulation Statistics after closure of stores:")
weekday_closure_sim()

# weekend simulations
print("\n")
print("Weekend Simulation Statistics after closure of stores:")
weekend_closure_sim()

print("\n")

