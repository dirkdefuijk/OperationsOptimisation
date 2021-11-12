import random
import numpy as np
import pandas as pd

no_flights = 3
no_gates = 3
no_categories = 3
no_timeslots = 32
max_passengers = 300
min_passengers = 50
max_distance = 100

filename = 'test'
np.random.seed(0)

flights = np.arange(0, no_flights, 1).reshape(-1,1)
passengers = np.random.randint(min_passengers, max_passengers, size=no_flights, dtype=int).reshape(-1,1)
flight_timeslots = np.random.randint(0, no_timeslots, size=no_flights, dtype=int).reshape(-1,1)
flight_categories = np.random.randint(0, no_categories, size=no_flights, dtype=int).reshape(-1,1)
temp = np.hstack((flights, passengers, flight_timeslots, flight_categories))
array_flights = np.asarray(['flights', 'passengers', 'timeslot', 'category'])
array_flights = np.vstack((array_flights, temp))
array_flights = pd.DataFrame(array_flights)

array_flights.to_csv(filename + '_flights.csv', index=False, header = False)

gates = np.arange(0, no_gates, 1).reshape(-1,1)
distance = np.random.randint(0, max_distance, size=no_gates, dtype=int).reshape(-1,1)
gates_categories = np.random.randint(0, no_categories, size=no_gates, dtype=int).reshape(-1,1)
temp = np.hstack((gates, distance, gates_categories))
array_gates = np.asarray(['gates', 'distance', 'category'])
array_gates = np.vstack((array_gates, temp))
array_gates = pd.DataFrame(array_gates)

array_gates.to_csv(filename + '_gates.csv', index=False, header = False)
