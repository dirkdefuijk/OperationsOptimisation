import seaborn as sb
import numpy as np
import matplotlib.pyplot as plt
from flight_gate_maker import no_timeslots, no_flights
from gatePlanning import model, variables, flights, gates


def create_data(variables, gates, flights):
    data = np.zeros((no_flights,3))

    for i in range(len(variables)):
        for j in range(len(variables[i])):
            if variables[i][j].X == 1:
                data[i,0] = gates["distance"][j]
                data[i,1] = flights["time period"][i]
                data[i,2] = flights["category"][i]
    return data


data = create_data(variables, gates, flights)
sb.barplot(x = data[:,1], y = data[:,0], hue = data[:,2],ci=0,estimator=sum)
plt.xlabel("Time Slot")
plt.ylabel("Walking distance (m)")
plt.legend(title="Category")
plt.show()
