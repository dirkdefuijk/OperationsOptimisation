import pandas as pd

def create_dict(csv_flights, csv_gates):
    dataset_flights = pd.read_csv(csv_flights, header = None, skiprows = [0])
    flights = {'passengers': dataset_flights.iloc[:,1], 'time period': dataset_flights.iloc[:,2], 'category':dataset_flights.iloc[:,3], 'VIP':dataset_flights.iloc[:,4]}

    dataset_gates = pd.read_csv(csv_gates, header = None, skiprows = [0])
    gates = {'distance': dataset_gates.iloc[:,1], 'category': dataset_gates.iloc[:,2]}

    return flights, gates
