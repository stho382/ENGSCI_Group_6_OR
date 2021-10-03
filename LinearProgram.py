import numpy as np
import pandas as pd # We will discuss this more next week!
from pulp import *
from routeGeneration import *

possible_routes = [i for i in range(0, len(routes))]

x = LpVariable.dicts("Route", possible_routes, 0, None, LpBinary)
