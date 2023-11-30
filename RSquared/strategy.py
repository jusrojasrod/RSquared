# import utils
# import paths
import sectors as s
import data


class strategy:

    def __init__(self, y_back=5, start=None, end=None):
        self.start = start
        self.end = end
        self.y_back = y_back
        self.__ff_data = None

        # initialize tickers
        self.tickers = s.ETF_sectors  # define function to read tickers

    def etf_dates(self):
        pass

    def factors_dates(self):
        pass

    def _set_fama_french_data(self):
        self.__ff_data = data.famaFrenchdownload(self.start, self.end)[0]/100

    def _set_momento_data():
        pass

    def _set_etf_data():
        pass

    def _concat_factors():
        pass

    def returns():
        pass

    def excess_return():
        pass

    def plot_returns():
        pass

    def _regression():
        pass

    def join_reg_factors():
        pass

    def r_squared():
        pass

    def strategy():
        pass
