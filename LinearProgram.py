import numpy as np
import pandas as pd
from pulp import *
from routeGeneration import *

max_routes = 30 * 6

possible_routes = [i for i in range(0, len(routes))]

x = LpVariable.dicts("Route", possible_routes, 0, None, LpBinary)

prob += lpSum[(225 * x[route] * hours[route] for route in possible_routes)]

prob += lpSum[(x[route] for route in possible_routes)] <= max_routes

for store in stores:
    prob += lpSum([x[route]] for route in possible_routes if store in routes[route]) == 1

prob.writeLP("Woolworths.lp")

prob.solve()

print("Status:", LPStatus[prob.status])