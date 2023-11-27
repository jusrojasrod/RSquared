import pandas as pd


def data_format(data, format="%Y%m", period="M"):
    """
    """
    data.index = pd.to_datetime(data.index, format=format).to_period(period)
    return 
