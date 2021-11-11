import pandas as pd

def create_dict(csv_file):
    dataset = pd.read_csv(csv_file, header = None, skiprows = [0])
    flights = {'passengers': dataset.iloc[:,1], 'time period': dataset.iloc[:,2]}
    gates = {'distance': dataset.iloc[:,4]}

    return flights, gates
