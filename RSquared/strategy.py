import utils
import paths
import tickers as t


class strategy():

    def __init__(self, start=None, end=None):
        self.start = start
        self.end = end

        # initialize tickers
        self.tickers = t.TICKERS()  # define function to read tickers

    def etf_dates(self):
        pass

    def factors_dates(self):
        pass

    def fama_french_data():
        pass

    def momento_data():
        pass

    def etf_data():
        pass

    def concat_factors():
        pass

    def returns():
        pass

    def excess_return():
        pass

    def plot_returns():
        pass

    def regression():
        pass

    def join_reg_factors():
        pass

    def r_squared():
        pass

    def strategy():
        pass
