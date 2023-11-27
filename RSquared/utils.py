import pandas as pd


def data_format(data, format="%Y%m", period="M"):
    """
    """
    data.index = pd.to_datetime(data.index, format=format).to_period(period)
    return data


def percentile(serie):
    """
    """
    return pd.qcut(serie, 5, labels=False)


def join_r2_alpha():
    pass
