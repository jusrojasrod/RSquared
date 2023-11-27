import pandas as pd


def data_format(data):
    """
    """
    data.index = pd.to_datetime(data.index, format="%Y%m").to_period("M")
    return data
