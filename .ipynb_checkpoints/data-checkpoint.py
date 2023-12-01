import pandas_datareader.data as reader
import yfinance as yf


def famaFrenchdownload(interval, start, end):
    """
    """
    if interval == "monthly":
        data = reader.DataReader('F-F_Research_Data_Factors',
                                 'famafrench',
                                 start, end)
        return data
    elif interval == "weekly":
        data = reader.DataReader('F-F_Research_Data_Factors_weekly',
                                 'famafrench',
                                 start, end)
        return data


def downloadData(tickers, start, end):
    return yf.download(tickers, start=start, end=end, interval="1mo")
