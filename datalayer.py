import pandas as pd

def read_prices(csv_name, date_name_col='ref_date'):
    """
    Read prices from folder data
    """
    data = pd.read_csv("data/{0}.csv".format(csv_name))
    data[date_name_col] = pd.to_datetime(data[date_name_col])
    
    data[csv_name] = data[csv_name].pct_change()
    data = data.dropna(subset=[csv_name])
    
    return data

def read_data(csv_name, date_name_col='ref_date'):
    
    data = pd.read_csv("data/{0}.csv".format(csv_name))
    data[date_name_col] = pd.to_datetime(data[date_name_col])
    
    data = data.dropna(subset=[csv_name])
    
    
    return data


def merge_data_on_ibov(ibov, prices=['spx', 'uc1'], absolute_values=['br_econ_uncert']):
    
    for price_name in prices:
        price_df = read_prices(price_name)
        ibov = ibov.merge(price_df, on='ref_date', how='left')
        
    for abosulute_name in absolute_values:
        absolute_df = read_data(abosulute_name)
        ibov = ibov.merge(absolute_df, on='ref_date', how='left')
        
    #br_gdp_yoy = read_prices("br_gdp_yoy", "release_dt")
    #br_gdp_yoy = br_econ_uncert.rename(columns={"release_dt":"ref_date"})
    #ibov = ibov.merge(br_econ_uncert, on='ref_date', how='left')
    
    return ibov


def fill_na_values(result):
    result['br_econ_uncert'] = result['br_econ_uncert'].fillna(method='ffill')
    
    result = result.dropna()
    
    
    return result


def get_train_data():
    prices = ['spx', 'uc1']
    absolute_values = ['br_econ_uncert']
    
    ibov = read_prices('ibov')
    result = merge_data_on_ibov(ibov, prices, absolute_values)
    result = fill_na_values(result)
    
    return result