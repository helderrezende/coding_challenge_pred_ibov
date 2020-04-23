def create_lags(data, columns):
    for col_name in columns:
        data['{0}_lag1'.format(col_name)] = data[col_name].shift(1)
        
    return data