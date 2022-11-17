from pathlib import Path
import pandas as pd

def load_data(path = './data', datasets = ['seasons', 'constructors', 'drivers', 'races', 'circuits', 'lap_times', 'results', 'status']):
    data_dir = Path(path).absolute()
    d = {k: pd.read_csv((data_dir/k).with_suffix('.csv')) for k in datasets}
    r = races = d['races']
    r = r.merge(d['results'], on='raceId')
    r = r.merge(d['constructors'], on='constructorId')
    r = r.merge(d['status'], on='statusId')
    r = r.merge(d['drivers'], on='driverId')
    r.drop(columns=[])
    r = r[r.year > 2010]
    races = races[races.year > 2010]
    return r

data = load_data()

