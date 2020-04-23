import pandas as pd

def read_data(csv_name, date_name_col='ref_date'):
    
    data = pd.read_csv("data/{0}.csv".format(csv_name))
    data[date_name_col] = pd.to_datetime(data[date_name_col])
    
    data = data.dropna(subset=[csv_name])
    
    
    return data

def merge_data_on_ibov(ibov, prices=['spx', 'uc1', 'br_econ_uncert']):
    
    for price_name in prices:
        price_df = read_data(price_name)
        ibov = ibov.merge(price_df, on='ref_date', how='left')
    
    return ibov


def fill_na_values(result):
    result['br_econ_uncert'] = result['br_econ_uncert'].fillna(method='ffill')
    result = result.dropna()
    
    return result


def get_train_data(resample_time='14B'):
    prices = ['spx', 'uc1', 'br_econ_uncert']
    
    ibov = read_data('ibov')
    result = merge_data_on_ibov(ibov, prices)
    result = fill_na_values(result)
    
    result = result.set_index('ref_date')
    
    result = result.resample(resample_time).agg({'close': 'last'})
    result.columns = result.columns.droplevel()
    result = result.pct_change().dropna()
    
    return result