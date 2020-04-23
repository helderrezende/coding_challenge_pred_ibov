import pandas as pd

def read_prices(csv_name):
    """
    Read prices from folder data
    """
    data = pd.read_csv("data/{0}.csv".format(csv_name))
    data['ref_date'] = pd.to_datetime(data['ref_date'])
    data = data.set_index('ref_date')
    
    data[csv_name] = data[csv_name].pct_change()
    data = data.dropna(subset=[csv_name])
    
    
    return data

